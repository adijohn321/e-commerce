var update_ad_id
function editAds(id) {
  _id = parseInt(id)
  update_ad_id = parseInt(id)
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

$(document).on('submit', '#formEditAd', function (e) {
  e.preventDefault()

  var formData = new FormData(this)
  var token = $("#token").attr("data-csrf-token");
  var url = $(this).attr("data-ajax-url");
  console.log(url)

  formData.append('csrfmiddlewaretoken', token)
  formData.append('item_id', update_ad_id)

  $.ajax({
    url: url,
    type: 'post',
    data: formData
    , success: function (data) {
      openMessageModal(data.message)
      editAds(update_ad_id)
    }, error: function () {

    },
    cache: false,
    contentType: false,
    processData: false
  })

})


$(document).on('click', '#deleteAd', function(e){

  var url = $(this).attr("data-ajax-url");
  openMessageModalPrompt('Are you sure to delete  this Ad Campaign? This proccess is irreversible proceed with CAUTION.',url, update_ad_id)
})