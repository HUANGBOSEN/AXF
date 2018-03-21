$(function () {
    // 类型选择 排序规则
    $('#all_type').click(function () {
        // alert("全部类型")
        $('#all_type_content').css('display','block').click(function () {
            $(this).css('display','none');
        })
    });
    $('#sort_rule').click(function () {
        $('#sort_rule_content').css('display','block').click(function () {
            $(this).css('display','none');
        })
    });

//    商品+
    $('.goods_add').click(function () {
        var goods_id = $(this).attr('goods_id');

        // 写地址的时候 浏览器上写的是ip就写ip 使用的域名就写域名
        $.getJSON('/axf/addtocart', {'goods_id':goods_id}, function (data) {
            alert(data['msg']);
        })

    })









});









