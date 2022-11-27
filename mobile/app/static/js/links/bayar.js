var backendHost = window.location.host+":1000/";

$(document).ready(function() {

    loadKeranjang();

    $(".btnBeli").on("click", function() {
        if ($("#txtNamaLengkap").val()=='')
        {
            alert("Masukkan nama lengkap!");
            return false;
        }
        if ($("#txtEmail").val()=='')
        {
            alert("Masukkan email!");
            return false;
        }
        if ($("#txtNoTelp").val()=='')
        {
            alert("Masukkan no telepon!");
            return false;
        }

        // $.post("http://127.0.0.1:7000/api/beli", {"fullname":$("#txtNamaLengkap").val(), "email": $("#txtEmail").val(), "notelp": $("#txtNoTelp").val(), "daftarbeli": $.parseJSON(sessionStorage.getItem("keranjang"))}, function(data, status){
        //     if (status=="success")
        //     {
        //         if (data["msg"]=="ok")
        //         {
        //             sessionStorage.clear();
        //             alert("Terima Kasih telah melakukan Pembelian di UD USAHA!");
        //             window.location.href = "/";

        //         }
        //     }
        //     if (status=="error")
        //     {
        //         alert("Operasi Error!");    
        //     }
        // });

        var formData = new FormData()
        
        formData.append('fullname', $("#txtNamaLengkap").val());
        formData.append('email', $("#txtEmail").val());
        formData.append('notelp', $("#txtNoTelp").val());
        formData.append('daftarbeli', JSON.stringify(sessionStorage.getItem("keranjang")) );
    
        // console.log(gbr);
        $.ajax({
            url: "http://127.0.0.1:7000/api/beli",
            type: 'POST',
            contentType: false,
            processData: false,
            cache: false,
            data: formData,
            success: function(res){
                sessionStorage.clear();
                alert("Terima Kasih telah melakukan Pembelian di UD USAHA!");
                window.location.href = "/";
        },
            error: function(){
                console.log('error')
            }
        });
    });


});

function loadKeranjang() {
    if (sessionStorage.getItem("keranjang")!=null)
    {
        var cart = $.parseJSON(sessionStorage.getItem("keranjang"));
        var str='';
        var sumTot = 0;
        for (var i=0; i<cart.length; i++)
        {
            str=str+"<tr id='"+cart[i][1]+"'><td>"+cart[i][0]+"</td><td>"+cart[i][2]+"</td><td>"+cart[i][3]+"</td><td>"+cart[i][4]+"</td></tr>";
            sumTot = sumTot + parseInt(cart[i][4]);
        }
        str=str+"<tr><td colspan='3'>Total Pembayaran</td><td><h3><span class='label label-info'>Rp. "+sumTot+"</span></h3></td></tr>";
        $("#tblKeranjang tbody").html(str);
    }
}


