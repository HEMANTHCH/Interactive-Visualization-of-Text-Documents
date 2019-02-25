$( function() {
	$( "#sortable" ).sortable();
	$( "#sortable" ).disableSelection();
});


$(document).ready(function(){
	$('input[type="checkbox"]').click(function(){
		var inputValue = $(this).attr("value");
		//console.log($("."+inputValue).toggle());
		console.log(inputValue);
		$("." + inputValue).toggle();
	}); 
});

$(document).ready(function(){
  $("#myInput").on("keyup", function() {
	var value = $(this).val().toLowerCase();
	$("#myList li").filter(function() {
	  $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
	}); 
  }); 
});

$( ".row_position" ).sortable({
	delay: 150,
	stop: function() {
		var selectedData = new Array();
		$('.row_position>li').each(function() {
			selectedData.push($(this).attr("id"));
		});
	}
});

$('input:checkbox').change(function(){
	if($(this).is(':checked')) 
       	$(this).parent().addClass('active'); 
  	else 
      	$(this).parent().removeClass('active')
});

function test(elem) {
	var a = elem.innerText;
	var res = a.split("\n");
	var arr = res.slice(1, res.length-1);
	console.log(arr);
}

function test1(elem) {
	var clusterName = elem.innerHTML;
	var r = /\d+/;
	var clusterNum = parseInt(clusterName.match(r)[0]);
	clusterNum += 1;
	var arr = document.getElementById("sortable").innerText;
	var temp = "Cluster " + clusterNum;
	var a = arr.indexOf(clusterName);
	var b = arr.indexOf(temp);
	var res = arr.slice(a,b);
	var arrData = res.split("\n");
	var tempData = arrData.slice(1, arrData.length-1);

	for (var i=0; i<tempData.length; i++) {
		$("."+tempData[i]).toggle();
	}
}


