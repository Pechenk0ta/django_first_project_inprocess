from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect, Http404

from .models import News
from .models import Category
from .models import Coments_1
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Likes_At_News

"""

/NEWS/ID

"""
'''
Процесс получения рендера страницы новости/процесс комменатрия
'''
def News_Processes_comments(request, id):
    if request.method == 'GET':
        return article_detailed(request, id)
    elif request.method == 'POST':
        return Get_comment(request, id)



"""
Получение и обработка коментария
"""

@login_required
def Get_comment(request, id):
    coment_content = request.POST.get('coment')
    new_coment = Coments_1.objects.create(content=coment_content,post_id_id = id,user = request.user)

    return redirect("News_Processes_comments",id)

"""
Обработка и выдача страницы
"""




def article_detailed(request, id):
    try:
        article = News.objects.get(pk=id)
        category = Category.objects.get(pk = article.category_id)
        comments = Coments_1.objects.filter(post_id_id=id)
        author = User.objects.get(pk = article.author_id).username
        likes_count = Likes_At_News.objects.filter(on_post_id = id).count()

        context = {
            'article': article,
            'title': article.title,
             'category': category,
            'comments' : comments,
            'author': author,
            'id': id,
            'likes_count': likes_count
        }
        return render(request, 'polls/news_content.html', context=context)
    except News.DoesNotExist:
        return HttpResponse('Error Happened')


"""

NEWS / CREATE

"""

"""
Создание новости получение хтмл
"""
def get_news_form(request):
    return render(request, 'polls/index.html')


"""
Обработка полученных данных из создания новости
"""
@login_required
def processing_news_form(request):
    content1 = request.POST.get('content')
    label1 = request.POST.get('title')
    category1 = request.POST.get('secelt-category')
    category = Category.objects.get(title=category1).id
    news1 = News.objects.create(title=label1,content=content1,category_id = category, author =request.user)
    return redirect('News_Processes_comments',id = news1.id)


"""
Процесс получения новости
"""
def processes_forms(request):
    if request.method == 'GET':
        return get_news_form(request)
    elif request.method == 'POST':
        return processing_news_form(request)


"""

NEWS/Search

"""


"""
Процесс работы /search в зависимости от реквест метода
"""

def Filter_processes(request):
    if request.method == 'GET':
        return Get_Search_Form(request)
    elif request.method == 'POST':
        return News_Post_filter(request)

"""
Процес выдачи страницы search
"""

def Get_Search_Form(request):
    return render(request, 'polls/search-form.html')


"""
Процес обработки фильтра
"""

def News_Post_filter(request):
    category = request.POST.get('secelt-category')
    category1 = Category.objects.get(title = category).id
    return redirect('Search_Output', id = category1)


"""
Процесс выдачи информации с фильтром
"""

def Search_Output(request, id):
    news1 = News.objects.filter(category_id = id)
    context ={
        'news':news1
    }
    return render(request, 'polls/Search_response.html',context=context)


"""
Главная страница
"""

def main(requerst):
    return render(requerst, 'main.html')


"""
Лайки обработка 
"""
@login_required
def like_get(request, id):
    likes_on_post = Likes_At_News.objects.filter(on_post = id, from_user = request.user.id)
    print(len(likes_on_post))
    if len(likes_on_post) == 0:
        Likes_At_News.objects.create(from_user_id = request.user.id, on_post_id = id)
    else:
        Likes_At_News.objects.filter(from_user_id=request.user.id, on_post_id=id).delete()
    return redirect("News_Processes_comments",id)
