var data = "";

function send() {
  data = document.getElementById("ip").value;
}

function hide() {
  //get
  $("section,.center").toggle();
}
// get the data
var con = 0;

function callme() {
  if (con == 0) {
    // on state
    var xhr = new XMLHttpRequest();
    var url =
      "http://" +
      data +
      ":5000/work/?key=qxZVfGaLXvOaWH7W6fISF457hBAZRynlT9MVEuAqvbN6f7ZJMgvx9i9Wb8iGeAkUK28OrL5wRFWaHy48gz4o4BCAqTHnFQN8tFph&val=True";
    xhr.open("GET", url, true);
    xhr.onload = function() {
      var data = JSON.parse(xhr.responseText);
      console.log(data);
    };
    xhr.send();

    document.getElementById("demo").innerHTML = "bulb is ON";
    document.getElementById("summa").innerHTML = data;
    con += 1;
  } else if (con == 1) {
    // off state
    var xhr = new XMLHttpRequest();
    var url =
      "http://" +
      data +
      ":5000/work/?key=qxZVfGaLXvOaWH7W6fISF457hBAZRynlT9MVEuAqvbN6f7ZJMgvx9i9Wb8iGeAkUK28OrL5wRFWaHy48gz4o4BCAqTHnFQN8tFph&val=False";
    xhr.open("GET", url, true);
    xhr.onload = function() {
      var data = JSON.parse(xhr.responseText);
      console.log(data);
    };
    xhr.send();
    document.getElementById("summa").innerHTML = "No ip is set";
    document.getElementById("demo").innerHTML = "bulb is OFF";
    con -= 1;
  }
}
