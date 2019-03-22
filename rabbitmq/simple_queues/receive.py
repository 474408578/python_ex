import pika

connectin = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connectin.channel()

channel.queue_declare(queue='Hello')

# whenever we receive a message, this callback function is called by the pika library
def callback(ch, method, properties, body):
    print("[x] Received {}".format(body.decode()))

# tell RabbitMQ that this particular callback function should receive messages from our Hello queue
channel.basic_consume(callback, queue='Hello', no_ack=True)

print("[*] Waiting for message. To exit press CTRL + C")

# enter a never-ending loop waits for data and runs callback whenever necessary
channel.start_consuming()