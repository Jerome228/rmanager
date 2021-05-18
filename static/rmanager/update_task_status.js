$(document).ready(function() {

    var taskinfo = $('#taskinfo')
    const update_url = taskinfo.data('updateurl')

    $('<div>',{
        'id': 'task-status',
        'html': `<a href="${update_url}">Update URL</a>` 
    }).appendTo('#taskinfo')

    var term = $('#terminal')
    var out = []
    $.ajax({
        type: 'GET',
        url: update_url,
        dataType: 'json',
        success: function (response) {
            if (response.line) {
                term.html(response.line.line)                
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
                        term.html(response.line.line)
                        out.push(response.line.iter)
                    }             
                }
                const state = response.state
                if (state === 'SUCCESS') {
                    term.html(response.line)
                    return false                   
                } else if (state === 'FAILURE') {
                    return false
                }
                setTimeout(get_task_update, 1000)
            }
        })
    }
})
