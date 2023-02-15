$(document).on('click', '#saveAds', function (e) {

    var url = $("#myModal1").attr("data-ajax-url");
    var registerModal = document.getElementById("myModal1");
    var ads_name = $("#ads_name").val()
    var ads_description = $("#ads_description").val()
    var ads_image = $("#ads_image")[0].files[0] 

    $.ajax({
        url: url,
        data: {
            'ads_name': ads_name,
            'ads_description': ads_description,
            'ads_image': ads_image,
        }, success: function () {
            registerModal.style.display = "none";
            loadAds()
        },error: function(xhr, textStatus, error) {
            console.log(xhr.statusText);
            console.log(textStatus);
            console.log(error);
        }
    })


});
$('body').on('submit','#upload-file',function(e){
    e.preventDefault()
    var formData = new FormData(this);
    
    var registerModal = document.getElementById("myModal1");
    var ads_name = $("#ads_name").val()
    var ads_description = $("#ads_description").val()
    
    var url = $("#myModal1").attr("data-ajax-url");
    formData.append('ads_name',ads_name)
    formData.append('ads_description',ads_description)
    $.ajax({
          url:url,
          type: 'POST',
          data: formData,
          success: function (response) {
            registerModal.style.display = "none";
            loadAds()
            openMessageModal("Successfully Created Ads Campaign.")
          },
          error: function (response) {
          },
         cache: false,
         contentType: false,
         processData: false
    });
});

$('body').on('submit','#upload-Item',function(e){
    e.preventDefault()
    
    var formData = new FormData(this);
    var registerModal = document.getElementById("myModal");
    var url = $("#myModal").attr("data-ajax-url");

    var itemName = $("#itemName").val()
    var description = $("#description").val()
    var price = $("#price").val()

    formData.append('name',itemName)
    formData.append('description',description)
    formData.append('price',price)
    $.ajax({
        url:url,
        type: 'POST',
        data: formData,
        success: function (response) {
          registerModal.style.display = "none";
          loadItems()
          openMessageModal("Successfully Created Item "+itemName+".")
        },
        error: function (response) {
        },
       cache: false,
       contentType: false,
       processData: false
  });

});

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

$("#imgInp").change(function(){
    readURL(this);
});
function readURL1(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#preview1').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

$("#imgInput").change(function(){
    readURL1(this);
});
