from pytxtchat.com import pong
from pytxtchat.textual.stopwatch import StopwatchApp
from pytxtchat.textual.chat import ChatApp
from pytxtchat.textual.weather import WeatherApp

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

