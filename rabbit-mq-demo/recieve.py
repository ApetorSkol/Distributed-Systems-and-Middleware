from datetime import datetime
import pika, sys, os


def main():
    # define machine to where Message Broker is located
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # define queue
    channel.queue_declare(queue='hello-queue')

    def callback(ch, method, properties, body):
        print(f"{datetime.now()} [x] Received {body}")

    # parse recieved message
    channel.basic_consume(queue='hello-queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)