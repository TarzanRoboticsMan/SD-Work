// Coby Sontag
// SoftDev pd1
// K13: Ask Circles [Change || Die]
// 2020-03-31

var pic = document.getElementById('vimage');
var clear_button = document.getElementById("clear");
var move_button = document.getElementById("move");

var animating=false;

var draw = function(e) {
  if (e.target == pic){
    var x = e.offsetX; // mouse xcor
    var y = e.offsetY; // mouse ycor
    // make circle
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", x);
    c.setAttribute("cy", y);
    c.setAttribute("r", 10);
    c.setAttribute("fill", "blue");
    //c.setAttribute("stroke", "black");
    var direction = Math.floor(Math.random() * 6.2832);
    c.setAttribute("dx", 10*Math.sin(direction));
    c.setAttribute("dy", 10*Math.cos(direction));
    c.addEventListener('click', moveSome); // add fxn
    pic.appendChild(c);
  }
};

var changeCircle = function(e) {
  if (e.target.getAttribute("fill") == "blue"){   // if circle blue
    e.target.setAttribute("fill", "cyan");
  }
  else { // if circle != blue
    e.target.setAttribute("cx", Math.floor(Math.random() * 450));
    e.target.setAttribute("cy", Math.floor(Math.random() * 450));
    e.target.setAttribute("fill", "blue");
  }
};

var clear = function(){
  while (pic.firstChild){
    pic.removeChild(pic.firstChild);
  }
  if (id!=null){
    window.cancelAnimationFrame(id);
  }
  animating = false;
}

var moveSome = function(e) {
  e.target.setAttribute("cx", parseInt(e.target.getAttribute("cx")) + parseInt(e.target.getAttribute("dx")));
  e.target.setAttribute("cy", parseInt(e.target.getAttribute("cy")) + parseInt(e.target.getAttribute("dy")));
  if (e.target.getAttribute("cx") > 490 || e.target.getAttribute("cx") < 10){
    e.target.setAttribute("dx", -1 * e.target.getAttribute("dx"))
  }
  if (e.target.getAttribute("cy") > 490 || e.target.getAttribute("cy") < 10){
    e.target.setAttribute("dy", -1 * e.target.getAttribute("dy"))
  }
}

/*var animate = function() {
  if (!animating) {animating = true;}
  while (animating){
    for each (var kid in pic.childNodes) {
      moveSome(kid);
    }
    id=window.requestAnimationFrame(animate);
  }
}*/

pic.addEventListener('click', draw);
clear_button.addEventListener('click', clear);
move_button.addEventListener('click', move);
