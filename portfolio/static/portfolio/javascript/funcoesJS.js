function temperatura_Max(){
    var temp_Max = document.querySelector('.temp_Max')

    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
        .then(response => response.json())
        .then(data => {
            temp_Max.innerHTML = data['data'][0]['tMax'];
        })

    return temp_Max
}
temperatura_Max()
function temperatura_Min(){
    var temp_Min = document.querySelector('.temp_Min')

    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
        .then(response => response.json())
        .then(data => {
            temp_Min.innerHTML = data['data'][0]['tMin'];
        })

    return temp_Min
}
temperatura_Min()
function data(){
    var dataTemp = document.querySelector('.data')

    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
        .then(response => response.json())
        .then(data => {
            dataTemp.innerHTML = data['data'][0]['forecastDate'];
        })
}
data()
/*
* <p>No dia <b class="data"></b> na cidade de Lisboa, a temperatura máxima é de
        <b class="temp_Max"></b>ºC e a temperatura mínima é de <b class="temp_Min"></b>ºC.</p>

  <script>
      var dataTemp = document.querySelector('.data')
      var temp_Max = document.querySelector('.temp_Max')
      var temp_Min = document.querySelector
      fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
          .then(response => response.json())
          .then(data => {
              dataTemp.innerHTML = data['data'][0]['forecastDate'];
              temp_Max.innerHTML = data['data'][0]['tMax'];
              temp_Min.innerHTML = data['data'][0]['tMin'];
          })
  </script>
* */