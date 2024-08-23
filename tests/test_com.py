from pytxtchat.com import pong

def test_pong():
    msg = pong()
    assert msg == "pong"
