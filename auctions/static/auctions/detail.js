const current = document.querySelector('#current');
const imgs = document.querySelectorAll('.imgs img');
const opacity = 0.4;
const original = document.querySelector(".full-img");

// Set first img opacity
imgs[0].style.opacity = opacity

imgs.forEach(img => img.addEventListener('click', imgClick))

function imgClick(e) {
  // Reset the opacity
  imgs.forEach(img => (img.style.opacity = 1))

  // Change current image to src of clicked image
  current.src = e.target.src;
  original.src = e.target.src;

  // Add fade in class
  current.classList.add('fade-in')

  // Remove fade-in class after .5 sec
  setTimeout(() => current.classList.remove('fade-in'),
    500);

  //Change the opacity to opacity var
  e.target.style.opacity = opacity;
}


// Display modal image
const modal = document.querySelector(".modal");
const mainImg = document.querySelector(".main-image")


mainImg.addEventListener("click", (e) => {
  modal.classList.add("open");
  original.src = e.target.src
  original.classList.add("open");

});



modal.addEventListener("click", (e) => {
  if (e.target.classList.contains("modal")) {
    modal.classList.remove("open");
    original.classList.remove("open");
  }
});