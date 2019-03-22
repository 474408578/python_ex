import pika
import time


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

# create a queue with a random name.
result = channel.queue_declare(exclusive=True)
# once the consumer connection is closed, the queue should be deleted.
queue_name = result.method.queue

# bind the temporary queue to log exchange
channel.queue_bind(exchange='logs',
                   queue=queue_name)

print("[*] Waiting for logs. To exit press CTRL+C")

def callback(ch, method, properties, body):
    print("[x]{}".format(body.decode()))
    time.sleep(2)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
