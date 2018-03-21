$(function () {
    $('#username').blur(function () {
        var username = $('#username').val();
        $.getJSON('http://127.0.0.1:8000/axf/check_user_info', {'username':username}, function (data) {
            if (data['state'] == 200){
                $('#is_username').html(data['msg']);
                $('#is_username').css('color','#00ff00');
            } else {
                $('#is_username').html(data['msg']);
                $('#is_username').css('color','#ff0000');
            }
        })
    })
});



function check() {
    var phone = $('#user_phone').val();
    if (phone.length < 6){
        return false;
    }
}










