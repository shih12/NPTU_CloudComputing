import pika
import time
import logging
import warnings
import json
import pymongo
import sql_connection

# configure logger
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
warnings.filterwarnings("ignore", category=DeprecationWarning) 

# connection configurations
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)


def callback(ch, method, properties, body):


    message = body.decode("utf-8") 
    logging.info(message)
    time.sleep(1)

    data = json.loads(message)
    
    ch.basic_ack(delivery_tag=method.delivery_tag)
    username = data['username']
    password = data['password']

    sql_connection.connt(username,password)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()
