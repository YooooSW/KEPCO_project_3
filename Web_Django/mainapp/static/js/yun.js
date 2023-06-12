
function previewImage(event) {
  var reader = new FileReader();
  reader.onload = function () {
      var preview = document.getElementById('imagePreview');
      var img = document.createElement('img');
      img.src = reader.result;
      img.style.maxWidth = '300px';  // Adjust the maximum width as needed
      preview.innerHTML = '';
      preview.appendChild(img);
  };
  reader.readAsDataURL(event.target.files[0]);
}