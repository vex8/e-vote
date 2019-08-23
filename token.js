let tokenInput = document.querySelector('#token');
let submit = document.querySelector('#submit');
let popup = document.querySelector('#popup-container');
let popupTitle = document.querySelector('#popup-title');
let popupContent = document.querySelector('#popup-content');

submit.addEventListener('click', ()=>{
  let token = sanitize(tokenInput.value);
  if(token.length < 4){
    showPopup(
      'Error!',
      'Token should be exactly 4 alphanumeric characters.');
    return;
  }
  ajaxPromise('http://127.0.0.1:5000/checktoken', JSON.stringify({"token": token}))
    .then((data)=>{
      if(data['code'] == 1){ // our code 1 means error, show popup
        showPopup('Error!', data['return']);
      }
      else if(data['code']==4){ // our code 4 means OK, proceed
        showPopup('Success!', data['return']);
      }
    }).catch((error) => {
      showPopup('Error!', error);
    });
});

function showPopup(title, content){
  popupTitle.innerText = title;
  popupContent.innerHTML = content;
  popup.classList.add('active');
}
popup.addEventListener('click', ()=>{
  popup.classList.remove('active');
});

function sanitize(text){
  return text.replace(/[^a-zA-Z0-9]/g, '');
}