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
        dataType: "json",
        success: function(respuesta) {
            var salida = "";
            salida = "<table class= 'table'>";
            $.each(respuesta, function(indice, valor) {
                salida += "<tr><td>" + indice + "</td><td>" + valor + "</td></tr>"
            });
            salida += "</table>";
            document.getElementById('resultado').innerHTML = salida;


            console.log(respuesta);
        },
        error: function() {
            document.getElementById('resultado').innerHTML = "No se a podido traer la informacion";
        }
    })

}