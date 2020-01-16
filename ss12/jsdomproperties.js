var btn = document.getElementById('btn')
btn.textContent = "stop";

var searchBar = document.getElementById("search_bar");
console.log(searchBar);
searchBar.value = "";
searchBar.style.backgroundColor = "blue";
searchBar.style.color = "white";

var menu = document.getElementById("menu");
var newli = document.createElement("li");
newli.textContent = "fries";
menu.appendChild(newli);

menu.textContent = "";
var menu = document.getElementById("menu");
var lilist = menu.getElementsByTagName("li");
var firstli = lilist[0];
firstli.remove();