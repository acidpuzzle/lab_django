import logging

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectListMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm

logger = logging.getLogger(__name__)


class PostMixin:
    model = Post
    model_form = PostForm


class PostList(PostMixin, ObjectListMixin, View):
    template = 'blog/post_list.html'


class PostDetail(PostMixin, ObjectDetailMixin, View):
    template = 'blog/post_detail.html'


class PostCreate(PostMixin, ObjectCreateMixin, View):
    template = 'blog/post_create.html'


class PostUpdate(PostMixin, ObjectUpdateMixin, View):
    template = 'blog/post_update.html'


class PostDelete(PostMixin, ObjectDeleteMixin, View):
    template = 'blog/post_delete.html'


#########################################################################################
# class PostCreate(View):
#     def get(self, request):
#         form = PostForm
#         return render(request, 'blog/post_create.html', context={'form': form})
#
#     def post(self, request):
#         bound_form = PostForm(request.POST)
#         if bound_form.is_valid():
#             new_post = bound_form.save()
#             return redirect(new_post)
#         return render(request, 'blog/post_detail.html', context={'form': bound_form})
#
#
# def posts_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', context={'posts': posts})
#
#
# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', context={'post': post})
#
#
# class PostDetail(View):
#     def get(self, request, slug):
#         # post = Post.objects.get(slug__iexact=slug)
#         post = get_object_or_404(Post, slug__iexact=slug)
#         return render(request, 'blog/post_detail.html', context={'post': post})
#########################################################################################


class TagMixin:
    model = Tag
    model_form = TagForm


class TagsList(TagMixin, ObjectListMixin, View):
    template = 'blog/tag_list.html'


class TagDetail(TagMixin, ObjectDetailMixin, View):
    template = 'blog/tag_detail.html'


class TagCreate(TagMixin, ObjectCreateMixin, View):
    template = 'blog/tag_create.html'


class TagUpdate(TagMixin, ObjectUpdateMixin, View):
    template = 'blog/tag_update.html'


class TagDelete(TagMixin, ObjectDeleteMixin, View):
    template = 'blog/tag_delete.html'


#########################################################################################
#
# class TagUpdate(View):
#     def get(self, request, url):
#         tag = Tag.objects.get(url__exact=url)
#         bound_form = TagForm(instance=tag)
#         return render(request, 'blog/tag_update.html', context={'form': bound_form, 'tag': tag})
#
#     def post(self, request, url):
#         tag = Tag.objects.get(url__exact=url)
#         bound_form = TagForm(request.POST, instance=tag)
#
#         if bound_form.is_valid():
#             updated_tag = bound_form.save()
#             return redirect(updated_tag)
#         return render(request, 'blog/tag_update.html', context={'form': bound_form, 'tag': tag})
#
#
# class TagCreate(View):
#     def get(self, request):
#         form = TagForm()
#         return render(request, 'blog/tag_create.html', context={'form': form})
#
#     def post(self, request):
#         print(request.POST)
#         bound_form = TagForm(request.POST)
#
#         if bound_form.is_valid():
#             new_tag = bound_form.save()
#             return redirect(new_tag)
#         return render(request, 'blog/tag_create.html', context={'form': bound_form})
#
#
# def tags_list(request):
#     tags = Tag.objects.all()
#     return render(request, 'blog/tag_list.html', context={'tags': tags})
#
#
# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', context={'tag': tag})
#
#
# class TagDetail(View):
#     def get(self, request, slug):
#         # tag = Tag.objects.get(slug__iexact=slug)
#         tag = get_object_or_404(Tag, slug__iexact=slug)
#         return render(request, 'blog/tag_detail.html', context={'tag': tag})
#########################################################################################
