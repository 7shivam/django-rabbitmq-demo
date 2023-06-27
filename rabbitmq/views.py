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
    channel.queue_declare(queue='shivam-test-queue')
    channel.basic_publish(exchange='', routing_key='shivam-test-queue', body=message)
    connection.close()
    print("Sent message to RabbitMQ:", message)

