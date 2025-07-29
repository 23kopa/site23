# app/services/tokens_services/base_token.py
from abc import ABC, abstractmethod

class BaseTokenService(ABC):

    @abstractmethod
    def generate(self, user_id: int, **kwargs) -> str:
        pass

    @abstractmethod
    def process_trigger(self, token_uid: str, request):
        pass
