import pika
import time

connectin = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connectin.channel()

channel.queue_declare(queue='Hello')
'''
Message durability:
    # RabbitMQ doesn't allow you to redefine an existing queue with different parameters and 
    # return an error to any program that tries to do that.
    # so let's declare a queue with different name.
    channel.queue_declare(queue='task_queue', durable=True)

    # this queue_declare change needs to be applied to both the producer and consumer code.
    
'''

def callback(ch, method, properties, body):
    print("[x] Received {}".format(body.decode()))
    time.sleep(2)
    print("[x] Done")
    # send a proper acknowledgment from the worker
    ch.basic_ack(delivery_tag=method.delivery_tag)


# channel.basic_qos(prefetch_count=1)
'''
Fair dispatch:
    RabbitMQ doesn't look at the number of unacknowledged message for a consumer. 
    It just blindly dispatches every n-th message to n-th consumer.
    channel.basic_qos(prefetch_count=1) make sure RabbitMQ don't dispatch a new message to a worker until it has processed and acknowledged the previous,
    instead, it will dispatch it to the next worker that is not still busy.
'''


# channel.basic_consume(callback, queue='Hello', no_ack=True)
channel.basic_consume(callback, queue='Hello')

'''
Message acknowledgment:
    in order to make sure a message is never lost, RabbitMQ support message acknowledgments.
    a acknowledgement is sent back by the consumer to tell RabbitMQ that a particular message had been received, 
    processed and that RabbitMQ is free to delete it.
'''

print("[*] Waiting for message. To exit press CTRL + C")

channel.start_consuming()