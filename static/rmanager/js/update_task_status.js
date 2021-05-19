$(document).ready(function() {
    /*
    $('#beforeRefresh').on('show.bs.modal', function (e) {
        no = $('#status').hasClass('alert-warning')
        if (no) {
            return e.preventDefault() // stops modal from being shown
        }
    })
    */

    var termClass = document.getElementById('terminal')
    termClass.classList = 'body_foreground body_background'

    var taskinfo = $('#taskinfo')
    const update_url = taskinfo.data('updateurl')    

    var term = $('#terminal')
    var status = $('#status')
    var out = []
    $.ajax({
        type: 'GET',
        url: update_url,
        dataType: 'json',
        success: function (response) {
            if (response.line) {
                term.html(response.line.line)  
                status.html(response.state)             
            }
            get_task_update()
            }
        })
    
    function get_task_update() {
        $.ajax({
            type: 'GET',
            url: update_url,
            dataType: 'json',
            success: function (response) {                
                if (response.line) {
                    if (!(out.includes(response.line.iter))) {
                        //status.html('<i class="fas fa-cogs"></i> ' + response.state) 
                        status.html(`<div class="spinner-border text-danger" role="status">
                        <span class="visually-hidden">Loading...</span>
                      </div>`) 
                        // status.removeClass()
                        // status.addClass('alert alert-warning')
                        term.html(response.line.line)
                        out.push(response.line.iter)
                    }             
                }
                const state = response.state
                if (state === 'SUCCESS') {
                    status.html('<i class="fas fa-check-circle"></i> ' + response.state) 
                    status.removeClass()
                    status.addClass('alert alert-success')
                    term.html(response.line)
                    return false                   
                } else if (state === 'FAILURE') {
                    status.removeClass()
                    status.addClass('alert alert-danger')
                    status.html('<i class="fas fa-exclamation-circle"></i> ' + response.state) 
                    return false
                }
                setTimeout(get_task_update, 1000)
            }
        })
    }
})
