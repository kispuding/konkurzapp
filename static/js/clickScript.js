$(document).ready(function(){
    $(".check").click( function(){

        if ($(this).attr("class") == "checked")  {
               $(this).attr("class", "check");
        }
        else {
            $(this).attr("class", "checked");
        }
    });
});

$(document).ready( function() {
    $(".pos").click( function() {
        var elements = document.getElementsByClassName("checked");
        for (i = 0; i < elements.length; i++){
            var j = i+1;
            $("<input type='text' value='' />")
            .attr("value", elements[i].textContent)
            .attr("name", "pos_" + j)
            .appendTo("#pos");
        }
//        $("button").not( document.getElementsByClassName("checked")).remove();
    })
});

$(document).ready( function() {
    $(".skill").click( function() {
        var elements = document.getElementsByClassName("checked");
        for (i = 0; i < elements.length; i++){
            var j = i+1;
            $("<input type='text' value='' />")
            .attr("value", elements[i].textContent)
            .attr("name", "skill_" + j)
            .appendTo("#skill");
        }
    })
});

$(document).ready(function() {
        $(".finishheader").animate({
            height: "+=70%"
        },3000);
});

