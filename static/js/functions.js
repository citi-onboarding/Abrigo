function showMenu() {
    let x = document.querySelector('.menu');
    x.classList.toggle('change');
}


let caSlick = document.querySelector('.slick-infos');
let caModal = document.querySelector('.ca-banco-info');
let caBtn = document.querySelector('.ca-modal');

caBtn.onclick = function(){
    caSlick.style.display = "block";
}

window.addEventListener("click", function(event){
    console.log(event.target);
    if(event.target != caModal && event.target != caBtn && screen.width>1024 && event.target != caSlick){
        caSlick.style.display = "none";
    }
});