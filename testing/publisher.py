import pika
import sys

def publish(mes):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.120'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    #  設置參數接收外部呼叫程式時傳入的字串
    message = ' '.join(sys.argv[1:]) or mes

    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(delivery_mode = 2)
    )


    connection.close()
