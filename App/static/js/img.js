document.getElementById('image_input').addEventListener('change', function(event){
    var input = event.target;
    var file = input.files[0];

    if (file) {
        var reader = new FileReader();
        reader.onload = function(e) {
            var preview = document.getElementById('imagePreview');
            var uploadButton = document.getElementById('uploadIcon');

            preview.src = e.target.result;
            preview.style.display = 'flex';
            uploadButton.style.display = 'none';
        }
        reader.readAsDataURL(file)
    } else {
        console.log('No File Selected');
    }
    
});

document.getElementById('imagePreview').addEventListener('click', function(){
    document.getElementById('image_input').click();
});

document.addEventListener('DOMContentLoaded', function() {
    var toggles = document.querySelectorAll('.recipe_toggle');
    toggles.forEach(function(button){
        button.addEventListener('click', function(event) {
            var content = this.nextElementSibling;
            if (content.style.display === "none") {
                content.style.display = "block";
            } else {
                content.style.display = "none";
            }
        });
    });
});
