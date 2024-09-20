from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from .models import GuessNumbers
from django.shortcuts import render, redirect

def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/templates/lotto/default.html', {'lottos':lottos})

def hello(request) :
        return HttpResponse('<h1 style = "color:red">Hello, world!</h1>')

def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)  #사용자로부터 넘겨져 온 POST 요청 데이터

        if form.is_valid():
            # 사용자로부터 입력받은 form 데이터에서 추가로 수정해주려는 사항이 있을 경우 save를 보류함
            lotto = form.save(commit=False)
            lotto.generate()
            return redirect('index')
    else:
        form = PostForm()  # empty form
        return render(request, "lotto/templates/lotto/form.html", {"form": form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey)
    return render(request, "lotto/templates/lotto/detail.html", {"lotto": lotto})
