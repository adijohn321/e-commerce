
var modal3 = document.getElementById("addToCartModal");


var closeAddToCart = document.getElementsByClassName("closeAddToCart")[0];
var loader = document.getElementById('loader')

function openAddToCart(x) {
    item_id = x;
    modal3.style.display = "block";
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
    modal3.style.display = "none";
    $('#informationDiv').html('')
}


window.onclick = function (event) {
    if (event.target == modal3) {
        modal3.style.display = "none";
        $('#informationDiv').html('')
    }
}
function addCartItem(n) {
    var url = $("").attr("data-ajax-url")
    var item_id = $("").attr("data-ajax-item-id")
    var quantity = $('#quantity').val()
    console.log(n)
}




$(document).on('click', '#submitAddToCart', function (e) {
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
            modal3.style.display = "none";
            openMessageModal(data.message)
        }, error: function (xhr, textStatus, error) {
            console.log(xhr.statusText);
            console.log(textStatus);
            console.log(error);
        }
    })

})


function searchItem(query) {

}

function viewCart() {

}


let items = new Array()

function calculateItem() {
    items = new Array()
    // Loop through each div element with the class box
    document.querySelector("#submitCheckOut").disabled = true
    var itemSelected = 0;
    var totalItem = 0;
    var totalAmount = 0;
    var itemAmount = 0;
    $(".selectedCheckOut").each(function () {
        
        var amount = parseFloat(this.querySelector(".price").textContent);
        var id = parseInt(this.querySelector(".item_id").textContent);
        var quantity = parseInt(this.querySelector(".quantityOut").value);
        this.querySelector("#total").textContent = "Total: $" + parseFloat(amount * quantity).toFixed(2)

        if (this.querySelector(".checkedOut").checked) {
            var amount = parseFloat(this.querySelector(".price").textContent);
            var id = parseInt(this.querySelector(".item_id").textContent);
            var quantity = parseInt(this.querySelector(".quantityOut").value);
            totalAmount += parseFloat(amount * quantity);
            totalItem += quantity;
            itemSelected++;
            document.querySelector("#submitCheckOut").disabled = false
            let item = {
                'id':id,
                'quantity':quantity
            }
            items.push(item)

        }
    })

    document.querySelector("#itemsSelected").textContent = "Item Selected: " + itemSelected
    document.querySelector("#totalItems").textContent = "Total Item: " + totalItem
    document.querySelector("#totalAmount").textContent = "Total Amount: $" + totalAmount.toFixed(2)
}

function placeOrder() {
    var url = $("#submitFormCheckOut").attr("data-ajax-url");
    var token = $("#token").attr("data-csrf-token");


    var formData = new FormData()

    

    
    formData.append('csrfmiddlewaretoken', token)
    items.forEach(function(item){
        formData.append('items', item.id);
        formData.append('quantities', item.quantity);
    })



    $.ajax({
        url: url,
        data: formData,
        method: 'post',
        processData: false,
        contentType: false,
        cache: false,
        success: function (data) {
          openMessageModal("Operation was successful.")
          myCart();
        },
        error: function(xhr, textStatus, error){
            console.log(xhr.statusText);
            console.log(textStatus);
            console.log(error);
        }
      });

    
}

