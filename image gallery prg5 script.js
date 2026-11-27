let images = document.querySelectorAll(".gallery img");
let current = 0;

function showImage(index) {
    images.forEach(img => img.style.display = "none");
    images[index].style.display = "block";
}

function nextImage() {
    current = (current + 1) % images.length;
    showImage(current);
}

function previousImage() {
    current = (current - 1 + images.length) % images.length;
    showImage(current);
}

images.forEach(img => img.style.display = "block");
