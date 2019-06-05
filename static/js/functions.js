function showMenu() {
    let x = document.querySelector('.menu');
    x.classList.toggle('change');
}

let caModal = document.querySelector('.ca-banco-info');
let caBtn = document.querySelector('.ca-modal');

caBtn.onclick = function(){
    caModal.style.display = "block";
}

window.addEventListener("click", function(event){
    console.log(event.target);
    if(event.target != caModal && event.target != caBtn && screen.width>1024){
        caModal.style.display = "none";
    }
});