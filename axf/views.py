import hashlib

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from axf.models import Wheel, Nav, MustBuy, Shop, MainShow, FoodTypes, Goods, User, Cart, Order


def home(request):
    title = '主页'
    # 查询主页面中的数据
    wheels = Wheel.objects.all()
    # 查询导航
    navs = Nav.objects.all()
    # 第二个轮播
    mustBuys = MustBuy.objects.all()
    # 便利商店
    shops = Shop.objects.all()
    shops_more = shops[3:7]
    shops_rec = shops[7:]
    # main_show
    main_shows = MainShow.objects.all()

    context = {'wheels': wheels,
               'navs': navs,
               'mustbuys': mustBuys,
               'shops': shops,
               'shops_more': shops_more,
               'title': title,
               'shops_rec': shops_rec,
               'main_shows': main_shows}

    return render(request, 'axf/home/home.html', context=context)


def market(request, typeid, childcid, sort_rule):
    title = '闪送超市'
    # 查询所有类型
    foodtypes = FoodTypes.objects.all()
    # 查询所有商品

    if childcid == '0':
        goods_list = Goods.objects.filter(categoryid=typeid)
    else:
        goods_list = Goods.objects.filter(categoryid=typeid).filter(childcid=childcid)

    if sort_rule == '1':
        # 销量升序
        goods_list = goods_list.order_by('productnum')
    elif sort_rule == '2':
        # 销量降序
        goods_list = goods_list.order_by('-productnum')
    elif sort_rule == '3':
        # 价格最高
        goods_list = goods_list.order_by('-price')
    elif sort_rule == '4':
        # 价格最低
        goods_list = goods_list.order_by('price')
    else:
        pass

    # 根据typeid将childtypename获取
    foodtype = FoodTypes.objects.filter(typeid=typeid)
    childtypenames = '全部分类:0'
    if len(foodtype) > 0:
        childtypenames = foodtype.first().childtypenames

    childtypenamelist = childtypenames.split('#')

    print(childtypenamelist)

    childtypenamelisttran = []
    for item in childtypenamelist:
        itemtran = item.split(':')
        childtypenamelisttran.append(itemtran)

    print(childtypenamelisttran)

    sort_rule_list = [['综合排序', '0'], ['销量升序', '1'], ['销量降序', '2'], ['价格最低', '3'], ['价格最高', '4']]

    context = {
        'title': title,
        'foodtypes': foodtypes,
        'goods_list': goods_list,
        'list': childtypenamelisttran,
        'typeid': typeid,
        'childcid': childcid,
        'sort_rule_list': sort_rule_list
    }

    return render(request, 'axf/market/market.html', context=context)


def cart(request):
    # 判断是否登录
    username = request.session.get('username')
    if username == None:
        return redirect(reverse('axf:login'))

    user = User.objects.get(u_name=username)
    carts = Cart.objects.filter(c_user=user).filter(c_belong=False)

    context = {
        'carts': carts
    }
    return render(request, 'axf/cart/cart.html', context=context)


def mine(request):
    # 配置基本信息
    title = '我的'
    user_icon = ''
    username = request.session.get('username')

    if username == None:
        username = '未登录'
        is_login = False
        context = {
            'username': username,
            'title': title,
            'is_login': is_login
        }
    else:
        username = User.objects.filter(u_name=username).first().u_name
        user_icon = User.objects.filter(u_name=username).first().u_icon.url

        is_login = True

        context = {
            'title': title,
            'is_login': is_login,
            'username': username,
            'user_icon': 'http://127.0.0.1:8000/static/uploadfiles/' + user_icon
        }
    return render(request, 'axf/mine/mine.html', context=context)


def urlToMarket(request):
    return redirect(reverse('axf:market', args=['104749', '0', '0']))


def login(request):
    return render(request, 'axf/user/login.html')


def register(request):
    return render(request, 'axf/user/register.html')


