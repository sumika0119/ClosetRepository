function previewImage() {
    console.log('previewImage function called');
    var input = document.getElementById('image');
    var previewContainer = document.getElementById('image-preview-container');
    var existingImage = document.querySelector('.clothe-image');

    // 既存の画像が存在する場合、削除
    if (existingImage) {
        existingImage.remove();
    }

    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            // 新しい画像を表示
            var previewImage = document.createElement('img');
            previewImage.src = e.target.result;
            previewImage.alt = 'Preview Image';
            previewImage.classList.add('clothe-image');
            previewImage.style.width = '500px';
            previewImage.style.margin = '0 auto';
            previewImage.style.height = 'auto';

            // 新しい画像を追加
            previewContainer.innerHTML = '';
            previewContainer.appendChild(previewImage);
        };
        reader.readAsDataURL(input.files[0]);
    }
}




function submitSortForm() {
    document.getElementById("sortForm").submit();
}
