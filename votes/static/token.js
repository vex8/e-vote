let tokenInput = document.querySelector('#token');
let nimInput = document.querySelector('#nim');
let submit = document.querySelector('#submit');
let popup = document.querySelector('.popup-container');

submit.addEventListener('click', send);
tokenInput.addEventListener('keydown', (e)=>{
  if(e.keyCode == 13){
    e.preventDefault();
    send();
  }
});
function send(){
  let token = sanitize(tokenInput.value);
  let nim = nimInput.value;
  if(token.length < 4){
    showPopupContent(
      popup,
      'Error!',
      'Token should be exactly 4 alphanumeric characters.'
    );
    return;
  }
  if(isNaN(parseInt(nim))){
    showPopupContent(
      popup,
      'Error!',
      'NIM should be only number'
    );
    return;
  }
  ajaxPromise('/checktoken', JSON.stringify(
    {
      "token": token,
      "nim": nim  
    }
    ))
    .then((data)=>{
      if(data['code'] == 1){ // our code 1 means error, show popup
        showPopupContent(popup, 'Error!', data['return']);
      }
      else if(data['code']==4){ // our code 4 means OK, proceed
        showPopupContent(popup, 'Success!', data['return']);
        window.location.href = '/vote';
      }
    }).catch((error) => {
      showPopupContent(popup, 'Error!', error);
    });
}

popup.addEventListener('click', ()=>{
  unPopup(popup);
});

function sanitize(text){
  return text.replace(/[^a-zA-Z0-9]/g, '');
}