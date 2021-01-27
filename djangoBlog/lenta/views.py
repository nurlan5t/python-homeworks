from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from lenta.models import Post

@csrf_exempt
def show_lenta(request):
    if request.method == 'GET':
        return render(request, 'lenta.html', context={'posts': Post.objects.all()})

def add_post(request):
    if request.method == 'POST':
        data = request.POST
        post = Post.objects.create(image=data['image'], title=data['title'],
                                   description=data['description'])
        return HttpResponse('Post created')
    if request.method == 'GET':
        return render(request, 'add-post.html')
    else:
        return HttpResponse('Method not allowed')

def delete_post(request, id):
        del_post = Post.objects.get(id=id)
        del_post.delete()
        return HttpResponse('Post deleted')
        show_lenta()
@csrf_exempt
def add_like(request):
    return HttpResponse(
        f'method - {request.method} </br> </br> header - {request.headers} </br> </br> body - {request.body}'
    )

def add_comment(request):
    return HttpResponse('Added comment')

