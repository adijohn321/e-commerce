
function modal_valid(modal) {
  modal.find('.required').each(function(e) {
    $(this).valid();
  });

};

var modal = document.getElementById("myModal");
var registerModal = document.getElementById("registerModal");

var btn = document.getElementById("myBtn");
var registerButton = document.getElementById("registerButton");

var span = document.getElementsByClassName("close")[0];
var span2 = document.getElementsByClassName("close")[1];

btn.onclick = function() {
  modal.style.display = "block";
}
registerButton.onclick = function() {
  registerModal.style.display = "block";
}

span.onclick = function() {
  modal.style.display = "none";
}

span2.onclick = function() {
  registerModal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
  if (event.target == registerModal) {
    registerModal.style.display = "none";
  }
}



let slideIndex = 1;
let slideIndexs = 0;
showSlide();

// Next/previous controls
function plusSlides(n) {
  showSlides()
  slideIndexs += (n-1)
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides()
  slideIndexs = n-1
}


setInterval(showSlide,5000)
function showSlide() {
  
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slideIndexs++;
  if (slideIndexs > slides.length) {slideIndexs = 1}    
  slides[slideIndexs-1].style.display = "block";  
  dots[slideIndexs-1].className += " active";
}





