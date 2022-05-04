from django.urls import path
from msg_manager.views import MessageView, MessageSend



urlpatterns = [
    
    path('', MessageView.as_view()), 
    path('<username>', MessageSend.as_view()), 
    
]