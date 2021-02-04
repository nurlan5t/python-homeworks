from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Post_Comment
from django.views import generic
from .forms import CommentForm

class PostView(generic.ListView):
    template_name = 'lenta.html'
    queryset = Post.objects.all()

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post-detail.html'
    extra_context = {'form': CommentForm()}

    @csrf_exempt
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST, initial={'post': post})
        if form.is_valid():
            form.save()
        return self.get(request, *args, **kwargs)

class PostCreateView(generic.CreateView):
    template_name = 'add-post.html'
    model = Post
    fields = [
        'title',
        'description',
        'image'
    ]
class PostEditView(generic.UpdateView):
    model = Post
    template_name = 'edit-post.html'
    fields = [
        'title',
        'description',
        'image'
    ]

class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = '/'
    template_name = 'delete_post.html'


@csrf_exempt
def add_like(request):
    return HttpResponse(
        f'method - {request.method} </br> </br> header - {request.headers} </br> </br> body - {request.body}'
    )

@csrf_exempt
def add_comment(request, pk):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        data = request.POST
        comment_post = Post_Comment.objects.create(post=post['pk'],text=data['text'])
        comment_post.save()
        return HttpResponse(f'Added comment {comment_post.text}')
    if request.method == 'GET':
        return render(request, 'post-detail.html')
    else:
        return HttpResponse('Method not allowed')
