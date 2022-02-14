$(document).ready(function(){
    $("#miForm").validate({
        rules:{
            txt_nombre:{
                required: true
                
            },
            txt_fono:{
                required: true,
                digits: true
                
            },
            txt_correo:{
                required: true
                
            },
            txt_mensaje:{
                required: true
                
            }
            
        },
        messages:{
            txt_nombre:{
                required: "Debe ingresar un nombre"
            },
            txt_fono:{
                required: "Debe ingresar un fono"
            },
            txt_correo:{
                required: "Debe ingresar un correo"
            },
            txt_mensaje:{
                required: "Debe ingresar un mensaje"
            }

        }
    });
});