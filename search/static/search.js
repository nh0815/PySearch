$(document).ready(function(){
	$('#form').submit(function(e){
		e.preventDefault();
		var query = $('#query').val();
		$.get('/search/query/', {query: query}, function(data){
			alert(data);
		});
	});
});