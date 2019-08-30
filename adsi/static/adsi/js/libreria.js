function verAprendiz(ruta) {
    $.ajax({
        url: ruta,
        success: function(respuesta) {
            document.getElementById('resultado').innerHTML = respuesta;
            console.log(respuesta);

        },
        error: function() {
            console.log("No se a podido obtener la informacion");
        }
    })

}

function verAprendiz2(ruta) {
    $.ajax({
        url: ruta,
        success: function(respuesta) {
            document.getElementById('resultado').innerHTML = respuesta;
            console.log(respuesta);

        },
        error: function() {
            console.log("No se a podido obtener la informacion");
        }
    })

}