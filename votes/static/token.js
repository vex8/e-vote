let tokenInput = document.querySelector('#token');
let nimInput = document.querySelector('#nim');
let submit = document.querySelector('#submit');
let popup = document.querySelector('.popup-container');
let popupTitle = document.querySelector('#popup-title');
let popupContent = document.querySelector('#popup-content');

submit.addEventListener('click', ()=>{
  let token = sanitize(tokenInput.value);
  let nim = nimInput.value;
  if(token.length < 4){
    showPopupContent(
      'Error!',
      'Token should be exactly 4 alphanumeric characters.');
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
        showPopupContent('Error!', data['return']);
      }
      else if(data['code']==4){ // our code 4 means OK, proceed
        showPopupContent('Success!', data['return']);
        window.setTimeout(()=>{
          window.location.href = '/vote';
        }, 1000);
      }
    }).catch((error) => {
      showPopupContent('Error!', error);
    });
});

function showPopupContent(title, content){
  popupTitle.innerText = title;
  popupContent.innerHTML = content;
  showPopup(popup);
}
popup.addEventListener('click', ()=>{
  unPopup(popup);
});

function sanitize(text){
  return text.replace(/[^a-zA-Z0-9]/g, '');
}