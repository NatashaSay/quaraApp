// response = jQuery.parseJSON(response);
// console.log(response);
jQuery(document).ready(function () {
  jQuery('#vmap').vectorMap({
    map: 'ukraine_ua',
    backgroundColor: '#fff',
    borderColor: '#fff',
    color: '#279fe0',
    hoverColor: '#005bbb',
    selectedColor: '#ffd500',
    enableZoom: true,
    showTooltip: true,
    //showLabels: true,
    //pins: { "pk" : "pin_for_pk", "ru" : "pin_for_ru"},
    onRegionClick: function(element, code, region)
    {
  var message = 'You clicked "'
      + region
      + '" which has the code: '
      + code.toUpperCase();

  alert(message);
    },
    onRegionOver: function(element, code, region)
    {
      if (code==63){
        document.getElementById("info").innerHTML = "Харківська область - 595";
      }
      else if (code==56){
        document.getElementById("info").innerHTML = "Рівненьська область - 987";
      }
      else if (code==07){
        document.getElementById("info").innerHTML = "Волинська область - 482";
      }
      else if (code==46){
        document.getElementById("info").innerHTML = "Львівська область - 789";
      }
      else if (code==21){
        document.getElementById("info").innerHTML = "Закарпатська область - 730";
      }
      else if (code==26){
        document.getElementById("info").innerHTML = "Івано-Франківська область - 1126";
      }
      else if (code==61){
        document.getElementById("info").innerHTML = "Тернопільська область - 1118";
      }
      else if (code==77){
        document.getElementById("info").innerHTML = "Чернівецька область - 2324";
      }
      else if (code==68){
        document.getElementById("info").innerHTML = "Хмельницька область - 178";
      }
      else if (code==18){
        document.getElementById("info").innerHTML = "Житомирська область - 523";
      }
      else if (code==05){
        document.getElementById("info").innerHTML = "Віницька область - 482";
      }
      else if (code==32){
        document.getElementById("info").innerHTML = "Київська область - 2871";
      }
      else if (code==71){
        document.getElementById("info").innerHTML = "Черкаська область - 342";
      }
      else if (code==35){
        document.getElementById("info").innerHTML = "Кіровоградська область - 420";
      }
      else if (code==51){
        document.getElementById("info").innerHTML = "Одеська область - 646";
      }
      else if (code==48){
        document.getElementById("info").innerHTML = "Миколаївська область - 223";
      }
      else if (code==65){
        document.getElementById("info").innerHTML = "Херсонська область - 161";
      }
      else if (code==74){
        document.getElementById("info").innerHTML = "Чернігівська область - 77";
      }
      else if (code==53){
        document.getElementById("info").innerHTML = "Полтавська область - 247";
      }
      else if (code==12){
        document.getElementById("info").innerHTML = "Дніпропетровська область - 731";
      }
      else if (code==23){
        document.getElementById("info").innerHTML = "Запорізька область - 329";
      }
      else if (code==43){
        document.getElementById("info").innerHTML = "АР Крим - 731";
      }
      else if (code==59){
        document.getElementById("info").innerHTML = "Сумська область - 154";
      }
      else if (code==09){
        document.getElementById("info").innerHTML = "Луганська - 42";
      }
      else if (code==14){
        document.getElementById("info").innerHTML = "Донецька область - 100";
      }


      else{
        document.getElementById("info").innerHTML = "";
      }
  var message = 'You clicked "'
      + region
      + '" which has the code: '
      + code.toUpperCase();

    },
  });
});
