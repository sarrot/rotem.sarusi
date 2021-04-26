document.getElementById("abouttxt").innerHTML = "My name is Rotem Sarusi, I'm 26 years old and originally from Metar.\n" +
    "        I am a third year student in the : Industrial Engineering and Management department in Ben Gurion University.\n" +
    "        I like to spend time with my family and friends, dive and cook.";

document.getElementById("exptxt").innerHTML = "• Call center in the economic company for the development of the string (security unit) - providing an ongoing response\n" +
    "         for the residents of the locality in the event of incidents and problems, both personal and security. Working with many factors\n" +
    "         in the security of the settlement and its maintenance."

function startTime() {
  var today = new Date();
  var h = today.getHours();
  var m = today.getMinutes();
  var s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);

  document.getElementById("time").innerHTML = h + ":" + m + ":" + s;

  var t = setTimeout(startTime, 500);
  n = new Date();
  y = n.getFullYear();
  m = n.getMonth() + 1;
  d = n.getDate();

  document.getElementById("date").innerHTML = m + "•" + d + "•" + y;
}

function checkTime(i) {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
}
setInterval(() => {
  document.title = new Date().toLocaleTimeString();
}, 1);