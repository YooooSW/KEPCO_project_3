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


// my_page
        var content1 = document.getElementById("content1");
        var content2 = document.getElementById("content2");
        // var content3 = document.getElementById("content3");
        var btn1 = document.getElementById("btn1");
        var btn2 = document.getElementById("btn2");
        // var btn3 = document.getElementById("btn3");

        function openHTML(){
            content1.style.transform = "translateX(0)";
            content2.style.transform = "translateX(100%)";
            // content3.style.transform = "translateX(100%)";
            btn1.style.color = "#CF4D9D";
            btn2.style.color = "#000";
            // btn3.style.color = "#000";
            content1.style.transitionDelay = "0.3s"
            content2.style.transitionDelay = "0s"
            // content3.style.transitionDelay = "0s"
        }
        function openCSS(){
            content1.style.transform = "translateX(100%)";
            content2.style.transform = "translateX(0)";
            //content3.style.transform = "translateX(100%)";
            btn1.style.color = "#000";
            btn2.style.color = "#CF4D9D";
            // btn3.style.color = "#000";
            content1.style.transitionDelay = "0s"
            content2.style.transitionDelay = "0.3s"
            //content3.style.transitionDelay = "0s"
        }
        // function openJAVASCRIPT(){
        //     content1.style.transform = "translateX(100%)";
        //     content2.style.transform = "translateX(100%)";
        //     content3.style.transform = "translateX(0)";
        //     btn1.style.color = "#000";
        //     btn2.style.color = "#000";
        //     btn3.style.color = "#ff7846";
        //     content1.style.transitionDelay = "0s"
        //     content2.style.transitionDelay = "0s"
        //     content3.style.transitionDelay = "0.3s"
        // }