$(document).ready(function(){
    $('#input_new_title').css('display', 'none')

    $(document).on('click', '.show_task', function () {
        var fired_button = $(this).val();
        $('.h5_task_title').text(fired_button.slice(1,fired_button.search('~')))
        $('#save_task_changes').val(fired_button[0])
        var description = fired_button.slice(fired_button.search('~')+1, fired_button.length)
        if(description){
            $('#show_textarea').css('display', 'block')
            $('#addchangedesc').text('Change description:')
            $('#message-text').css('display', 'none')
        }
        else{
            $('#show_textarea').css('display', 'none')
            $('#addchangedesc').text('Add description:')
            $('#message-text').css('display', 'block')
        }
        $('#description_tag').text(description)
        // alert(description)
    });

    $(document).on('click', '#show_textarea', function () {
        $('#message-text').css('display', 'block')
        $('#show_textarea').css('display', 'none')
    })

    $(document).on('click', '#change_title', function () {
        $('#change_title').css('display', 'none')
        $('.h5_task_title').css('display', 'none')
        $('#input_new_title').css('display', 'block')
    })

    $(document).on('click', '#close_modal', function () {
        $('#input_new_title').css('display', 'none')
        $('.h5_task_title').css('display', 'block')
        $('#change_title').css('display', 'block')
    })

})