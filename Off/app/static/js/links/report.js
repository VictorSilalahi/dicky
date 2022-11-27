var backendHost = "http://"+window.location.hostname+":7000/";

$(document).ready(function() {
    
    $("#dpPenjualan").datepicker();

    $("#btnProsesDataPenjualan").on("click", function() {
        if ($("#dpPenjualan").val()=='')
        {
            alert("Tentukan bulan tahun!");
            $("#dpPenjualan").focus();
            return false;
        }
        loadReport($("#dpPenjualan").val(), $("#slcCaraBayar").val());
    });

});


$(document).on("click", ".btnCetak", function() {
    PrintMe('divReport');
});

function loadReport(tgl, cara) {
    $("#tblPembelian > tbody").html("");
    var tglout = tgl.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
    var temp = tglout.split("-");
    var nf = Intl.NumberFormat();
    $.get(backendHost+"api/report", {bln: temp[1], thn: temp[0], cara: cara}, function(data, status){
        if (status=="success")
        {
            if (data["msg"]=="ok")
            {
                console.log(data["data"]);
                var str="";
                var j=1;
                var sumTot = 0;
                for (var i=0; i<data["data"].length; i++)
                {
                    str=str+"<tr><th scope='row'>"+j+"</th><td>"+data["data"][i]["tanggal"]+"</td><td>"+nf.format(data["data"][i]["total"])+"</td><td>"+data["data"][i]["nama"]+"</td></tr>";
                    sumTot = sumTot + parseInt(data["data"][i]["total"]);
                    j++;
                }
                str=str+"<tr><th scope='row'></th><td>T o t a l</td><td>"+nf.format(sumTot)+"</td><td></td></tr>";
                $("#tblReport > tbody").html(str);    
            }
        }
        if (status=="error")
        {
            $("#tblReport tbody").html("Error!");
        }
    });
}

function PrintMe(DivID) {
    var disp_setting="toolbar=yes,location=no,";
    disp_setting+="directories=yes,menubar=yes,";
    disp_setting+="scrollbars=yes,width=650, height=600, left=100, top=25";
       var content_vlue = document.getElementById(DivID).innerHTML;
       var docprint=window.open("","",disp_setting);
       docprint.document.open();
       docprint.document.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"');
       docprint.document.write('"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">');
       docprint.document.write('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">');
       docprint.document.write('<head><title>Cetak</title>');
       docprint.document.write("<meta http-equiv='content-script-type' content='text/javascript'>");
        docprint.document.write("<link rel='stylesheet' href='"+$("#vbaseurl").val()+"assets/css/bootstrap.css'>");
        docprint.document.write("<link rel='stylesheet' href='"+$("#vbaseurl").val()+"assets/css/style.css'>");
        docprint.document.write("<script src='"+$("#vbaseurl").val()+"assets/js/bootstrap.min.js'></script>");
       docprint.document.write('<style type="text/css">body{ margin:0px;');
       docprint.document.write('font-family:verdana,Arial;color:#000;');
       docprint.document.write('font-family:Verdana, Geneva, sans-serif; font-size:12px;}');
       docprint.document.write('a{color:#000;text-decoration:none;} </style>');
       docprint.document.write('</head><body onLoad="self.print()"><center>');
       docprint.document.write(content_vlue);
       docprint.document.write('</center></body></html>');
       docprint.document.close();
       docprint.focus();
    }



