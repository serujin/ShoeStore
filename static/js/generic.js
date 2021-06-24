
function genericSuccess() {
    console.log("SUCCESS");
}

function genericError() {
    console.log("ERROR");
}

function ajaxToPostData(url, data, successFunction = genericSuccess, errorFunction = genericError) {
    $.ajax({
        url: "/" + url,
        type: "POST",
        data: data,
        headers: {"X-CSRFToken": get_token()},
        success: function(data) {
            successFunction(data);
        },
        error: function(data) {
            errorFunction(data);
        }
    });
}

function ajaxToGetData(url, data, successFunction = genericSuccess, errorFunction = genericError) {
    $.ajax({
        url: "/" + url,
        type: "GET",
        data_type: "json",
        data: data,
        headers: {"X-CSRFToken": get_token()},
        success: function(data) {
            successFunction(data);
        },
        error: function(error) {
            errorFunction(error);
        }
    });
}

function showFeedback(icon, title, confirmation, timer, backdrop, actionOnEnd = genericSuccess) {
    options = {
        icon: icon,
        title: title,
        showConfirmButton: confirmation,
        timer: timer,
        backdrop: backdrop
    }
    Swal.fire(options).then(() => {
        actionOnEnd()
    });
}