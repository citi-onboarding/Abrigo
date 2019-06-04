var modal = document.getElementById('modal-arrec');
var botaoModal = document.getElementById('botaomodal-arrec');

botaoModal.addEventListener('click', openModal);
window.addEventListener('click', clickOutside);

function openModal(){
    modal.style.display = 'block';
    console.log(123)
}

function clickOutside(e){
    console.log(456)
    if(e.target == modal){
        console.log(789)
        modal.style.display = 'none';
    }
}
