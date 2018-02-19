#!/usr/bin/env python
import pika
import time
import pg8000 as ps2

time.sleep(60)

print(" [*] I'm here!")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
channel = connection.channel()

conn = ps2.connect(user="postgres", password="postgres", host="db")
cur = conn.cursor()
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

channel.queue_declare(queue='hello')

print(" [*] Waiting for messages. To exit press CTRL+C")

def callback(ch, method, properties, body):
    print(" [x] Received")
    cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (1, body))
    print(" [x] Send to psql")

channel.basic_consume(callback, queue='hello', no_ack=True)

channel.start_consuming()
