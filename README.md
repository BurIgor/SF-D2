# SF-D2

В переменные окружения добавьте адрес вашего сайта в sentry.io,  это можно сделать,   
добавив переменные окружения,  
  - редактируя конфигурацию в PyCharm,   
  - либо задав адрес в переменной SENTRY_DSN в файле env.py,   
  - либо явно задав его в переменной my_SENTRY_DSN в файле server.py.  


Для проверки работы программы задайте пути:  

http://localhost:8081/success - возвращает 200  

http://localhost:8081/fail - возвращает 500, в sentry передается сообщение об ошибке.  


Кроме того, проверить работу программы можно здесь:  https://murmuring-inlet-05721.herokuapp.com/
