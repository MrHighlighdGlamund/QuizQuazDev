from django.urls import path

from .views import index, quiz_data_view, quiz

urlpatterns = [
    path('', index, name='index'),
    path("<str:id>", quiz, name='quiz'),

    

        path('<str:id>/data', quiz_data_view, name='quiz_data_view'),
    ]

