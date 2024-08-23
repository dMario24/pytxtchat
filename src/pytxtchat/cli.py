from pytxtchat.com import pong
from pytxtchat.textual import StopwatchApp

def ping():
    msg = pong()
    print(msg)


def run_stopwatch():
    app = StopwatchApp()
    app.run()
