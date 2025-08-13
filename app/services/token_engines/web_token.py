# app/services/tokens_services/web_token_service.py
import hashlib
import uuid
from datetime import datetime
from flask import request, render_template
from app.services.kv.redis_store import store_token, get_token, update_token

from .base_token import BaseTokenService
import requests


class WebTokenService(BaseTokenService):

    PREFIX = "web_token:"

    def generate_token_uid(self) -> str:
        random_bytes = uuid.uuid4().bytes + uuid.uuid4().bytes
        return hashlib.sha1(random_bytes).hexdigest()

    def generate(self, user_id: int, email: str = None, alert_message: str = None) -> str:
        token_uid = self.generate_token_uid()
        base_url = request.host_url.rstrip('/')
        trigger_url = f"{base_url}/token/{token_uid}/img.gif"

        store_token(token_uid, {
            'user_id': user_id,
            'email': email,
            'alert_message': alert_message,
            'triggered_at': None,
            'token_metadata': {
                'trigger_url': trigger_url,
                'created_at': datetime.utcnow().isoformat()
            }
        })
        return trigger_url

    def process_trigger(self, token_uid: str, request):
        token_data = get_token(token_uid)
        if not token_data:
            return "Not found", 404

        triggered_at = datetime.utcnow()

        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        if ip and ',' in ip:
            ip = ip.split(',')[0].strip()
        if ip in ('127.0.0.1', '10.8.1.2', '192.168.106.85'):
            ip = '185.22.172.242'  # заглушка

        user_agent = request.headers.get("User-Agent")

        geo_info = {}
        try:
            r = requests.get(
                f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,lat,lon,org,as,isp,query"
            )
            if r.status_code == 200 and r.json().get("status") == "success":
                geo_info = r.json()
        except Exception as e:
            print("Geo lookup failed:", e)

        prev_meta = token_data.get("token_metadata", {})
        update_token(token_uid, {
            "triggered_at": triggered_at.isoformat(),
            "token_metadata": {
                **prev_meta,
                'ip': ip,
                'user_agent': user_agent,
                'geo_info': geo_info,
                'trigger_time': triggered_at.isoformat(),
                'trigger_url': prev_meta.get('trigger_url')
            }
        })

        return render_template('base/trigger_gif.html', gif_url='/static/images/gif/spbgut.gif')

    def get_token_data(self, token_uid: str) -> dict | None:
        return get_token(token_uid)


web_token_service = WebTokenService()


def generate_web_token(user_id: int, email: str = None, alert_message: str = None) -> str:
    return web_token_service.generate(user_id, email, alert_message)
