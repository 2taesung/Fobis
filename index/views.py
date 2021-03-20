from django.shortcuts import render
from .models import Notice

# Create your views here.
def index(request):

    return render(request, 'index/index.html')

def list(request):
    notice = Notice.objects.all()
    print(notice)
    context = {
        'notice': notice,
    }

    return render(request, 'index/list.html', context)

def detail(request, notice_pk):
    notice = Notice.objects.all()

    context = {
        'notice': notice,
    }
    return render(request, 'index/detail.html', context)