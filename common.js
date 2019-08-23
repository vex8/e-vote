function ajaxPromise(endpoint, data){
  let promise = new Promise((resolve, reject) => {
    let xhr = new XMLHttpRequest();
    xhr.open('POST',endpoint , true);
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
