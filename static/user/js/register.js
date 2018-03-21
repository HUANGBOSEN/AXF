$(function () {
    console.log('进入js');
    $('#register_username').blur(function () {
    //    失去焦点获取输入框中的内容 需要将输入内容发送服务器验证
        var uname = $(this).val();
        // 向服务器发送用户名 进行验证
        // $.getJSON(url, json数据, 回调函数)
        $.getJSON('http://127.0.0.1:8000/axf/check_user',{'uname':uname},function (data) {
            if(data['state'] == 200){
                $('#user_name_check').css('color', '#00ff00');
            } else if (data['state'] == 201){
                $('#user_name_check').css('color', '#ff0000');
            }
            console.log(data['state'] == 200);
            $('#user_name_check').html(data['msg'])
        })
    })
});


function check() {
    // 在这做提交前的验证
    var pwd = $('#register_password').val();
    var pwd2 = $('#register_password_confirm').val();
    if (pwd == pwd2){
        $('#password_check').html('两次密码一致');
        $('#password_check').css('color','#00ff00');
    }else {
        $('#password_check').html('两次密码不一致');
        $('#password_check').css('color','#ff0000');
        return false;
    }

    var newPwd = md5(pwd);
    $('#register_password').val(newPwd);
    console.log(newPwd);
    console.log($('#register_password').val());

    return true;


}







