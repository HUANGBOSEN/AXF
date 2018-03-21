$(function () {
    $('.ischose').click(function () {
       // 将当前点击选项的id发送给服务器
        var cart_id = $(this).attr('cartid');
        var cart_select = $(this).attr('cartselect');
        console.log(cart_id);
        console.log(cart_select);
        if (cart_select == 'True'){
            $(this).attr('cartselect','False');
        } else {
            $(this).attr('cartselect','True');
        }
        // $(this).attr('cartselect', !cart_select);
        var child = $(this).find('span');
       $.getJSON('/axf/changeselect', {'cartid': cart_id, 'cartselect': cart_select}, function (data) {
           if (data['msg'] == 'ok'){
                $(child).toggle();
           }
       })
    });

    $('.subShopping').click(function () {
    //    获取到点击项目的id
        var sub = $(this);
        var cartid = sub.attr('cartid');

        $.getJSON('/axf/cart_goods_sub', {'cartid':cartid}, function (data) {
            console.log(data['msg']);
            if(data['num'] == 0){
                sub.parents('li').remove();
            } else {
                sub.next('span').html(data['num']);
            }
        })
    });

    // 购物车+
    $('.addShopping').click(function () {
        var add = $(this);
        var cartid = add.attr('cartid');

        $.getJSON('/axf/cart_goods_add', {'cartid': cartid}, function (data) {
            console.log(data['msg']);
            add.prev('span').html(data['num']);
        })
    });





    $('#select_ok').click(function () {
        var spans = $(".ischose").find('span');

        var cartids = [];

        for (var i = 0; i<spans.length; i ++){
            if($(spans[i]).css('display') == 'block'){
                cartids.push($(spans[i]).attr('id'))
            }
        }

        console.log(cartids);

        $.getJSON('/axf/gen_order', {'cartids': cartids.join('=')}, function (data) {
            console.log(data['msg']);
            window.open('/axf/pay'+data['orderid'], '_self');
        })
    })



});
















