from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='homepage'),
    path('post/<int:id>', views.single_page, name='single')
]