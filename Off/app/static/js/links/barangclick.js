$(document).on("dblclick", "#tblBarang tbody tr td", function() {
    var currentRow=$(this).closest("tr"); 
    var barangid = currentRow.attr("id");

    if ($(this).index()==3)
    {
        var jumlahBaru = prompt("Masukkan jumlah barang yang baru!");
        if (jumlahBaru == null || jumlahBaru == "") {
            return false;
        } 
        else {
            $.ajax({
                url: backendHost+'api/barang/jumlah?barangid='+barangid+"&jumlah="+jumlahBaru,
                type: 'PUT',
                success: function (result) {
                    loadBarang();
                }
            });
    
        }

    }
    if ($(this).index()==4)
    {
        var hargaBaru = prompt("Masukkan harga barang yang baru!");
        if (hargaBaru == null || hargaBaru == "") {
            return false;
        } 
        else {
            $.ajax({
                url: backendHost+'api/barang/harga?barangid='+barangid+"&harga="+hargaBaru,
                type: 'PUT',
                success: function (result) {
                    loadBarang();
                }
            });

        }

    }

});




