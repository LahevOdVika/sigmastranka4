const rotatingTextHandler = document.querySelector('.rotatingTextHandler');
const options = {
    'Pixel': 'green',
    'Apple': 'blue',
    'Samsung': 'red',
}
let currentIndex = 0;

function changeHandler() {
    if (currentIndex < Object.keys(options).length - 1) {
        currentIndex++;
    } else {
        currentIndex = 0;
    }
    rotatingTextHandler.innerHTML = Object.keys(options)[currentIndex];
    rotatingTextHandler.style.color = Object.values(options)[currentIndex];
}

changeHandler();
setInterval(changeHandler, 1000);