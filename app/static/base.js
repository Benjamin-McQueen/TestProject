$(document).ready(function () {
    $('#table_id').DataTable();
});

$("#users").on('change', function(e) {
    console.log($("#users").val());
    e.preventDefault();
    $.ajax('/getuserdata', {
        type: 'POST',  // http method
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({data: parseInt($("#users").val())}),  // data to submit
        success: function (data, status, xhr) {
            // console.log("Success");
            // console.log(data);
            document.getElementById('username').value = data.username
            document.getElementById('email').value = data.email
        }
        // error: function (jqXhr, textStatus, errorMessage) {
        //     console.log('Error' + errorMessage);
        // }
    });
});

$("#delete_button").click(function(e) {
    console.log($("#users").val());
    e.preventDefault();
    $.ajax('/deleteuserdata', {
        type: 'POST',  // http method
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({data: parseInt($("#users").val())}),  // data to submit
        success: function (data, status, xhr) {
            console.log("user deleted");
            location.reload();
        }
    });
});

$("#edit_button").click(function(e) {
    console.log($("#users").val());
    e.preventDefault();

    var userdata = {
        id: $("#users").val(),
        username: $("#username").val(),
        email: $("#email").val(),
        pw: $("#pw").val()
    }

    $.ajax('/edituserdata', {
        type: 'POST',  // http method
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(userdata),  // data to submit
        success: function (data, status, xhr) {
            console.log("user updated");
        }
    });
});

$("body").bind("ajaxSend", function (elm, xhr, s) {
    if (s.type == "POST") {
        xhr.setRequestHeader('X-CSRF-Token', getCSRFTokenValue());
    }
});