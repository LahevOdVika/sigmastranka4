const ranges = document.querySelectorAll('.range');
const image = document.querySelector('.imageDrag');

let currentRotation = 0;
let currentScale = 100;

ranges.forEach(range => {
    const input = range.querySelector('input');
    const amount = range.querySelector('.amount');

    amount.textContent = input.value;

    input.addEventListener('input', function(e) {
        let newValue = e.target.value;
        amount.textContent = newValue;
        switch (e.target.id) {
            case 'size':
                currentScale = newValue;
                applyTransform();
                break;
            case 'rotation':
                currentRotation = newValue;
                applyTransform();
                break;
            case 'transparency':
                image.style.opacity = `${e.target.value / 100}`;
                break;
        }
    })
})

let isDragging = false;
let startX, startY;
let initialLeft, initialTop;

image.addEventListener('mousedown', (e) => {
    e.preventDefault();

    isDragging = true;

    startX = e.clientX;
    startY = e.clientY;


    const styles = window.getComputedStyle(image);

    initialLeft = parseFloat(styles.left) || 0;
    initialTop = parseFloat(styles.top) || 0;

    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', handleMouseUp);
});

function handleMouseMove(e) {
    if (!isDragging) return;

    const dx = e.clientX - startX;
    const dy = e.clientY - startY;

    image.style.left = `${initialLeft + dx}px`;
    image.style.top = `${initialTop + dy}px`;
}

function handleMouseUp() {
    if (!isDragging) return;

    isDragging = false;

    document.removeEventListener('mousemove', handleMouseMove);
    document.removeEventListener('mouseup', handleMouseUp);
}

image.addEventListener('dragstart', (e) => {
    e.preventDefault();
});

function applyTransform() {
    console.log(`rotate(${currentRotation}deg) scale(${currentScale / 100})`);
    image.style.transform = `rotate(${currentRotation}deg) scale(${currentScale / 100})`;
}