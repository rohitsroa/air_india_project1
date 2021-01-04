$('input[type=text]').keypress(function(event) {
    if (event.keyCode == 13) {
    	$('textarea').val("hello");
        event.preventDefault();
    }
});