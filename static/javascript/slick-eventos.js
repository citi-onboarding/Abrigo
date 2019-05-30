$(document).ready(function(){
    $('.carrossel-eventos').slick({
        dots: true,
        infinite: true,
        speed: 500,
        arrows: false,
        centerMode: true,
        variableWidth: true,
        arrows:true,
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