# django-rabbitmq-demo

How to run this project?
1). First run the rabbitmq container by the following command
docker run -itd --rm --name rabbitmq -p 5672:5672 -p 15672:15672 --net=my-network -v /var/lib/rabbitmq:/var/lib/rabbitmq --hostname rabbitmq rabbitmq:3-management


2). second run the django container by the following command
docker run -itd -p 8000:8000 --net=my-network djangorabbitmq

both the containers should be in the same network

Testing
1). send the request from the postman [POST] request, to the django url http://localhost:8000/send/ , by editing body x-www-form-urlencoded (message:hello demo msg)
2). you can also use the curl command, curl -X POST -d "message=Hello, RabbitMQ!" http://localhost:8000/send/


dockerimage - https://hub.docker.com/repository/docker/zabakar/djangorabbitmq/general



