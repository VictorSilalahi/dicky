backendHost = "http://"+window.location.hostname+":7000/";

$(document).ready(function() {
    
    loadData();
    $("#btnTambahTipe").on("click", function() {
        if ($("#txtTipeBarang").val()=='')
        {
            alert("Masukkan tipe barang!");
            $("#txtTipeBarang").focus();
            return false;
        }        
        $.post( backendHost+"api/tipe", {namatipe: $("#txtTipeBarang").val()}, function(data, status) {
            if (status=="success")
            {
                if (data["msg"]=="ok")
                {
                    loadData();
                }
            }
            if (status=="error")
            {
                $("#tblTipeBarang tbody").html("Error!");
            }
        });

    });

});

$(document).on("click",".btnHapus",function() {
    if (confirm("Hapus tipe barang ini?")==true)  {
        var id = $(this).parent().parent().attr("id");
        $.ajax({
            url: backendHost+'api/tipe?tipeid='+id,
            type: 'DELETE',
            success: function (result) {
                loadData();
            }
        });
    }  
});

$(document).on("click",".btnEdit",function() {
    var id = $(this).parent().parent().attr("id");
    var tipe = $(this).parent().parent().find("td:eq(0)").text();
    $("#txtTipeId").val(id);
    $("#txtEditTipe").val(tipe);
    $("#modalEditTipe").modal("show");

});

$(document).on("click",".btnSaveEdit",function() {
    if (confirm("Simpan perubahan tipe barang ini?")==true)  {
        var id = $("#txtTipeId").val();
        var tipe = $("#txtEditTipe").val();
        $.ajax({
            url: backendHost+'api/tipe?tipeid='+id+"&nama="+tipe,
            type: 'PUT',
            success: function (result) {
                loadData();
                $("#modalEditTipe").modal("hide");
            }
        });
    }  

});

function loadData() {
    $("#tblTipeBarang > tbody").html("");
    $.get(backendHost+"api/tipe", function(data, status){
        if (status=="success")
        {
            if (data["msg"]=="ok")
            {
                var str="";
                var j=1;
                for (var i=0; i<data["data"].length; i++)
                {
                    str=str+"<tr id='"+data["data"][i]["tipeid"]+"'><th scope='row'>"+j+"</th><td>"+data["data"][i]["tipe"]+"</td><td><button class='btn btn-warning btnEdit'>Edit</button>&nbsp;<button class='btn btn-danger btnHapus'>Hapus</button></td></tr>"
                    j++;
                }
                $("#tblTipeBarang > tbody").html(str);    
            }
        }
        if (status=="error")
        {
            $("#tblTipeBarang tbody").html("Error!");
        }
      });
}




