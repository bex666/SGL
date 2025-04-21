import requests

def check_ip():
    return requests.get("https://api.ipify.org").text

def is_tor_used():
    ip = check_ip()
    try:
        response = requests.get("https://check.torproject.org/api/ip", timeout=5)
        return response.json().get("IsTor", False)
    except Exception:
        return False

def get_ip_info():
    ip = check_ip()
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
