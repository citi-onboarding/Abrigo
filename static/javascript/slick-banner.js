$(document).ready(function(){
    $('.carrossel-banner').slick({
        dots: true,
        infinite: true,
        speed: 500,
        fade: true,
        arrows: true,
        swipe: true,
        responsive: [
            {
                breakpoint: 1200,
                settings:{
                    arrows:false
                } 
            }
        ]
    });
});