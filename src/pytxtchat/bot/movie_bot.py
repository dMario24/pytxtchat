from pytxtchat.kafka.consumer import create_consumer
from pytxtchat.kafka.producer import create_producer

def run(topic_name: str, bootstrap_server:str, offset_reset='latest'):
  bootstrap_server_list = [bootstrap_server]
  pro = create_producer(bootstrap_server_list)
  con = create_consumer(topic_name=topic_name, bootstrap_server_list=bootstrap_server_list, offset_reset=offset_reset)

  for m in con:
    data = m.value
    to = data['to']
    msg = data['msg']

    if "@bot" in msg:
      bot_msg = {
            "to" : "bot",
            "msg" : "몰라"
      }

      pro.send(topic=topic_name, value=bot_msg)
      pro.flush()

      print(f"Q:{msg} A:{bot_msg['msg']}")
