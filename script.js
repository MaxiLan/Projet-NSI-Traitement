var bouton1 = document.getElementById("bouton1");
var bouton2 = document.getElementById("bouton2");

bouton1.addEventListener("click",page2);
bouton2.addEventListener("click",page1);

function page1() {
  window.location.href = 'page_web1.html'
}
function page2() {
  window.location.href = 'page_web2.html'
}
