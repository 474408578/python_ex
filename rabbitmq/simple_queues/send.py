import pika

# establish a connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create hello queue
channel.queue_declare(queue='Hello')

# send a message to Hello queue
channel.basic_publish(exchange='',
                      routing_key='Hello',
                      body='Hello World!')
'''
routing_key = queue
'''

print("[x] Send 'Hello World!'")

# close the connection
connection.close()


