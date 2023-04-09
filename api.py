import requests


def api(text_area: str, role: str, range_slider_min: int, range_slider_max: int, func: str, type: str) -> str:
    small_text}<br>Выбранный текст: {select_text}<br>{select_function}
    request = "%".join(text.split())
    session = requests.get("http://54.212.19.94:8081/session")
    print(session)
    url = f"http://54.212.19.94:8081/generate?request={request}?role={role}?lang=RU?id={session.text}?do={func}"
    print(url)
    answer = requests.get(url)
    return answer.text
