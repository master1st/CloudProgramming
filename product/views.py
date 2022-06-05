from django.shortcuts import render
from .models import Product
from .forms import RegisterForm
from django.views.generic import FormView, ListView


class ProductRegister(FormView):
    template_name = 'product_register.html'
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
    template_name = 'product_list.html'
    model = Product
    ordering = '-pk'

    # CBV방식은 FBV방식과 다르게 이미 기정의된 클래스 라이브러리를 상속받아 정의된 기능을 사용하는것
    # postlist역시 포스트들을 가져와서 나열해주는 역할만하고, 즉 post에 대한 정보만 들어있고, 다른 데이터를 같이 매개변수로 전달해주고싶다면,
    # 그렇다면 get_context_data 메서드라이브러리를 사용해서, context 딕셔너리에 담아 데이터전달.
    # def get_context_data(self, **kwargs):
    #     context = super(PostList, self).get_context_data()
    #     context['categories'] = Category.objects.all()
    #     context['no_category_post_count'] = Post.objects.filter(category=None).count()
    #
    #     return context
