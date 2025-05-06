import pika

# define machine where Message Broker is running
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# define queue to which we are connecting
channel.queue_declare(queue='hello-queue')

# populate the queue
channel.basic_publish(exchange='', routing_key='hello-queue', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()