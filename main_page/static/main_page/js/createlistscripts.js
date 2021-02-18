$(document).ready(function(){
    // $("#append_button").click(function() {
    $(document).on('click', '#append_button', function () {
        $('#task_list').append("<tr class='table-primary'><td><div class='input-group'><input type='text' name='list_of_tasks' class='form-control' placeholder='Task to do' aria-describedby='basic-addon1' maxlength='40' required><button type='button' class='btn btn-danger align-self-sm-center mx-auto deleteTask'>❌</button></div></td></tr>")
    })

    $(document).on('click', '.deleteTask', function () {
        $(this).parent().parent().parent().remove()
        console.log("hello")
    })

})