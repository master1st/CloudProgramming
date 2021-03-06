from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Tag, Category
from .forms import RegisterForm
from django.views.generic import FormView, ListView, DetailView
from .forms import CommentForm

import stripe
from django.conf import settings


class ProductRegister(FormView):

    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            stock=form.data.get('stock'),
            description=form.data.get('description')
        )
        product.save()
        return super().form_valid(form)


class ProductList(ListView):

    model = Product
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Product.objects.filter(category=None).count()

        return context

    def show_tag_posts(request, slug):
        tag = Tag.objects.get(slug=slug)
        product_list = tag.product_set.all()

        context = {
            'categories': Product.objects.all(),
            'tag': tag,
            'product_list': product_list
        }
        return render(request, 'product/product_list.html', context)


class ProductDetail(DetailView):
    # template_name = 'product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        context['comment_form'] = CommentForm
        return context

    def show_tag_posts(request, pk):
        product = Product.objects.get(pk=pk)
        product_detail = product.product_set.all()

        context = {
            'categories': Product.objects.all(),
            'product': product,
            'product_detail': product_detail,
            'stripe.api_key': settings.STRIPE_SECRET_KEY,
            'description': '?????? ????????? ????????????!',
            'data_key': settings.STRIPE_PUBLIC_KEY,
        }
        return render(request, 'product/product_detail.html', context, )

# def show_category_posts(request, slug):
#         if slug == 'no-category':
#             category = '?????????'
#             product_list = Product.objects.filter(category=None)
#         else:
#             category = Category.objects.get(slug=slug)
#             product_list = Product.objects.filter(category=category)
#             # ?????? ?????? ????????? ???????????????. ??????
#         context = {
#             'categories': Category.objects.all(),
#             'no_category_post_count': Product.objects.filter(category=None).count(),
#             'category': category,
#             'product_list': product_list
#         }
#         return render(request, 'product/product_detail.html', context)


def addComment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Product, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied

def show_category_posts(request, slug):
    if slug == 'no-category':
        category = '?????????'
        product_list = Product.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        product_list = Product.objects.filter(category=category)
        # ?????? ?????? ????????? ???????????????. ??????
    context = {
        'categories': Category.objects.all(),
        'no_category_post_count': Product.objects.filter(category=None).count(),
        'category': category,
        'product_list': product_list
    }
    return render(request, 'product/product_list.html', context)

    # CBV????????? FBV????????? ????????? ?????? ???????????? ????????? ?????????????????? ???????????? ????????? ????????? ???????????????
    # postlist?????? ??????????????? ???????????? ??????????????? ???????????????, ??? post??? ?????? ????????? ????????????, ?????? ???????????? ?????? ??????????????? ????????????????????????,
    # ???????????? get_context_data ??????????????????????????? ????????????, context ??????????????? ?????? ???????????????.
    # def get_context_data(self, **kwargs):
    #     context = super(PostList, self).get_context_data()
    #     context['categories'] = Category.objects.all()
    #     context['no_category_post_count'] = Post.objects.filter(category=None).count()
    #
    #     return context
