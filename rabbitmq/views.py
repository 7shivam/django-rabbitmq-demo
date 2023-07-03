# myapp/views.py

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pika

@csrf_exempt
def send_to_rabbitmq(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        if message:
            send_message_to_rabbitmq(message)
            return HttpResponse("Message sent to RabbitMQ")
    
    return HttpResponse("Invalid request")


def send_message_to_rabbitmq(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='shivam-test-queue', durable=True)
    channel.basic_publish(exchange='', routing_key='shivam-test-queue', body=message,
                         properties=pika.BasicProperties(delivery_mode=2))
    connection.close()
    print("Sent message to RabbitMQ:", message)

