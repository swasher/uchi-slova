/**
 * Created by swasher on 08.03.2016.
 */

/*
Hook for table's buttons
 */

function simpleObjInspect(oObj, key, tabLvl)
// usage: alert(simpleObjInspect(Obj));
{
    key = key || "";
    tabLvl = tabLvl || 1;
    var tabs = "";
    for(var i = 1; i < tabLvl; i++){
        tabs += "\t";
    }
    var keyTypeStr = " (" + typeof key + ")";
    if (tabLvl == 1) {
        keyTypeStr = "(self)";
    }
    var s = tabs + key + keyTypeStr + " : ";
    if (typeof oObj == "object" && oObj !== null) {
        s += typeof oObj + "\n";
        for (var k in oObj) {
            if (oObj.hasOwnProperty(k)) {
                s += simpleObjInspect(oObj[k], k, tabLvl + 1);
            }
        }
    } else {
        s += "" + oObj + " (" + typeof oObj + ") \n";
    }
    return s;
}

$(document).ready(function() {

    // по нажитию выполняем вьюху, и изменяем цвет и текст в соответствии с
    // возвращенным из вььхи значением [для Import mode]
    $(".table").on('click','.btn', function(event) {

        var remember_or_not = $(this).attr("value");
        var accumulated_points = 0;

        switch (remember_or_not) {
            case "remember":
                accumulated_points = 1;
                break;
            case "notremember":
                accumulated_points = -2;
                break;
        }

        var pk = $(this).parents('tr').attr('value');

        if (!event.shiftKey) {
            // если кнопка нажата без шифта, то выполняется изменение поинтов
            $.getJSON("/change_points/", {pk: pk, accumulated_points: accumulated_points}, function (json) {
                $("table tr[value=" + pk + "] span[class='badge'] ").html(json['points']);
                $("table tr[value=" + pk + "] td[value='rus'] span").removeAttr("hidden");
            });
        }
        else {
            // а если с шифтом (скрытая функция), то удаляется запись
            $.getJSON("/delete_word/", {pk: pk}, function (json) {}
            );
        }
    });
});


/*
Registration form
 */

$(function() {

    $('#login-form-link').click(function(e) {
		$("#login-form").delay(100).fadeIn(100);
 		$("#register-form").fadeOut(100);
		$('#register-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#register-form-link').click(function(e) {
		$("#register-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
		$('#login-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});

});
