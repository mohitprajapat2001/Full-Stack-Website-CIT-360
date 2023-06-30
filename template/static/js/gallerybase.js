const galleryImgs = document.querySelectorAll('.gallery-img');
const modalImg = document.getElementById('modalImg');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

let currentIndex = 0;

galleryImgs.forEach(function(img, index) {
  img.addEventListener('click', function() {
    currentIndex = index;
    showImage();
    const myModal = new bootstrap.Modal(document.getElementById('myModal'));
    myModal.show();
  });
});

prevBtn.addEventListener('click', function() {
  currentIndex = (currentIndex - 1 + galleryImgs.length) % galleryImgs.length;
  showImage();
});

nextBtn.addEventListener('click', function() {
  currentIndex = (currentIndex + 1) % galleryImgs.length;
  showImage();
});

function showImage() {
  const selectedImg = galleryImgs[currentIndex];
  modalImg.src = selectedImg.src;
}


const galleryImages = document.querySelectorAll('.gallery-img');

galleryImages.forEach((image) => {
  image.addEventListener('mouseenter', () => {
    // Add unblur class to the hovered image
    image.classList.add('unblur');
    // Add blur class to all other images
    galleryImages.forEach((otherImage) => {
      if (otherImage !== image) {
        otherImage.classList.add('blur');
      }
    });
  });

  image.addEventListener('mouseleave', () => {
    // Remove unblur and blur classes from all images
    galleryImages.forEach((otherImage) => {
      otherImage.classList.remove('unblur', 'blur');
    });
  });
});

