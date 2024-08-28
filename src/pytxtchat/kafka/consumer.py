from kafka import KafkaConsumer
from json import loads

def create_consumer(topic_name: str, bootstrap_server_list: list, offset_reset='earliest') -> KafkaConsumer:    
        consumer = KafkaConsumer(
                topic_name,
                bootstrap_servers=bootstrap_server_list,
                value_deserializer=lambda x: loads(x.decode('utf-8')),
                #consumer_timeout_ms=5000,
                auto_offset_reset='earliest', #'earliest' 'latest'
                # group_id="fbi",
                # enable_auto_commit=True,
        )

        return consumer
        
