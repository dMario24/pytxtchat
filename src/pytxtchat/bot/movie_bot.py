from pytxtchat.kafka.consumer import create_consumer
from pytxtchat.kafka.producer import create_producer
from pytxtchat.data.manager import search_movie

def run(topic_name: str, bootstrap_server:str, offset_reset='latest'):
  bootstrap_server_list = [bootstrap_server]
  pro = create_producer(bootstrap_server_list)
  con = create_consumer(topic_name=topic_name, bootstrap_server_list=bootstrap_server_list, offset_reset=offset_reset)

  for m in con:
    data = m.value
    to = data['to']
    msg = data['msg']

    if "@bot" in msg:

      try:

        start_index = msg.index('"') + 1
        end_index = msg.rindex('"')
        movie_title = msg[start_index:end_index]
        
        r = search_movie(movie_title)
      except:
        r = "몰라"
      
      bot_msg = {
            "to" : "bot",
            "msg" : r
      }

      pro.send(topic=topic_name, value=bot_msg)
      pro.flush()

      print(f"Q:{msg} A:{bot_msg['msg']}")
