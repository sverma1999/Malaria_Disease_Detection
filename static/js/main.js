$(document).ready(function () {
    const imageUpload = $('#imageUpload');
    const uploadedImage = $('#uploadedImage');
    const predictButton = $('#predictButton');
    const predictionResult = $('#predictionResult');
    const resultText = $('#resultText');

    imageUpload.on('change', function () {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                uploadedImage.attr('src', e.target.result);
                uploadedImage.removeAttr('hidden');
            };
            reader.readAsDataURL(file);
            predictButton.removeAttr('disabled');
        }
    });

    predictButton.on('click', function () {
        const file = imageUpload[0].files[0];
        if (!file) {
            return;
        }
        const formData = new FormData();
        formData.append('file', file);

        predictButton.attr('disabled', 'disabled');
        predictButton.text('Predicting...');

        // $.ajax({
        //     type: 'POST',
        //     url: '/predict',
        //     data: formData,
        //     contentType: false,
        //     cache: false,
        //     processData: false,
        //     success: function (data) {
        //         resultText.text(data);
        //         predictionResult.removeAttr('hidden');
        //         predictButton.removeAttr('disabled');
        //         predictButton.text('Predict');
        //     },
        //     error: function () {
        //         alert('Error occurred while making the prediction. Please try again.');
        //         predictButton.removeAttr('disabled');
        //         predictButton.text('Predict');
        //     }
        // });
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: formData,
            contentType: false,
            cache: false,
            processData: false,
            beforeSend: function (xhr) {
                xhr.setRequestHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
                xhr.setRequestHeader('Pragma', 'no-cache');
                xhr.setRequestHeader('Expires', '0');
            },
            success: function (data) {
                resultText.text(data);
                predictionResult.removeAttr('hidden');
                predictButton.removeAttr('disabled');
                predictButton.text('Predict');
            },
            error: function () {
                alert('Error occurred while making the prediction. Please try again.');
                predictButton.removeAttr('disabled');
                predictButton.text('Predict');
            }
        });
    });
});
