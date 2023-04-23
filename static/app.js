function deleteMember(member) {
    document.getElementById('member-to-delete').value = member;
    submitDeleteForm();
}
function generateNewOrderAndTopic() {
    document.getElementById('generate-new-order-and-topic').value = 'true';
    document.querySelector('form[action="/"]').submit();
}
function submitDeleteForm() {
    document.getElementById('delete-form').submit();
}