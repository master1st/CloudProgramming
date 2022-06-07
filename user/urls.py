from django.contrib.auth.views import LogoutView

from . import views
from django.contrib import admin
from django.urls import path, include
from user.views import index, RegisterView, LoginView, logout  # 회원가입하기 위해 view갖고옴
#from product.views import ProductList

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    #path('product/', ProductList.as_view())
]
