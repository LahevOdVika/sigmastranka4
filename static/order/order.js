function submitModel(id, model) {
    document.querySelector('.model').value = JSON.stringify({id: id, model: model});
    document.querySelector('.modelForm').submit();
}