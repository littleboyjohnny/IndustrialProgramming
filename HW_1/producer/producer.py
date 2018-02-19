#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
channel = connection.channel()

channel.queue_declare(queue='hello')

#message = "HELLO WORLD!"
while True:   
	message = input('> ') 
	channel.basic_publish(exchange='', routing_key='hello', body=message)
	print(" [x] Send: %s" % message)

connection.close()
