This is a simple `rabbit-mq` demo.

Demo is composed of three services:
1. **Rabbit MQ** the message broker. It can be easily set up using `docker` and running
`docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4-management`
It provides GUI at `localhost:15672`
2. Message sender defined in `send.py`. It is script to create messages in Message Broker queue.
3. Message receiver defined in `recieve.py`. It is simply parses messages that it receives and prints them out.