$(document).on('click', '#submmitReg', function (e) {

    var url = $("#registerDiv").attr("data-ajax-url");
    var registerModal = document.getElementById("registerModal");
    var first_name = $("#fName").val()
    var last_name = $("#lName").val()
    var email = $("#emailreg").val()
    var username = $("#usernamereg").val()
    var password = $("#passwordreg").val()

    $.ajax({
        url: url,
        data: {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'username': username,
            'password': password,
        }, success: function () {
            registerModal.style.display = "none";
            openMessageModal("Registration Was Successful.")
        },error: function(xhr, textStatus, error) {
            console.log(xhr.statusText);
            console.log(textStatus);
            console.log(error);
        }
    })


});