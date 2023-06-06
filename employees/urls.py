from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('update/<int:id>', views.update, name='update'),
]
