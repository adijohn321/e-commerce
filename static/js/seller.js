var addToStockModal = document.getElementById("addToCartModal");

var closeAddToCart = document.getElementsByClassName("closeAddToCart")[0];
var loader = document.getElementById('loader')

function openAddStock(x) {
    item_id = x;
    addToStockModal.style.display = "block";
    $('#informationDiv').html(loader)

    $.ajax({
        url: 'shop/item',
        data: {
            'item_id': item_id
        }, success: function (data) {
            $('#informationDiv').html(data.htmlStr)
        }, error: function (xhr, textStatus, error) {
            console.log(xhr.statusText);
            console.log(textStatus);
            console.log(error);
        }
    })

}
closeAddToCart.onclick = function () {
    addToStockModal.style.display = "none";
    $('#informationDiv').html('')
}

$(document).on('click', '#submitAddStock', function (e) {
    var url = $(this).attr("data-ajax-url")
    var item_id = $(this).attr("data-ajax-item-id")
    var quantity = $('#quantity').val()
    console.log(quantity)
    $.ajax({
        url: url,
        data: {
            'item_id': item_id,
            'quantity': quantity
        }, success: function (data) {
            addToStockModal.style.display = "none";
            openMessageModal(data.message)
            loadItems()
        }, error: function (xhr, textStatus, error) {
            console.log(xhr.statusText);
            console.log(textStatus);
            console.log(error);
        }
    })

})