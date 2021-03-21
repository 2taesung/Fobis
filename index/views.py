from django.shortcuts import render, redirect
from .models import Notice
from .forms import NoticeForm

# Create your views here.
def index(request):

    return render(request, 'index/index.html')

def list(request):
    notice = Notice.objects.all()
    # print(notice)
    context = {
        'notice': notice,
    }

    return render(request, 'index/list.html', context)

def detail(request, notice_pk):
    notice = Notice.objects.get(pk=notice_pk)
    # print(notice)
    context = {
        'notice': notice,
    }
    return render(request, 'index/detail.html', context)

def update(request, notice_pk):
    notice = Notice.objects.get(pk=notice_pk)
    if request.method == 'POST':
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            return redirect('index:detail', notice.pk)
    else:
        form = NoticeForm(instance=notice)

    context = {
        'form': form,
        'notice': notice,
    }

    return render(request, 'index/update.html', context)

def delete(request, notice_pk):
    notice = Notice.objects.get(pk=notice_pk)
    notice.delete()

    return redirect('index/index.html')

def create(request):
    if request.method == "POST":
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save()
            return redirect('index:list')
    else:
        form = NoticeForm()

    context = {
        'form': form,
    }

    return render(request, 'index/create.html', context)