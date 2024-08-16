from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse
from .models import LogItem
# Create your views here.

class LogList(ListView):
    model = LogItem
    ordering = ['-id']
    
class LogCreate(CreateView):
    model = LogItem
    # 新增時只顯示需填寫的部份欄位
    fields = ['subject','description','reporter','phone']
    
    def get_success_url(self):
        return reverse('log_list')
    
class LogReply(UpdateView):
    model = LogItem
    fields = ['handler','status','comment']
    
    def get_success_url(self):
        #使用 reverse 函数反向解析 log_view URL，并将回复的日志的 id 
        # 作为 pk 参数传递，并返回该 URL 以便重新導向到查看该具体日志的详情页面。
        return reverse('log_view',kwargs={'pk':self.object.id})
