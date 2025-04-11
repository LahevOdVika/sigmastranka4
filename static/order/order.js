function redirectToDesignPage(model) {
    fetch('/design', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            model: model
        })
    })
    .then(response => response.text())
    .then(data => {
        window.location.href = '/design';
    })
    .catch(error => {
        console.error('Error:', error);
    });
}