"""Labwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from member.views import show_member_info
from TalkTopic.views import receive_post, show_talk_info

##override the 404_errorPage and 500_errorPage
handler404 = "Labwebsite.views.error_views.error_404"
handler500 = "Labwebsite.views.error_views.error_500"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member_info/', show_member_info),
    path('member_info2/', receive_post),
    path('teacher_page/', show_talk_info),
]
