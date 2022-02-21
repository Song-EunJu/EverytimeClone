from django.db import models

class Board(models.Model): # models 안의 Model (이미 구현되어있는 장고의 모델 기능 사용) 을 상속해서 만들어짐
    # 데이터베이스 테이블의 열들을 선언 + 데이터 형식과 함께
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) #자동으로 지금 시간 추가

    def __str__(self):
        return self.title