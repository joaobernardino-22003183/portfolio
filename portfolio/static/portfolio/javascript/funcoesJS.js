window.onload = function (){
    temperatura_Max()
    temperatura_Min()
    data()
    longitude()
    latitude()
    currentTime()
}

function temperatura_Max(){
    var temp_Max = document.querySelector('.temp_Max')

    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
        .then(response => response.json())
        .then(data => {
            temp_Max.innerHTML = data['data'][0]['tMax'];
        })
}

function temperatura_Min(){
    var temp_Min = document.querySelector('.temp_Min')

    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
        .then(response => response.json())
        .then(data => {
            temp_Min.innerHTML = data['data'][0]['tMin'];
        })
}

function data(){
    var dataTemp = document.querySelector('.data')

    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
        .then(response => response.json())
        .then(data => {
            dataTemp.innerHTML = data['data'][0]['forecastDate'];
        })
}

function longitude() {
    var longitude = document.querySelector('.longitude')
    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
        .then(response => response.json())
        .then(data => {
            longitude.innerHTML = data['data'][0]['longitude'];
        })
}
function latitude() {
    var latitude = document.querySelector('.latitude')
        fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
            .then(response => response.json())
            .then(data => {
                latitude.innerHTML = data['data'][0]['latitude'];
            })
}
function currentTime() {
          var date = new Date();
          var horas = date.getHours();
          var minutos = date.getMinutes();
          var segundos = date.getSeconds();

          if (horas < 10){
              horas = "0" + horas;
          }
          if (minutos < 10){
              minutos = "0" + minutos;
          }
          if (segundos < 10){
              segundos = "0" + segundos;
          }
        document.getElementById("relogio").innerText = horas + ":" + minutos + ":" + segundos;
        var tempo = setTimeout(function(){ currentTime() }, 1000);//Para que o relógio não pare
}
