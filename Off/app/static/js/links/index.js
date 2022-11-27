$(document).ready(function() {
    
    $("#btnLogin").on("click", function() {
        if ($("#txtUsername").val()=="")
        {
            alert("Masukkan username!");
            return false;
        }
        if ($("#txtPassword").val()=="")
        {
            alert("Masukkan password!");
            return false;
        }
        $("#frmLogin").submit();
        
    });

});

$(document).on("click",".btn-delete",function() {
    if (confirm("Hapus link berita ini?")==true)  {
       var tr =  $(this).parent().parent();
       tr.remove();
    }  
});




