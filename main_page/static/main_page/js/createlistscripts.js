$(document).ready(function(){
    var task_line =



    $("#append_button").click(function() {
        // var fired_button = $(this).val();
        // del_message = "Are you sure you want to delete bundle: " + fired_button + "?"
        // $('#delete_content').text(del_message)
        // $('#confirm_deletion').val(fired_button)

        $('#append_tasks').append("<tr class='table-primary'><td><div class='input-group'><input type='text' name='list_of_tasks' className='form-control' placeholder='Task to do' aria-label='' aria-describedby='basic-addon1'></div></td></tr>")
    });


})
