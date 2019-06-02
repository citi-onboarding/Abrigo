$(document).ready(function(){
    $('.slick-contas').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: true,
        fade: true,
        asNavFor: '.slick-infos',
        responsive: [
            {
                breakpoint: 1024,
                setting: {
                    
                }
            }
        ]
    });
});

$(document).ready(function(){
    $('.slick-infos').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        asNavFor: '.slick-contas',
        arrows: false,
        fade: true,
    });
});

