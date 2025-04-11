function redirectToDesignPage(model) {
    model = model.toLowerCase();
    model = model.replaceAll(/\s/g, '');
    window.location.href = 'design/' + model + '/';
}