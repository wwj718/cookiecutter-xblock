/* Javascript for {{cookiecutter.repo_name}}XBlock. */
function {{cookiecutter.repo_name}}XBlockInitStudio(runtime, element) {

    $(element).find('.action-cancel').bind('click', function() {
        runtime.notify('cancel', {});
    });

    $(element).find('.action-save').bind('click', function() {
        var data = {
            'display_name': $('#{{cookiecutter.repo_name}}_edit_display_name').val(),
//            'file_id': $('#{{cookiecutter.repo_name}}_edit_file_id').val(),
            'iframe': $('#{{cookiecutter.repo_name}}_edit_iframe').val(),
//            'width': $('#{{cookiecutter.repo_name}}_edit_width').val(),
//            'height': $('#{{cookiecutter.repo_name}}_edit_height').val(),
        };

        runtime.notify('save', {state: 'start'});

        var handlerUrl = runtime.handlerUrl(element, 'save_{{cookiecutter.repo_name}}');
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
