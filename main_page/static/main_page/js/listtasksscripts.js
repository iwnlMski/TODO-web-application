$(document).ready(function(){
    alert('hi')

    // $(".show_task").click(function() {
    $(document).on('click', '.show_task', function () {
        var fired_button = $(this).val();
        $('.h5_task_title').text(fired_button)
        // $('#confirm_deletion').val(fired_button)
    });


}