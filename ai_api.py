import requests


def api(text: str, role: str, len_min: int, len_max: int, func: str, type: str) -> str:
    current_len = (int(len_max) + int(len_min)) / 2
    request = "%".join(text.split())
    session = requests.get("http://54.212.19.94:8081/session")
    print(session)
    url = f"http://54.212.19.94:8081/generate?request={request}?role={role}?lang=RU?id={session.text}?do={func}?ln={current_len}"
    print(url)
    answer = requests.get(url)
    return answer.text
