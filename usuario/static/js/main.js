

$(document).ready(function(){

    let btnLogin = $("#btnLogin")
    let btnOtroLogin = $("#OtroLogin")
    btnOtroLogin.click(function(){

        $("#miModal").modal()
    })

    btnLogin.click(function(){

        $("#miModal").modal()
    })

    $("#btnAceptar").click(function(){
        let user=$("#txt_user")
        let pass=$("#txt_pass")
        if (user.val()=="" || user.val()==" " || pass.val()=="" || pass.val()==""){
            alert("campos en blancos")
        }
        else{
            alert("Logeado")
        }   
    })
    $("#btnCancelar").click(function(){

        let user=$("#txt_user")
        let pass=$("#txt_pass")
        user.val("")
        pass.val("")
        $("#miModal").modal('hide')
    })



})
