$(document).ready(function(){
    const integrity_err = JSON.parse(document.getElementById('integrity_error').textContent)
    if(integrity_err){
        alert(integrity_err)
    }

    $(document).on('click', '.delete_button', function () {
        var fired_button = $(this).val();
        del_message = "Are you sure you want to delete bundle: " + fired_button + "?"
        $('#delete_content').text(del_message)
        $('#confirm_deletion').val(fired_button)
    });
})

