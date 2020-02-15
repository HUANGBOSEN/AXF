from django.db import models


# Create your models here.
# 首页轮播1
class Wheel(models.Model):
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)
    img = models.CharField(max_length=210)

    class Meta:
        db_table = 'axf_wheel'


# 首页导航
class Nav(models.Model):
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)
    img = models.CharField(max_length=200)

    class Meta:
        db_table = 'axf_nav'


# 第二个轮播
class MustBuy(models.Model):
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)
    img = models.CharField(max_length=200)

    class Meta:
        db_table = 'axf_mustbuy'


# 便利商店
class Shop(models.Model):
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)
    img = models.CharField(max_length=200)

    class Meta:
        db_table = 'axf_shop'


# trackid,name,img,categoryid,
# brandname,img1,childcid1,productid1,
# longname1,price1,marketprice1,img2,
# childcid2,productid2,longname2,price2,
# marketprice2,img3,childcid3,productid3,
# longname3,price3,marketprice3)

# 主页面的现实区域
class MainShow(models.Model):
    trackid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    categoryid = models.CharField(max_length=20)
    brandname = models.CharField(max_length=100)
    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=20)
    productid1 = models.CharField(max_length=20)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=20)
    marketprice1 = models.CharField(max_length=20)
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=20)
    productid2 = models.CharField(max_length=20)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=20)
    marketprice2 = models.CharField(max_length=20)
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=20)
    productid3 = models.CharField(max_length=20)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=20)
    marketprice3 = models.CharField(max_length=20)

    class Meta:
        db_table = 'axf_mainshow'

# 闪送模块

# 商品信息
# (productid,productimg,productname,
#  productlongname,isxf,pmdesc,specifics,
#  price,marketprice,categoryid,childcid,
#  childcidname,dealerid,storenums,productnum)
# 商品类型
# (typeid,typename,childtypenames,typesort)


class FoodTypes(models.Model):
    typeid = models.CharField(max_length=20)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_foodtypes'


class Goods(models.Model):
    productid = models.CharField(max_length=20)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=200)
    isxf = models.BooleanField(default=False)
    pmdesc = models.IntegerField(default=0)
    specifics = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    marketprice = models.CharField(max_length=20)
    categoryid = models.CharField(max_length=20)
    childcid = models.CharField(max_length=20)
    childcidname = models.CharField(max_length=100)
    dealerid = models.CharField(max_length=20)
    storenums = models.CharField(max_length=20)
    productnum = models.CharField(max_length=20)

    class Meta:
        db_table = 'axf_goods'


# 创建用户模型
class User(models.Model):
    # 用户名 密码 头像 邮箱 电话
    u_name = models.CharField(max_length=16, unique=True)
    u_password = models.CharField(max_length=33)  # md5 32
    u_icon = models.ImageField(upload_to='icons')
    u_email = models.CharField(max_length=50)
    u_phone = models.CharField(max_length=20)

    class Meta:
        db_table = 'axf_user'


class Order(models.Model):
    o_user = models.ForeignKey('User')
    # 订单状态
    o_status = models.IntegerField(default=0)


class Cart(models.Model):
    # 一条购物车数据对应一个用户 一个用户对应多个购物车
    c_user = models.ForeignKey('User')
    # 一条购物车数据对应一个商品
    c_goods = models.ForeignKey('Goods')
    # 商品数量
    c_goods_num = models.IntegerField(default=1)
    # 关联订单表
    c_order = models.ForeignKey('Order', null=True, default=None)
    # 此数据是否选中
    c_select = models.BooleanField(default=True)
    # 划分 此数据属于订单展示 还是购物车展示 False表示属于购物车 True属于订单
    c_belong = models.BooleanField(default=False)





















