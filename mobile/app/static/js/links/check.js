
$(document).ready(function() {

    if (sessionStorage.getItem("keranjang")!=null)
    {
        $("#dataKeranjang").html("<a href='/bayar'><button class='btn btn-info form-control'>Checkout!</div></a>");
    }

    $(".btnKeranjang").on("click", function() {

        if (parseInt($("#badgeJumlah").text())==0)
        {
            alert("Stock Kosong!");
            return false;
        }
        if (parseInt($("#badgeJumlah").text())<$("#txtJumlahDipesan").val())
        {
            alert("Pemesanan melebihi stock!");
            return false;
        }
        if (sessionStorage.getItem("keranjang")==null)
        {
            var cart = [];
            cart.push([$(".headingNama").text(), parseInt($("#txtBarangId").val()), parseInt($(".badgeHarga").text()), parseInt($("#txtJumlahDipesan").val()), parseInt($(".badgeHarga").text())*parseInt($("#txtJumlahDipesan").val())]);
            sessionStorage.setItem("keranjang",JSON.stringify(cart));
        }
        else
        {
            var cart = $.parseJSON(sessionStorage.getItem("keranjang"));
            console.log(cart);
            cart.push([$(".headingNama").text(), parseInt($("#txtBarangId").val()), parseInt($(".badgeHarga").text()), parseInt($("#txtJumlahDipesan").val()), parseInt($(".badgeHarga").text())*parseInt($("#txtJumlahDipesan").val())]);
            sessionStorage.setItem("keranjang",JSON.stringify(cart));
        }
        alert("Keranjang telah terisi!");
        console.log(sessionStorage.getItem("keranjang"));
    });


});

function loadKeranjang() {

}


