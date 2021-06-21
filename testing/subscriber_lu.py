import pika
import time
import sql

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.120'))
channel = connection.channel()


channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" %body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    sql.sql(body)
    ch.basic_ack(delivery_tag = method.delivery_tag)	

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)



channel.start_consuming()