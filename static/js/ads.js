
loadItems()
loadAds()
setInterval(showSlide,3000)
function loadAds() {
  var user_id = $('#adsDiv').attr("data-ajax-user-id")
  var url = $('#adsDiv').attr("data-ajax-url")

  $.ajax({
    url: url,
    data: {
      'user_id': user_id,
    },
    success: function (data) {
      $('#adsDiv').html(data.htmlStr)
      showSlide();
    },
    error: function (xhr, textStatus, error) {
      console.log(xhr.statusText);
      console.log(textStatus);
      console.log(error);
    }
  });
}
function loadItems(){
  var user_id = $('#adsDiv').attr("data-ajax-user-id")
  var url = $('#cardContainer').attr("data-ajax-url")

  $.ajax({
    url: url,
    data: {
      'user_id': user_id,
    },
    success: function (data) {

      $('#cardContainer').html(data.htmlStr)
    },
    error: function (xhr, textStatus, error) {
      console.log(xhr.statusText);
      console.log(textStatus);
      console.log(error);
    }
  });

}

var slideIndexs = 0;

function showSlide() {
  
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndexs++;
  if (slideIndexs > slides.length) {slideIndexs = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndexs-1].style.display = "block";  
  dots[slideIndexs-1].className += " active";
}
