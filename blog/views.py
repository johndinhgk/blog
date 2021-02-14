from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.views.generic import ListView,DetailView
# Create your views here.
#def list(request):
#    Data = {'Posts': Post.objects.all().order_by("-date")}
#    return render(request,'blog/blog.html',Data)
#def post(request,id):
#    try:
#        post = Post.objects.get(id=id)
#    except Post.DoesNotExist:
#        raise Http404("Page does not exist")
#    return render(request,'blog/post.html',{'post':post})
class PostListView(ListView):
    queryset = Post.objects.all().order_by("-date")
    template_name = 'blog/blog.html'
    context_object_name = 'Posts'
    paginate_by = 1

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
