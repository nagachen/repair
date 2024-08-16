from django.urls import path
from .views import *
#log_list: 显示日志列表
#log_create: 创建新日志
#log_view: 查看特定日志
#log_reply: 回复特定日志
urlpatterns = [
    path('',LogList.as_view(),name='log_list'),
    path('create/',LogCreate.as_view(),name='log_create'),
    path('<int:pk>/',LogView.as_view(),name='log_view'),
    path('<int:pk>/reply/',LogReply.as_view(),name='log_reply'),
]
