/* Javascript for mediasiteXBlock. */
function mediasiteXBlockInitStudio(runtime, element) {

    $(element).find('.action-cancel').bind('click', function() {
        runtime.notify('cancel', {});
    });

    $(element).find('.action-save').bind('click', function() {
        var data = {
            'display_name': $('#mediasite_edit_display_name').val(),
//            'file_id': $('#mediasite_edit_file_id').val(),
            'iframe': $('#mediasite_edit_iframe').val(),
//            'width': $('#mediasite_edit_width').val(),
//            'height': $('#mediasite_edit_height').val(),
        };

        runtime.notify('save', {state: 'start'});

        var handlerUrl = runtime.handlerUrl(element, 'save_mediasite');
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            if (response.result === 'success') {
                runtime.notify('save', {state: 'end'});
                // Reload the whole page :
                // window.location.reload(false);
            } else {
                runtime.notify('error', {msg: response.message})
            }
        });
    });
}
