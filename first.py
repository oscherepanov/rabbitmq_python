import pika

SERVER_URL = 'rabbitmq.poas45.ru'

credentials = pika.PlainCredentials('user', 'vba34tu')
connection = pika.BlockingConnection(pika.ConnectionParameters(host=SERVER_URL,
                                                               credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
