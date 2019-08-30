let base_endpoint = "http://127.0.0.1:8000";

function ajaxPromise(endpoint, data){
  let promise = new Promise((resolve, reject) => {
    let xhr = new XMLHttpRequest();
    xhr.open('POST',endpoint , true);
    xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
    xhr.onreadystatechange = () => {
      if(xhr.readyState == xhr.DONE){
        if(xhr.status == 200){
          if(xhr.getResponseHeader('Content-Type') == 'application/json'){
            resolve(JSON.parse(xhr.response));
          }
          else{
            resolve(xhr.response);
          }
        }
        else{
          reject(xhr.response);
        }
      }
    }
    xhr.send(data);
  });
  return promise;
}

function getCookie(name){
  let cookies = document.cookie.split(';');
  var value = '';
  cookies.forEach((e)=>{
    e = e.trim();
    if(e.startsWith(name)){ value = e.substring(name.length+1); }
  });
  return value;
}

function showPopup(popupEl){
  popupEl.classList.add('active');
}
function unPopup(popupEl){
  popupEl.classList.remove('active');
}
