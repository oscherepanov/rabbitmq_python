import sys

import pika

message = ' '.join(sys.argv[1:]) or "Hello World!"

SERVER_URL = 'rabbitmq.poas45.ru'

credentials = pika.PlainCredentials('user', 'vba34tu')
connection = pika.BlockingConnection(pika.ConnectionParameters(host=SERVER_URL,
                                                               credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print(f" [x] Sent '{message}'")
connection.close()
