const canvas = document.getElementById('drawingCanvas');
const ctx = canvas.getContext('2d');
let drawing = false;

canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mousemove', draw);

function startDrawing(event) {
    drawing = true;
    draw(event); // Draw a dot when starting to draw
}

function stopDrawing() {
    drawing = false;
    ctx.beginPath(); // Reset the path
}

function draw(event) {
    if (!drawing) return;

    ctx.lineWidth = 5;
    ctx.lineCap = 'round';
    ctx.strokeStyle = 'black';

    ctx.lineTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
}

document.getElementById('saveButton').addEventListener('click', function () {
    const imageData = canvas.toDataURL('image/png');
    document.getElementById('imageData').value = imageData;
    document.getElementById('imageForm').submit();
});

window.onload = function () {
    
    const img = new Image();
    img.onload = function () {
        ctx.drawImage(img, 0, 0);
    };
    img.onerror = function () {
        console.error("Image failed to load.");
    };
    img.src = notesData.imageUrl;
    console.log("Image URL: ", img.src); // Debug line to check the image URL
};      
