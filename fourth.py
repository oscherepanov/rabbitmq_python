import pika
import sys

SERVER_URL = 'rabbitmq.poas45.ru'

credentials = pika.PlainCredentials('user', 'vba34tu')
connection = pika.BlockingConnection(pika.ConnectionParameters(host=SERVER_URL, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
