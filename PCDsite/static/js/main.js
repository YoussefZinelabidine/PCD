var dropzone = document.getElementById("dropzone");
var dragContainer = document.querySelector('.drag-container');
const submitBtn = document.getElementById("Submit-btn");
const form = document.getElementById('uploadForm');

//Making the button work as the input tag
const Ifbutton = document.getElementById('import-files-btn');
const Ifinput = document.getElementById('import-files-inp');
Ifbutton.onclick = () => {
  Ifinput.click();
};
Ifinput.addEventListener("change", function () {
  const file = Ifinput.files[0];
  var fileType = file.type.toLowerCase();
  // Check if the dropped file is an image file
  if (fileType.indexOf('image') === 0) {
    var reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = function (e) {
      // Create a new image element for each dropped image file and add it to the image container
      var img = document.createElement('img');
      img.src = e.target.result;
      img.alt = file.name;
      img.id = "droppedImg";
      img.addEventListener('dragstart', function (e) {
        e.stopPropagation();
      });
      dragContainer.replaceChild(img, dropzone);
      submitBtn.style.display = "inline-block";
      Ifbutton.style.display = "none";
    }
  }
});

// Prevent default drag behaviors
["dragenter", "dragover", "dragleave", "drop"].forEach(function (eventName) {
  dropzone.addEventListener(eventName, preventDefaults, false);
  document.body.addEventListener(eventName, preventDefaults, false);
});

// Highlight dropzone when item is dragged over it
["dragenter", "dragover"].forEach(function (eventName) {
  dropzone.addEventListener(eventName, highlight, false);
});

// Unhighlight dropzone when item is dragged away from it
["dragleave", "drop"].forEach(function (eventName) {
  dropzone.addEventListener(eventName, unhighlight, false);
});

// Handle dropped items
dropzone.addEventListener("drop", handleDrop, false);

function preventDefaults(e) {
  e.preventDefault();
  e.stopPropagation();
}

function highlight(e) {
  dropzone.classList.add("dragover");
}

function unhighlight(e) {
  dropzone.classList.remove("dragover");
}

function handleDrop(e) {
  var files = e.dataTransfer.files;
  for (var i = 0; i < files.length; i++) {
    var file = files[i];
    var fileType = file.type.toLowerCase();
    // Check if the dropped file is an image file
    if (fileType.indexOf('image') === 0) {
      var reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = function (e) {
        // Create a new image element for each dropped image file and add it to the image container
        var img = document.createElement('img');
        img.src = e.target.result;
        img.alt = file.name;
        img.id = "droppedImg";
        img.addEventListener('dragstart', function (e) {
          e.stopPropagation();
        });
      dragContainer.replaceChild(img, dropzone);
      submitBtn.style.display = "inline-block";
      Ifbutton.style.display = "none"

        //create hidden input element and add it to the form to be submitted when you put image in the drag and drop area
        const imageData = reader.result;
        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'uploadFileDnD';
        input.value = imageData;
        input.setAttribute('form', 'uploadForm');
        submitBtn.parentNode.insertBefore(input, submitBtn); 
      }
    }
  }
}

