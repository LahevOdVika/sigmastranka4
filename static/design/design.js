const ranges = document.querySelectorAll('.range');

ranges.forEach(range => {
    const input = range.querySelector('input');
    const amount = range.querySelector('.amount');

    amount.textContent = input.value;

    input.addEventListener('input', function(e) {
        amount.textContent = e.target.value;
    })
})