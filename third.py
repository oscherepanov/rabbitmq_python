import pika
import sys

SERVER_URL = 'rabbitmq.poas45.ru'

credentials = pika.PlainCredentials('user', 'vba34tu')
connection = pika.BlockingConnection(pika.ConnectionParameters(host=SERVER_URL,
                                                               credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()
