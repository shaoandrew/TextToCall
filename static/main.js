var textBox = $('textarea');
//deprecated, need to change to async sometime
$.ajaxSetup({async: false});
var submit = function(){
	event.preventDefault();
};

var generateInsult = function(){
	var insult = httpGet();
	textBox.val(insult);
};

var httpGet = function()
{
    var result;
    result = $.getJSON('/insult', function(ajaxresult){
        return ajaxresult;
    });
    return result.responseText;
};



