
$(function () {
    // 加载完成 延迟开启轮播 轮播是在js初始化完成之后进行的轮播
    setTimeout(function () {
        // 轮播开启
        topSwiper();
        swiperMenu();
    },1000);
});

function topSwiper() {
    var topSwiper = new Swiper('#topSwiper',{
        loop: true,
        autoplay: 4000,
        pagination: '.swiper-pagination'
    });
}

function swiperMenu() {
    var swiperMenu = new Swiper('#swiperMenu',{
        slidesPerView:3
    });
}














