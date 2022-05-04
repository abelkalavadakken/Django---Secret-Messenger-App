from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View
from .models import Message
from .forms import MessageForm
from django.contrib.auth.models import User

# Create your views here.



class MessageView(View):
    def get(self, request):
        if(request.user.is_authenticated):
            # form=MessageForm()
            msgs=Message.objects.filter(user=request.user)
            name = request.user.username
            return render(request,'msg.html',{'name':name,'msgs':msgs})
        return render(request,'msg.html',{'error':'Permission Denied'})
    def post(self, request, username):
        text = request.POST.get('text')
        user = User.objects.get(username=username)
        Message.objects.create(text=text, user=user)
        # form = MessageForm()
        msgs = Message.objects.filter(user=request.user)
        name = request.user.username
        return render(request,'msg.html', {'name': name, 'user':user,  'msgs': msgs, 'rec': True})
        

class MessageSend(View):
    def get(self, request, username):
        print(username)
        form = MessageForm()
        user = User.objects.get(username=username)
        print(user)
        return render(request,'send-msg.html', {'form':form, 'user':user})
    def post(self, request, username):
        text = request.POST.get('text')
        user = User.objects.get(username=username)
        Message.objects.create(text=text, user=user)
        form = MessageForm()
        return render(request,'send-msg.html', {'form':form, 'user':user})