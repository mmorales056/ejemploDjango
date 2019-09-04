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

function graficos() {
    var ctx = document.getElementById('myChart');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [{
                label: '# of Votes',
                data: [12, 19, 3, 5, 2, 3],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}