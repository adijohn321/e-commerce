var modal = document.getElementById("myModal");
var modal1 = document.getElementById("myModal1");


var span = document.getElementsByClassName("close")[0];
var span1 = document.getElementsByClassName("close")[1];



$(document).on('click', '#myBtn', function (e) {
  
  modal.style.display = "block";
})
$(document).on('click', '#createAdsBtn', function (e) {
  
  modal1.style.display = "block";
})


span.onclick = function() {
  modal.style.display = "none";
}
span1.onclick = function() {
  modal1.style.display = "none";
}


window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
  if (event.target == modal1) {
    modal1.style.display = "none";
  }
}

// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the navbar
var navbar = document.getElementById("navbar");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}

var slideIndex = 1;

// Next/previous controls
function plusSlides(n) {
  // slideIndexs += n
  // showSlides(slideIndexs)
}

// Thumbnail image controls
function currentSlide(n) {
  // slideIndexs = n
  // showSlides(n)
}

// function showSlides(n) {
//   let i;
//   let slides = document.getElementsByClassName("mySlides");
//   let dots = document.getElementsByClassName("dot");
//   for (i = 0; i < slides.length; i++) {
//     slides[i].style.display = "none";  
//   }
//   if (slideIndexs > slides.length) {slideIndexs = 1}    
//   for (i = 0; i < dots.length; i++) {
//     dots[i].className = dots[i].className.replace(" active", "");
//   }
//   slides[slideIndexs-1].style.display = "block";  
//   dots[slideIndexs-1].className += " active";
// }

