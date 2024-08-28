from pytxtchat.com import pong
from pytxtchat.textual.stopwatch import StopwatchApp
from pytxtchat.textual.chat import ChatApp
from pytxtchat.textual.weather import WeatherApp
import typer, fire
import requests

def ping():
    msg = pong()
    print(msg)
    
def run_chat():
    app = ChatApp()
    app.run()

def run_stopwatch():
    app = StopwatchApp()
    app.run()

def run_weather():
    app = WeatherApp()
    app.run()

def weather_fire():
    fire.Fire(print_weather)

def weather_typer():
     typer.run(print_weather)
     

def print_weather(city: str, lang='ko') -> None:
    """날씨를 알려드립니다.
    
    https://wttr.in/:help
    
    Args:
        city: 도시이름
        lang: 표현언어
    """
    url = f"https://wttr.in/{city}?lang={lang}"
    response = requests.get(url)
    print(response.text)