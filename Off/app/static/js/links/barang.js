var backendHost = "http://"+window.location.hostname+":7000/";

$(document).ready(function() {
    
    loadBarang();
    loadTipe();
    $(".btnTambahBarang").on("click", function() {
        if ($("#txtNamaBarang").val()=='')
        {
            alert("Masukkan nama barang!");
            $("#txtNamaBarang").focus();
            return false;
        }        
        if ($("#txtJumlah").val()=='')
        {
            alert("Masukkan jumlah barang!");
            $("#txtJumlah").focus();
            return false;
        }        
        if ($("#txtHarga").val()=='')
        {
            alert("Masukkan harga barang!");
            $("#txtHarga").focus();
            return false;
        }        
        if ($("#txtFile").val()=='')
        {
            alert("Masukkan gambar barang!");
            $("#txtFile").focus();
            return false;
        }        
        if ($("#txtKeterangan").val()=='')
        {
            alert("Masukkan keterangan barang!");
            $("#txtKeterangan").focus();
            return false;
        }        

        var formData = new FormData()
        var gbr = $('#txtFile')[0].files[0]
        
        formData.append('nama', $("#txtNamaBarang").val());
        formData.append('satuan', $("#slcSatuan").val());
        formData.append('tipe', $("#slcTipe").val());
        formData.append('jumlah', $("#txtJumlah").val());
        formData.append('harga', $("#txtHarga").val());
        formData.append('fileGambar', gbr);
        formData.append('ket', $("#txtKeterangan").val());
    
        // console.log(gbr);
        $.ajax({
            url: backendHost+'api/barang',
            type: 'POST',
            contentType: false,
            processData: false,
            cache: false,
            data: formData,
            success: function(res){
                console.log('successfully');
                loadBarang();
                bersih();                
            },
            error: function(){
                console.log('error')
            }
        });

    });

});

$(document).on("click",".btnHapus",function() {
    if (confirm("Hapus barang ini?")==true)  {
        var id = $(this).parent().parent().attr("id");
        $.ajax({
            url: backendHost+'api/barang?barangid='+id,
            type: 'DELETE',
            success: function (result) {
                loadBarang();
            }
        });
    }  
});

$(document).on("click",".btnEdit",function() {
    var id = $(this).parent().parent().attr("id");
    var nama = $(this).parent().parent().find("td:eq(0)").text();
    var satuan = $(this).parent().parent().find("td:eq(1)").text();
    var tipe = $(this).parent().parent().find("td:eq(4)").text();
    $("#txtBarangId").val(id);
    $("#txtEditBarang").val(nama);
    $("#slcTipeEdit option [text=" + tipe +"]").prop("selected", "selected");
    $("#slcSatuanEdit option [text=" + satuan +"]").prop("selected", "selected");
    $("#modalEditBarang").modal("show");

});

$(document).on("click",".btnSaveEdit",function() {
    if (confirm("Simpan perubahan data barang ini?")==true)  {
        var id = $("#txtBarangId").val();
        var nama = $("#txtEditBarang").val();
        var satuan = $("#slcSatuanEdit").val();
        var tipe = $("#slcTipeEdit").val();
        $.ajax({
            url: backendHost+'api/barang?barangid='+id+"&nama="+nama+"&satuan="+satuan+"&tipeid="+tipe,
            type: 'PUT',
            success: function (result) {
                loadBarang();
                $("#modalEditBarang").modal("hide");
            }
        });
    }  

});

function loadBarang() {
    $("#tblBarang > tbody").html("");
    $.get(backendHost+"api/barang", function(data, status){
        if (status=="success")
        {
            if (data["msg"]=="ok")
            {
                var str="";
                var j=1;
                for (var i=0; i<data["data"].length; i++)
                {
                    str=str+"<tr id='"+data["data"][i]["barangid"]+"'><th scope='row'>"+j+"</th><td>"+data["data"][i]["nama"]+"</td><td>"+data["data"][i]["satuan"]+"</td><td>"+data["data"][i]["jumlah"]+"</td><td>"+data["data"][i]["harga"]+"</td><td>"+data["data"][i]["tipe"]+"</td><td><button class='btn btn-warning btnEdit'>Edit</button>&nbsp;<button class='btn btn-danger btnHapus'>Hapus</button></td></tr>"
                    j++;
                }
                $("#tblBarang > tbody").html(str);    
            }
        }
        if (status=="error")
        {
            $("#tblBarang tbody").html("Error!");
        }
    });
}

function loadTipe() {
    $("#slcTipe").empty();
    $.get(backendHost+"api/tipe", function(data, status){
        if (status=="success")
        {
            if (data["msg"]=="ok")
            {
                var str="";
                for (var i=0; i<data["data"].length; i++)
                {
                    str=str+"<option value='"+data["data"][i]["tipeid"]+"'>"+data["data"][i]["tipe"]+"</option>";
                }
                $("#slcTipe").html(str);    
                $("#slcTipeEdit").html(str);    
            }
        }
        if (status=="error")
        {
            $("#slcTipe").html("");
            $("#slcTipeEdit").html("");    
        }
    });
}

function bersih() {
    $("#txtNamaBarang").val("");
    $("#slcSatuan").val("");
    $("#slcTipe").val("");
    $("#txtJumlah").val("");
    $("#txtHarga").val("");
    $('#txtFile').val("");
    $('#txtKeterangan').val("");

}


