import pika
import sys

def publisher(mes):
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.0.105'))
	channel = connection.channel()

	channel.queue_declare(queue='task_queue', durable=True)

	message=mes

	channel.basic_publish(
                   	exchange='',
                   	routing_key='task_queue',
                   	body=message,
                   	properties=pika.BasicProperties(delivery_mode = 2 ))

	print( " [x] Sent %r" % message)
	connection.close()