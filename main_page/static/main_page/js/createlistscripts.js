$(document).ready(function(){
    $("#append_button").click(function() {
        $('#task_list').append("<tr class='table-primary'><td><div class='input-group'><input type='text' name='list_of_tasks' class='form-control' placeholder='Task to do' aria-describedby='basic-addon1'><button type='button' class='btn-close align-self-sm-center mx-auto' data-bs-dismiss='modal' aria-label='Close'></button></div></td></tr>")
    });

})
