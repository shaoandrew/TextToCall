var textBox = $('.message textarea');
var number = $('.message input');

var submit = function(){
	event.preventDefault();
	number.val("hello");
};

var generateInsult = function(){
	var insult = httpGet();
	textBox.val(insult);
};

var httpGet = function()
{
    result = $.getJSON('http://pacific-stream-4609.herokuapp.com/insult',function(ajaxresult){
    	return ajaxresult;
    });

    return result;
}



