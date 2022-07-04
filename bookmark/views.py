import imp
from msilib.schema import Class
from re import I, template
from tempfile import tempdir
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from bookmark.models import Bookmark

# Create your views here.

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 1

class BookmarkCreateView(CreateView):
    model = Bookmark                # 어떤 모델의 입력을 받을 것인가
    fields = ['site_name', 'url']   # 어떤 필드들을 입력받을 것인가
    success_url = reverse_lazy('list') # 글쓰기를 완료하고 이동할 페이지
    template_name_suffix = '_create'   # 사용할 템플릿의 접미사만 변경하는 설정값

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')