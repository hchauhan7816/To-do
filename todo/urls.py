from django.urls import path, include
from .views import show_todo_list, update_item, delete_item

urlpatterns = [
    path('', show_todo_list, name="ghumad"),
    path('update/<int:pkk>', update_item, name="garaj"),
    path('delete/<int:pkk>', delete_item, name="ghamdu"),
]
