$(document).ready(function(){
    var modal = $('#delete_assurance_modal')
    var btn = $('#delete_assurance')
    var span = $('.close_modal_assurance')


    btn.click(function (){
        modal.css('display', 'block')
    })

    span.click(function () {
        modal.css('display', 'none')
    })

    window.click(function (event) {
        if(event.target == modal){
            modal.css('display', 'none')
        }
    })


})

