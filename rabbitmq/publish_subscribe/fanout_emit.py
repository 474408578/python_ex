import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# crate a fanout log exchange
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

'''
fanout exchange just broadcasts all message it received to all queues it know
the default exchange:
    channel.basic_publish(exchange='', routing_key='Hello', body=message)
'''

for i in range(20):
    message = "hello exchange{}".format(i)
    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body=message)
    print("[x] Send {}".format(message))
    time.sleep(1)

connection.close()



