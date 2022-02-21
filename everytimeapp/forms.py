from django import forms # 장고에서 기본으로 제공하는 폼 기능
from .models import Board # board를 기반으로 form을 자동생성해주기 위해서 

# form을 정의할 수 있는 임의의 python file 폼을 만들어서 장고로 부터 forms 를 import 해와서 class로서 form을 정의해준다
class BoardForm(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)


class BoardModelForm(forms.ModelForm):
    class Meta:
        model = Board # 어떤 클래스를 기반으로 폼을 만들거냐 -> 애초에 폼을 기반으로 만들어진거고 위에꺼즌 내가 직접 작성해서 views.py에서도 일일히 넣어줌
        fields = '__all__' # 어떤 필드를 입력받을것이냐 -> board model의 모든 속성이 폼의 대상이 됨
        # fields = ['title'] # 특정 데이터로만 폼을 만들고싶은 경우
