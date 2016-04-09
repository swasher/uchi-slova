/**
 * Created by swasher on 08.03.2016.
 */



function simpleObjInspect(oObj, key, tabLvl)
/**
 * Function for debugging purpose. It help check objects of any type.
 *
 * usage: alert(simpleObjInspect(Obj));
 *
 */

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

/*
Hook for table's buttons
 */

$(document).ready(function() {

    // по нажитию выполняем вьюху, и изменяем цвет и текст в соответствии с
    // возвращенным из вььхи значением [для Import mode]
    $(".table").on('click','.choisebtn', function(event) {

        var word_is_remembered = $(this).attr("value");
        var accumulated_points = 0;

        switch (word_is_remembered) {
            case "remember":
                accumulated_points = 1;
                break;
            case "notremember":
                accumulated_points = -2;
                break;
        }

        var pk = $(this).parents('tr').attr('id');

        // при нажатии кнопки выполняется изменение поинтов
        // если достигнут лимит запоминания, выдается сообщение
        $.getJSON("/change_points/", {pk: pk, accumulated_points: accumulated_points}, function (json) {
            $("table tr[id=" + pk + "] span[class='badge'] ").html(json['points']);
            if (json['limit']) {
                $("table tr[id=" + pk + "] td[value='rus'] span:first").text("You can remember!").addClass("win");
                //$("table tr[id=" + pk + "] td[value='rus'] span:first").addClass("win");
            } else {
                $("table tr[id=" + pk + "] td[value='rus'] span").removeAttr("hidden");
            }
        });

    });


    $('[data-toggle="confirmation"]').confirmation({
        title: "Are you sure to remove?",
        placement: "left",
        singleton: "True",
        popout: "True",
        container: 'body',
        btnOkLabel: "&nbsp;Delete",
        btnOkClass: "btn-xs btn-danger",
        btnOkIcon: "glyphicon glyphicon-remove",
        btnCancelLabel: "&nbsp;Cancel",
        btnCancelIcon: "glyphicon glyphicon-repeat",
        onConfirm: function(event, element) {
            var pk = $(this).parents('tr').attr('id');

            $.getJSON("/delete_word/", {pk: pk}, function (json) {
                // put here refresh table code

                // or we can remove row right now from DOM

            });
            $(this).confirmation('destroy');
            $(this).parents('tr').remove();
        }
    });

});


/* deprecated

/!*
Registration form
 *!/

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
*/
