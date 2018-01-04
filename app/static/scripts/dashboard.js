var ctxGanadores = $("#ganadores");
var ctxLugares = $("#lugares");
var ctxAnos = $("#anos");

Chart.defaults.global.defaultFontColor = "#fff";

var dynamicColors = function() {
    var r = Math.floor(Math.random() * 255);
    var g = Math.floor(Math.random() * 255);
    var b = Math.floor(Math.random() * 255);
    return "rgba(" + r + "," + g + "," + b + ", 0.4)";
}


$.getJSON('/api/graficos')
    .then(function(data){
        console.log(data.ganadores);
        cargarGanadores(data.ganadores);
        cargarLugares(data.lugares);
        cargarAnos(data.anos);
    })
    .catch(function(error){
        console.log(error);
    });


function cargarGanadores(ganadores){
    var data = [], labels = [], colors = [];
    for(var key in ganadores){
        colors.push(dynamicColors());
        if (ganadores[key] != 0){
            data.push(ganadores[key]);
            labels.push(key);
        }
    }

    var options = {
        title: {
            display: true,
            text: 'Ganadores'
        }
    };
    var data = {
        datasets: [{
            data: data,
            backgroundColor: colors,
            borderWidth: 0,
            label: "Prueba"
        }],
    
        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: labels
    };
    
    var myPieChart = new Chart(ctxGanadores,{
        type: 'pie',
        data: data,
        options: options,
        mantainAspectRatio : true,
        responsive: true
    });

}

function cargarLugares(lugares){
    var data = [], labels = [], colors = [];
    for(var key in lugares){
        colors.push(dynamicColors());
        if (lugares[key] != 0){
            data.push(lugares[key]);
            labels.push(key);
        }
    }

    var options = {
        title: {
            display: true,
            text: 'Partidas por Lugar'
        }
    };
    var data = {
        datasets: [{
            data: data,
            backgroundColor: colors,
            borderWidth: 0,
            label: "Prueba"
        }],
    
        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: labels
    };
    
    var myPieChart = new Chart(ctxLugares,{
        type: 'pie',
        data: data,
        options: options,
        mantainAspectRatio : true,
        responsive: true
    });

}

function cargarAnos(anos){
    var data = [], labels = [], colors = [];
    for(var key in anos){
        colors.push(dynamicColors());
        if (anos[key] != 0){
            data.push(anos[key]);
            labels.push(key);
        }
    }

    var options = {
        title: {
            display: true,
            text: 'Partidas por Año'
        }
    };
    var data = {
        datasets: [{
            data: data,
            backgroundColor: colors,
            borderWidth: 0,
            label: "Prueba"
        }],
    
        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: labels
    };
    
    var myPieChart = new Chart(ctxAnos,{
        type: 'pie',
        data: data,
        options: options,
        mantainAspectRatio : true,
        responsive: true
    });

}


