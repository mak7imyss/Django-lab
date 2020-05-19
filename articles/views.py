from .models import Article
from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def test(request):
    return render(request, 'test.html', {"posts": Article.objects.all()})

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'content.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {'text': request.POST["text"], 'title': request.POST["title"]}
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                if Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = u"Название статьи уже существует"
                    return render(request, 'create_post.html', {'form': form})
                else:    
                    # если поля заполнены без ошибок
                    # Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    return redirect('get_article', article_id=article.id)
                    # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404

def auth(request):
    if request.user.is_authenticated:
        return redirect('archive')
    else:
        if request.method == 'POST':
            form = {
                'username' : request.POST['username'],
                'password' : request.POST['password']
            }

            user = authenticate(request, username=form['username'], password=form['password'])
            if user is not None:
                login(request, user)
                return redirect('archive')
            else:
                form['errors'] = u'Пользователь не найден!'
                return render(request, 'auth.html', {'form': form})
        else:
            return render(request, 'auth.html', {})

def registration(request):
    if request.method == 'POST':
        form = {
            'username': request.POST['username'],
            'mail': request.POST['mail'],
            'password': request.POST['password'],
        }
        if form["username"] and form["mail"] and form['password']:
            if len(form['password'])>6:
                if form['username'] in form['password']:
                    form['errors'] = u'Пароль содержит имя пользователя!'
                    return render(request, 'registration.html', {'form': form})
                else:
                    try:
                        User.objects.get(username = form['username'])
                        form['errors'] = u'Пользователь с таким именем уже существует!'
                        return render(request, 'registration.html', {'form': form})
                    except User.DoesNotExist:
                        User.objects.create_user(form['username'], form['mail'], form['password'])
                        user = authenticate(request, username=form['username'], password=form['password'])
                        login(request, user)
            else:
                form['errors'] = u'Пароль слишком короткий!'
                return render(request, 'registration.html', {'form': form})
        else:
            form['errors'] = u'Не все поля заполнены!'
            return render(request, 'registration.html', {'form': form})
        return redirect('archive')
    else:
        return render(request, 'registration.html', {})
