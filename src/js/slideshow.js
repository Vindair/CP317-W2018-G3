let img_index = 1;
show_image(img_index);

// Next/previous controls
function inc_image(n) {
  show_image(img_index += n);
}

// Thumbnail image controls
function cur_image(n) {
  show_image(img_index = n);
}

function show_image(n) {
  let i;
  let images = document.getElementsByClassName("images");
  let dots = document.getElementsByClassName("dot");
  if (n > images.length) {img_index = 1}
  if (n < 1) {img_index = images.length}
  for (i = 0; i < images.length; i++) {
    images[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  images[img_index-1].style.display = "block";
  dots[img_index-1].className += " active";
}
