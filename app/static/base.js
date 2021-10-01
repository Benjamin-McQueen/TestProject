$(document).ready(function () {
    $('#table_id').DataTable();
});

$("#fubutton").click(function() {
    console.log($("#users").val());
    $.ajax('/getuserdata', {
        type: 'POST',  // http method
        data: {data: $("#users").val()},  // data to submit
        success: function (data, status, xhr) {
            console.log("Success");
            console.log(data);
        },
        error: function (jqXhr, textStatus, errorMessage) {
            console.log('Error' + errorMessage);
        }
    });
});

$("body").bind("ajaxSend", function (elm, xhr, s) {
    if (s.type == "POST") {
        xhr.setRequestHeader('X-CSRF-Token', getCSRFTokenValue());
    }
});