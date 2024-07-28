from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, ListView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from .forms.create_post import PostForm

# Create your views here.
class MyPostTV(TemplateView):
    template_name = "mypost.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["profie_pic"] = "https://images.unsplash.com/photo-1719937050814-72892488f741?q=80&w=2072&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        context["username"] = "rhea_sidana"
        context["post_img"] = "https://img.freepik.com/free-photo/painting-mountain-lake-with-mountain-background_188544-9126.jpg"
        context["post_description"] = "This is a beautiful painting of a mountain lake with a stunning mountain background."
        context["likes"] = 3
        context["comments"] = 5
        context["share"] = 4
        context["save"] = 6

        return context


class MyPostDV(DetailView):
    template_name = "mypost-dv.html"
    model = Post
    context_object_name = "post"
    pk_url_kwarg = "id"

class MyPostCV(CreateView):
    model = Post
    template_name = "create_post.html"
    form_class = PostForm
    # fields= ["post_img", "post_description"]
    success_url = reverse_lazy("create-post-success-tv")

class CreatePostTV(TemplateView): 
    template_name = "success.html"

class MyPostsLV(ListView):
    model=Post
    template_name="myposts.html"
    context_object_name="posts"
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(post_description__icontains=query)
        return Post.objects.all()

class MyPostUV(UpdateView):
    model = Post
    template_name = "update_post.html"
    form_class = PostForm
    # fields= ["post_img", "post_description"]
    success_url = reverse_lazy("create-post-success-tv")
    pk_url_kwarg = "id"

class MyPostDLV(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("create-post-success-tv")
    pk_url_kwarg = "id"