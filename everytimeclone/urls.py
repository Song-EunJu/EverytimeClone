from django.contrib import admin
from django.urls import path
from everytimeapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # html form을 이용해 블로그 객체 만들기
    path('new/', views.new, name='new'), # 새로운 글쓰는 화면
    path('create/', views.create, name='create'), # 글 생성하기

    # django form을 이용해 블로그 객체 만들기
    # path('new/', views.new, name='new'), # 새로운 글쓰는 화면
    path('formcreate/', views.formcreate, name='formcreate'), # 글 생성해주는 


    # django form을 이용해 블로그 객체 만들기
    # path('new/', views.new, name='new'), # 새로운 글쓰는 화면
    path('modelformcreate/', views.modelformcreate, name='modelformcreate') # 글 생성해주는 
]
