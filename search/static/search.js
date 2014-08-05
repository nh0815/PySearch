$(document).ready(function(){
	$('#form').submit(function(e){
		e.preventDefault();
		var query = $('#query').val();
		var docs = [];
		$.get('/search/query/', {query: query}, function(data){
			var result = JSON.parse(data);
			console.log(typeof result);
			for(var key in result){
				var obj = {};
				obj['doc'] = key;
				obj['score'] = result[key]
				docs.push(obj)
			}
			docs.sort(function(a, b){
				return b.score-a.score;
			});
			console.log(docs);
		});
	});
});