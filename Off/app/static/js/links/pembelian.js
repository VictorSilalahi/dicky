var backendHost = "http://"+window.location.hostname+":7000/";

$(document).ready(function() {
    
    $("#dpPembelian").datepicker();

    $("#btnProsesDataPembelian").on("click", function() {
        if ($("#dpPembelian").val()=='')
        {
            alert("Tentukan tanggal!");
            $("#dpPembelian").focus();
            return false;
        }
        loadPembelian($("#dpPembelian").val());
    });

});

$(document).on("click", ".btnBayar", function() {
    var nf = Intl.NumberFormat();
    var cartid = $(this).parent().parent().attr("id");
    $.get(backendHost+"api/cart/detail", {cid: cartid}, function(data, status){
        if (status=="success")
        {
            if (data["msg"]=="ok")
            {
                var str="";
                var j=1;
                var sumTot=0;
                for (var i=0; i<data["data"].length; i++)
                {
                    str=str+"<tr id='"+data["data"][i]["cartdescid"]+"'><th scope='row'>"+j+"</th><td>"+data["data"][i]["nama"]+"</td><td>"+data["data"][i]["jumlah"]+"</td><td>"+nf.format(data["data"][i]["total"])+"</td><td></td></tr>";
                    sumTot = sumTot + parseInt(data["data"][i]["total"]);
                    j++;
                }
                str=str+"<tr><td colspan='3'>T o t a l</td><td>"+nf.format(sumTot)+"</td></tr>";
                $("#tblBeliDetail > tbody").html(str);    
            }
            $("#txtCartId").val(cartid);
            $("#modalDetail").modal("show");
        }
        if (status=="error")
        {
            $("#tblPembelian tbody").html("Error!");
        }
    });

});

$(document).on("click", ".btnHapusPembelian", function() {
    if (confirm("Hapus pembelian ini?")==true)
    {
        var cartid = $(this).parent().parent().attr("id");
        $.ajax({
            url: backendHost+'api/cart/detail?cid='+cartid,
            type: 'DELETE',
            success: function (result) {
                loadPembelian($("#dpPembelian").val());
            }
        });
    }
});

$(document).on("click", ".btnLunaskan", function() {
    if (confirm("Pembayaran dilunaskan?")==true)
    {
        var cartid = $("#txtCartId").val();
        var cara = $("#slcJenisPembayaran").val();
        $.ajax({
            url: backendHost+'api/cart/detail?cara='+cara+'&cid='+cartid,
            type: 'POST',
            success: function (result) {
                loadPembelian($("#dpPembelian").val());
                $("#modalDetail").modal("hide");
            }
        });
    }
});

function loadPembelian(tgl) {
    $("#tblPembelian > tbody").html("");
    var tglout = tgl.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
    $.post(backendHost+"api/cart", {tanggal: tglout}, function(data, status){
        if (status=="success")
        {
            if (data["msg"]=="ok")
            {
                console.log(data["data"]);
                var str="";
                var j=1;
                for (var i=0; i<data["data"].length; i++)
                {
                    str=str+"<tr id='"+data["data"][i]["cartid"]+"'><th scope='row'>"+j+"</th><td>"+data["data"][i]["fullname"]+"</td><td>"+data["data"][i]["email"]+"</td><td>"+data["data"][i]["telp"]+"</td><td><button class='btn btn-danger btnHapusPembelian'>Hapus</button>&nbsp;<button class='btn btn-primary btnBayar'>Bayar</button></td></tr>"
                    j++;
                }
                $("#tblPembelian > tbody").html(str);    
            }
        }
        if (status=="error")
        {
            $("#tblPembelian tbody").html("Error!");
        }
    });
}




