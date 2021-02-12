$(document).ready(function(){
    const integrity_err = JSON.parse(document.getElementById('integrity_error').textContent)
    if(integrity_err){
        alert(integrity_err)
    }

    const number_of_bundles = JSON.parse(document.getElementById('data_json').textContent)
    var modal = $('#delete_assurance_modal')
    var span = $('.close_modal_assurance')

    for(var iter = 0; iter < number_of_bundles; iter++) {
        $('#delete_assurance' + iter).click(function () {
            modal.css('display', 'block')
        })
    }

    span.click(function () {
        modal.css('display', 'none')
    })

    // window.onclick = function (event){
    //     if(event.target == modal){
    //         modal.css('display', 'none')
    //     }
    // }
    // $(document).click(function (my_event) {
    //     if(my_event.target == modal){
    //         modal.css('display', 'none')
    //     }
    // })
    $('#myModal').modal(options)
})

