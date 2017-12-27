
function fillManosGrid(){
    var divManoRow = '<div class="manos-grid-row"><input class="jugador-input" type="text" name="jugador" placeholder="Jugador"><input class="manos-input" type="text" name="manos" placeholder="Manos"></div>';
    var cantJugadores = $("#cant-jugadores").val();

    $(".manos-grid").html("").hide();
    for(var i=0; i < cantJugadores; i++) $(".manos-grid").append(divManoRow);
    $(".manos-grid").append("<button class='btn-cargar' onclick='postJuego()'>Cargar</button>").fadeIn(700);
} 


function postJuego(){

    var jsonBodyLapo = {
        juego: [],
        lugar: $("#lugar").val(),
        fecha: {
            dia: $("#fecha-dia").val(),
            mes: $("#fecha-mes").val(),
            ano: $("#fecha-ano").val()
        }
    };

    var rows = $(".manos-grid-row");
    console.log(rows);
   
    for (var i=0; i<rows.length; i++){
        console.log(rows[i].children[0].value);

        var juegoJSON = {};
        juegoJSON.jugador = rows[i].children[0].value;
        juegoJSON.manos = rows[i].children[1].value.split(',');
        jsonBodyLapo.juego.push(juegoJSON);

    }

    console.log(jsonBodyLapo);
   
    $.ajax({
        url: '/juegos/new'
    ,   type: 'POST'
    ,   contentType: 'application/json'
    ,   data: JSON.stringify(jsonBodyLapo) //stringify is important
    })
    .done(function(data){
        console.log(data);
    });


}






