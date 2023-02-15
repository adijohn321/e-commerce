function approve(order_number,status) {
    var formData = new FormData()
    var token = $("#token").attr("data-csrf-token");
    var url = $("#orderUrl").attr("data-ajax-url");
    formData.append('csrfmiddlewaretoken', token)
    formData.append('order_number', order_number)
    formData.append('status', status)
    $.ajax({
        url: url,
        type: 'post',
        data: formData
        , success: function (data) {
            openMessageModal(data.message)
            viewOrders('pending')
        }, error: function () {

        },
        cache: false,
        contentType: false,
        processData: false
    })

}