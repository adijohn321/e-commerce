loadItemOwner()
function loadItemOwner() {
  var url = $('#itemsContainer').attr("data-ajax-url")

  $.ajax({
    url: url,
    success: function (data) {

      $('.itemsContainer').html(data.htmlStr)
      editItem(data.item_id)

    },
    error: function (xhr, textStatus, error) {
      console.log(xhr.statusText);
      console.log(textStatus);
      console.log(error);
    }
  });

}
function loadItemOwnerReload() {
  var url = $('#itemsContainer').attr("data-ajax-url")

  $.ajax({
    url: url,
    success: function (data) {

      $('.itemsContainer').html(data.htmlStr)

    },
    error: function (xhr, textStatus, error) {
      console.log(xhr.statusText);
      console.log(textStatus);
      console.log(error);
    }
  });

}

function loadItemOwnerSearch() {
  var url = $('#itemsContainer').attr("data-ajax-url")
  input = $('#searchItems').val()
  console.log(input)

  $.ajax({
    url: url,
    data: {'search':input},
    success: function (data) {

      $('.itemsContainer').html(data.htmlStr)

    },
    error: function (xhr, textStatus, error) {
      console.log(xhr.statusText);
      console.log(textStatus);
      console.log(error);
    }
  });

}
function editItem(id) {
  _id = parseInt(id)
  update_item_id = parseInt(id)
  url = $('#itemsContainer').attr("data-ajax-url-edit")
  console.log("0")
  $.ajax({
    url: url,
    data: {
      'item_id': _id
    }, success: function (data) {
      $('.rightDiv').html(data.htmlStr)
    }, error: function () {

    }
  })
}

var update_item_id

$(document).on('submit', '#formEditItem', function (e) {
  e.preventDefault()

  var formData = new FormData(this)
  var token = $("#token").attr("data-csrf-token");
  var url = $(this).attr("data-ajax-url");
  console.log(url)

  formData.append('csrfmiddlewaretoken', token)
  formData.append('item_id', update_item_id)

  $.ajax({
    url: url,
    type: 'post',
    data: formData
    , success: function (data) {
      openMessageModal(data.message)
      loadItemOwnerReload()
      editItem(update_item_id)
    }, error: function () {

    },
    cache: false,
    contentType: false,
    processData: false
  })

})

$(document).on('click', '#deleteItem', function(e){
  
  var url = $(this).attr("data-ajax-url");
  openMessageModalPrompt('Proceed with CAUTION.\n Deleting this Item may affect other data.',url,update_item_id)
})