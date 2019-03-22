import pika
import sys
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='Hello')
'''
Message durability:
    # RabbitMQ doesn't allow you to redefine an existing queue with different parameters and 
    # return an error to any program that tries to do that.
    # so let's declare a queue with different name.
    channel.queue_declare(queue='task_queue', durable=True)
    
    # this queue_declare change needs to be applied to both the producer and consumer code.
    # besides, we need to mark our message as persistent--by supplying a delivery_mode property with value 2.
    channel.basic_publish(exchange='',
                      routing_key="task_queue",
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
'''


for i in range(50):
    message = "send from produce{}".format(i)
    channel.basic_publish(exchange='',
                          routing_key='Hello',
                          body=message)

    print("[x] Send {}".format(message))
    time.sleep(1)
'''
Round-robin dispatching:
    run two fanout_receive.py script at same time.  
    on average every consumer will get the same number of messages.
'''

connection.close()


