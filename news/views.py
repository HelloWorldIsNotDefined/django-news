from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from django.contrib import messages

from .forms import SearchForm
import requests


class IndexView(View):
    template_name = 'news/index.html'
    form_class = SearchForm
    
    def get(self, request):
        
        form = self.form_class
        url = 'https://newsapi.org/v2/everything'
        title = request.GET.get('search')
        
        query_params = {
            'apikey': 'e6e93ac0f1124c848f5fd8c1bb15727a',
            'language':'en',
            'q':title,
        }

        response = requests.get(url, params=query_params)
        data = response.json()
        articles = data.get('articles')
        
        if not articles and title:
            messages.error(request, "Sorry we didn't find any results.", 'danger')
        
        page_obj = None
            
        if articles:
            paginator = Paginator(articles, 6)
            page_num = request.GET.get('page')
            page_obj = paginator.get_page(page_num)
        
        
        context = {
            'page_obj':page_obj,
            'articles':articles,
            'search': title,
            'form':form
        }
        
        return render(request, 'news/index.html', context)     