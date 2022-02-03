
/*
function generarNuevoColor(){
	let codigo, color;
    let numeros="0123456789"
    let letras="ABCDEF"
	codigo = numeros+letras
	color = "#"

	for(let i = 0; i < 6; i++){
        console.log(color)
        console.log(codigo[Math.floor(Math.random() * 16)])
		color = color + codigo[Math.floor(Math.random() * 16)];
	}

    let contenido = document.getElementById("contenido")
  
    contenido.style.background=color
	

}*/


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
