from django.contrib import admin
from django.urls import path, include

from product.views import ProductRegister, ProductList
from user.views import index, RegisterView, LoginView # 회원가입하기 위해 view갖고옴
#from product.views import ProductList

urlpatterns = [
    path('createPro/', ProductRegister.as_view()),
    path('', ProductList.as_view()),
]
