$(document).ready(function(){
	$('#form').submit(function(e){
		e.preventDefault();
		var spinner = $('<i class="fa fa-spinner fa-spin spinner"></i>');
		$('#submit').html(spinner);
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
			var length = docs.length;
			for(var i = 0; i < length; i++){
				var doc = docs[i];
				var row = $('<tr></tr>');
				row.attr('id', doc['doc']);
				var rank = $('<td></td>').text(i+1);
				var docid = $('<td></td>').text(doc['doc']);
				var score = $('<td></td>').text(doc['score']);
				row.append(rank);
				row.append(docid);
				row.append(score);
				$('#result-body').append(row);
			}
			$('#result-table').removeClass('disabled');
			$('#submit').html('Search');
			$('tr td').click(function(){
				var id = $(this).parent().attr('id');
				console.log(id);
				$.get('/search/document/', {doc: id}, function(bytes){
					var data = JSON.parse(bytes);
					var text = data.text;
					$('#modal-header h2').html(id);
					$('#modal-body').html(text);
					$('#modal-footer button').click(function(){
						$('#modal').modal('hide');
					});
					$('#modal').modal();
				});
			});
		});
	});
});