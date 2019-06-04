$(document).ready(function(){
    $('.carrossel-arrec').slick({
        dots: true,
        infinite: false,
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