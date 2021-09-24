$(document).ready( function () {
    $('#table_id').DataTable();
} );

$("body").bind("ajaxSend", function(elm, xhr, s){
   if (s.type == "POST") {
      xhr.setRequestHeader('X-CSRF-Token', getCSRFTokenValue());
   }
});