import random

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_world(request):
    message = """
    <html>
      <body>
       <p>Hello World!</p>
      </body>
    </html>
    """
    return HttpResponse(message)


def random_number(request):

    number = random.randint(0, 100)

    message = f"""
    <html>
      <body>
       <p>Wylosowano liczbę: {number}</p>
      </body>
    </html>
    """
    return HttpResponse(message)


def random_max_number(request, max_number):

    my_number = random.randint(0, max_number)

    message = f"""
    <html>
      <body>
       <p>Użytkownik podał wartość: {max_number}</p>
       <p>Wylosowano liczbę: {my_number}</p>
      </body>
    </html>
    """
    return HttpResponse(message)
