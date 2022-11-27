$(document).ready(function() {
    
    loadTipe();

});

function loadTipe() {
    $("#divTipe").html("");
    $.get("http://127.0.0.1:7000/api/tipe", function(data, status){
        if (status=="success")
        {
            if (data["msg"]=="ok")
            {
                var str="";
                for (var i=0; i<data["data"].length; i++)
                {
                    str=str+"<div class='col-xs-6 col-sm-3 placeholder'><a href='http://127.0.0.1:1000/tipe/"+data["data"][i]['tipeid']+"'><img src='http://127.0.0.1:7000/"+data["data"][i]['path']+"' width='200' height='200' class='img-responsive'><h4>"+data["data"][i]['tipe']+"</h4></a></div>";
      
                }
                $("#divTipe").html(str);    
            }
        }
        if (status=="error")
        {
            $("#divTipe").html("Error!");    
        }
    });
}



