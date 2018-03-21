from django.conf.urls import url

from axf import views


urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^mine/', views.mine, name='mine'),
    url(r'^market/$', views.urlToMarket, name='urlToMarket'),
    url(r'^market/(\d+)/(\d+)/(\d+)', views.market, name='market'),
    url(r'^cart/', views.cart, name='cart'),

    url(r'^login/', views.login, name='login'),
    url(r'^do_login/', views.do_login, name='do_login'),
    url(r'^register/', views.register, name='register'),
    url(r'^do_register/', views.do_register, name='do_register'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^user_info/', views.user_info, name='user_info'),
    url(r'^do_user_info/', views.do_user_info, name='do_user_info'),

    url(r'^check_user/', views.check_user, name='check_user'),
    url(r'^check_user_info/', views.check_user_info, name='check_user_info'),

    url(r'^addtocart/', views.add_to_cart, name='add_to_cart'),
    url(r'^changeselect/', views.change_select, name='change_select'),
    url(r'^cart_goods_sub/', views.cart_goods_sub, name='cart_goods_sub'),
    url(r'^cart_goods_add/', views.cart_goods_add, name='cart_goods_add'),
    url(r'^gen_order/', views.gen_order, name='gen_order'),


    url(r'^pay/(\d+)', views.pay, name='pay'),
]
