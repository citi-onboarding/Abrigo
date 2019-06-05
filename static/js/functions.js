let x = document.querySelector('.menu');
function showMenu() {
    x.classList.toggle('change');
}

function closeMenu(){
    x.classList.toggle('change');
}
let menuChoice = document.querySelector('.itens-menu')


let caModal = document.querySelector('.ca-banco-info');
let caBtn = document.querySelector('.ca-modal');
let caBtnText = document.querySelector('.ca-modal h2');
if(screen.width>1024){
    caModal.style.display = "none";
}

caBtnText.onclick = function(){
    caModal.style.display = "block";
}

caBtn.onclick = function(){
    caModal.style.display = "block";
}

window.addEventListener("click", function(event){
    if(event.target != caModal && event.target != caBtn && event.target != caBtnText && screen.width>1024){
        caModal.style.display = "none";
    }
});