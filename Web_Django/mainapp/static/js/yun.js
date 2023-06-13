// 이미지 미리보기
function previewImage(event) {
  var reader = new FileReader();
  reader.onload = function () {
      var preview = document.getElementById('imagePreview');
      var img = document.createElement('img');
      img.src = reader.result;
      //img.style.maxWidth = '300px';  // Adjust the maximum width as needed
      preview.innerHTML = '';
      preview.appendChild(img);
  };
  reader.readAsDataURL(event.target.files[0]);
}

// function changeLoadView(url){
//   $("#car_data").load("/" + url);
// }


function uploadImage() {
  var form = document.getElementById('imageForm');
  var formData = new FormData(form);

  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
              var response = xhr.responseText;
              document.getElementById('car_data').innerHTML = response;
          } else {
              console.error("Error: " + xhr.status);
          }
      }
  };

  xhr.open("POST", "/car_repair_price/");
  xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
  xhr.send(formData);
}
