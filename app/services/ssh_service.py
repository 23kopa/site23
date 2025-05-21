import paramiko
from config.settings import Config

VPS_IP = Config.VPS_IP
VPS_USER = Config.VPS_USER
VPS_PASSWORD = Config.VPS_PASSWORD

# ! SSH Connect to VPS
def ssh_execute(command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(VPS_IP, username=VPS_USER, password=VPS_PASSWORD)
        stdin, stdout, stderr = ssh.exec_command(command)
        return stdout.read().decode(), stderr.read().decode()
    except Exception as e:
        return "", f"SSH error: {e}"
    finally:
        ssh.close()