def do_register(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        icon = request.FILES['icon']

        print(password)
        # 获取摘要
        md5 = hashlib.md5()
        # 将原数据传入进行摘要摘要运算  2进制才能转
        md5.update(password.encode('utf-8'))
        # 获取摘要后的信息 hex 16进制的输出
        p = md5.hexdigest()
        print(p)
        password = p

        user = User()
        user.u_name = username
        user.u_password = password
        user.u_email = email
        user.u_phone = phone
        user.u_icon = icon
        user.save()

        # 将用户关键信息
        request.session['username'] = username

        return redirect(reverse('axf:mine'))

    except Exception as e:
        print(e)
        return HttpResponse('注册失败')


def logout(request):
    del request.session['username']
    response = HttpResponseRedirect(reverse('axf:mine'))
    # response.delete_cookie('sessionid')
    return response


def check_user(request):
    uname = request.GET.get('uname')
    users = User.objects.filter(u_name=uname)
    if len(users) > 0:
        msg = "用户已存在"
        state = 201
    else:
        msg = '用户名可用'
        state = 200
    data = {'msg': msg, 'state': state}
    return JsonResponse(data)


def do_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 两种写法 第一种直接去数据库直接查询用户名密码
    # 先用用户名去找 找到 在验证密码
    user = User.objects.filter(u_name=username)
    if len(user) > 0:
        # 验证密码 将密码进行hash算法进行比较
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        newpassword = md5.hexdigest()
        if newpassword == user.first().u_password:
            # 登录成后 跳转回个人中心
            request.session['username'] = username
            response = HttpResponseRedirect(reverse('axf:mine'))
            return response
        else:
            return redirect(reverse('axf:login'))
    else:
        return redirect(reverse('axf:login'))


def user_info(request):
    username = request.session['username']
    user = User.objects.filter(u_name=username).first()
    u_name = user.u_name
    u_phone = user.u_phone
    u_email = user.u_email
    u_icon = user.u_icon.url

    context = {
        'u_name': u_name,
        'u_phone': u_phone,
        'u_email': u_email,
        'u_icon': 'http://127.0.0.1:8000/static/uploadfiles/' + u_icon
    }
    return render(request, 'axf/user/user_info.html', context=context)


def do_user_info(request):
    # 获取表单内容
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    icon = request.FILES['re_icon']

    # 实例化登录用户
    username = request.session['username']
    user = User.objects.filter(u_name=username).first()

    # 更改
    user.u_name = name
    user.u_email = email
    user.u_phone = phone
    user.u_icon = icon

    user.save()

    # 在session中存储新的username
    request.session.clear()
    request.session['username'] = name

    return redirect(reverse('axf:mine'))


def check_user_info(request):
    username = request.GET.get('username')
    user = User.objects.filter(u_name=username).first()

    if user == None:
        msg = '用户名可用'
        state = 200
    else:
        msg = '用户名不可用'
        state = 201

    data = {'msg': msg, 'state': state}

    return JsonResponse(data)


def add_to_cart(request):
    # 判断用户是否登录
    username =request.session.get('username')

    if username == None:
        return redirect(reverse('axf:login'))

    # 用户已登录
    goods_id = request.GET.get('goods_id')
    goods = Goods.objects.get(pk=goods_id)

    # 获取用户
    user = User.objects.get(u_name=username)

    c = Cart.objects.filter(c_user=user).filter(c_goods=goods).filter(c_belong=False)

    if len(c) == 0:
        # 存储购物信息
        c = Cart()
    else:
        c = c.first()
        c.c_goods_num += 1

    c.c_user = user
    c.c_goods = goods

    c.save()

    return JsonResponse({'msg': '添加成功'})


def change_select(request):
    cart_id = request.GET.get('cartid')
    cart_select = request.GET.get('cartselect')

    print(type(cart_id), cart_id)
    print(type(cart_select), cart_select)

    if cart_select == 'True':
        cart_select = False
    else:
        cart_select = True

    car = Cart.objects.get(pk=cart_id)
    car.c_select = cart_select

    car.save()

    return JsonResponse({'msg': 'ok'})


def cart_goods_sub(request):
    cartid = request.GET.get('cartid')
    car = Cart.objects.get(pk=cartid)
    num = car.c_goods_num
    if num == 1:
        car.delete()
    else:
        car.c_goods_num -= 1
        car.save()

    return JsonResponse({'num': num-1, 'msg': 'ok'})


def gen_order(request):
    cartids = request.GET.get('cartids')
    cartids = cartids.split('=')
    print(cartids)

    order = Order()
    username = request.session.get('username')
    user = User.objects.get(u_name=username)

    order.o_user = user
    order.o_status = 1
    order.save()

    # 修改商品属于哪张表
    for cartid in cartids:
        car = Cart.objects.get(pk=cartid)
        car.c_belong = True
        car.c_order = order
        car.save()

    return JsonResponse({'msg': 'ok', 'orderid': order.id})


def pay(request, orderid):

    context = {
        'orderid': orderid
    }
    return render(request, 'axf/order/pay.html', context=context)


def cart_goods_add(request):
    cartid = request.GET.get('cartid')

    car = Cart.objects.get(pk=cartid)
    car.c_goods_num += 1
    car.save()

    return JsonResponse({'msg': 'ok', 'num': car.c_goods_num})

