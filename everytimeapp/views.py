from django.shortcuts import render, redirect
from .models import Board # create 함수는 Board class로부터 게시글 하나씩 만들어내는 애니까 -> 클래스 객체얘기 다시 
from django.utils import timezone
from .forms import BoardForm, BoardModelForm

def home(request):
    return render(request, 'index.html')

# 게시판 글 작성 html 보여주는 함수
def new(request):
    return render(request, 'new.html')

# 게시판 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST'): 
        post = Board()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save() # 모델객체.save() 를 통해 모델 객체를 DB에 저장할 수 있음

# CREATE함수는 특정 HTML을 리턴해주는 함수가 아니자나? 
# 이거 다실행햇으면 특정 URL로 가라! Redirect해라 하는 명령보내

    return redirect('home')  # home함수를 redirect = index.html을 다시 띄워줘라


# django form 을 이용해 입력값 받는 함수
def formcreate(request):
    # django는 하나의 url에서 get / post요청을 모두 처리할 수 있음
    # form create에 get요청을 보낸것은? => 입력값을 받을 수 있는 html을 갖다준다!
    # form create에 post 요청을 보내면 -> 입력한 내용을db에 저장하는 기능 수행! form에서 입력한 내용을 처리
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = BoardForm(request.POST) # request.POST를 담고잇는 게시글 form을 만들어줌
        if form.is_valid(): # 폼에 입력된 값 유효성 검사
           post = Board()
           post.title = form.cleaned_data['title'] 
           post.body = form.cleaned_data['body']
           post.save()
           return redirect('home')
    else:
        # 입력받을 수 잇는 html을 갖다준다
        form = BoardForm() 
    return render(request, 'form_create.html', {'form':form})
    # 3번째 인자 : views.py 내의 데이터를 html에 넘겨줄 수 있음 (단, 딕셔너리 형태로 보내야함)

def modelformcreate(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = BoardModelForm(request.POST) # request.POST를 담고잇는 게시글 form을 만들어줌
        if form.is_valid(): # 폼에 입력된 값 유효성 검사
           form.save()
           return redirect('home')
    else:
        # 입력받을 수 잇는 폼이 담긴 html을 갖다준다
        form = BoardModelForm() 
    return render(request, 'form_create.html', {'form':form})
    # 3번째 인자 : views.py 내의 데이터를 html에 넘겨줄 수 있음 (단, 딕셔너리 형태로 보내야함)  
