const modal = document.getElementById('modal-arrec');
const botaoModal = document.getElementById('botaomodal-arrec');

botaoModal.addEventListener('click', openModal);
window.addEventListener('click', clickOutside);

function openModal(){
    modal.style.display = 'block';
}

function clickOutside(e){
    if(e.target != modal && e.target != botaoModal){
        modal.style.display = 'none';
    }
}
