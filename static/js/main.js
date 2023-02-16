var messageModal = document.getElementById("messageModal");
var closeMessage = document.getElementById("closeMessage");

closeMessage.onclick = function () {
    messageModal.style.display = "none";
}
function openMessageModal(message){
    messageModal.style.display = "block";
    document.getElementById("message").textContent = message
}
var messageModalPrompt = document.getElementById("messageModalPrompt");
var closeMessagePrompt = document.getElementById("closeMessagePrompt");
var proceed = document.getElementById("promptProceed");

closeMessagePrompt.onclick = function () {
    messageModalPrompt.style.display = "none";
}
function openMessageModalPrompt(message, link, id){
    deleteLink = link
    deleteId = id
    messageModalPrompt.style.display = "block";
    document.getElementById("messagePrompt").textContent = message
}

var deleteId
var deleteLink

var proceed = document.getElementById("promptProceed");
proceed.onclick = function () {
    messageModalPrompt.style.display = "none";
    var token = $("#token").attr("data-csrf-token");
    var formData = new FormData()
    formData.append('id',deleteId)
    formData.append('csrfmiddlewaretoken', token)

    $.ajax({
        url: deleteLink,
        data: formData,
        type: 'post',
        success:function(data){
            openMessageModal(data.message)
        },error:function(data){

        },
        cache: false,
        contentType: false,
        processData: false
    })
}



function myCart(){
    $.ajax({
        url: 'cart/items',
        success: function(data){
            $("#body").html(data.htmlStr)
            setInterval(showSlide, 9999999999)
        },error: function(xhr, textStatus, error){

        }
    })
}

function viewAllAds(){
    $.ajax({
        url: 'shop/edit-ads',
        success: function(data){
            $("#body").html(data.htmlStr)
            setInterval(showSlide, 9999999999)
            editAds(data.item_id)
        },error: function(xhr, textStatus, error){

        }
    })
}

function viewAllItems(){
    $.ajax({
        url: 'shop/edit-items',
        success: function(data){
            $("#body").html(data.htmlStr)
            clearInterval(showSlide)
        },error: function(xhr, textStatus, error){

        }
    })
}
function viewOrders(status){

    $.ajax({
        url: 'orders/get-orders',
        data:{'status':status,},
        success: function(data){
            $("#body").html(data.htmlStr)
            document.getElementById('xx').value = status
            clearInterval(showSlide)
        },error: function(xhr, textStatus, error){

        }
    })
}
get_badge_counts()
// get notification every 5 seconds
setInterval(get_badge_counts, 5000)

function get_badge_counts(){
    $.ajax({
        url: 'logs/get-notification',
        success: function(data){
            document.getElementById('notificationBadge').textContent = data.notifications
        },error: function(xhr, textStatus, error){

        }
    })
}
function get_notifications(){
    $.ajax({
        url: 'logs/get-notifications',
        success: function(data){
            $('#notificationView').html( data.htmlStr)
        },error: function(xhr, textStatus, error){

        }
    })
}

function mark_all_as_read(){
    $.ajax({
        url: 'logs/mark-all',
        success: function(data){
            get_notifications()
            openMessageModal(data.message)
            closeNotification()
        },error: function(xhr, textStatus, error){

        }
    })
}

function openNotification() {
    document.getElementById("mySidenav").style.width = "400px";
    get_notifications()
    
  }
  
  function closeNotification() {
    document.getElementById("mySidenav").style.width = "0";
    // document.getElementById("main").style.marginLeft= "0";
  }