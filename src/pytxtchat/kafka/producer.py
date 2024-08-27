from kafka import KafkaProducer
import json

def create_producer(bootstrap_server_list: list) -> KafkaProducer:
    pro = KafkaProducer(
        bootstrap_servers=bootstrap_server_list,
        value_serializer=lambda x:json.dumps(x).encode('utf-8')
        )
    return pro
    

# def send_msg(topic: str, msg: dict):
#     pro.send(topic=topic, value=msg)
#     pro.flush()
