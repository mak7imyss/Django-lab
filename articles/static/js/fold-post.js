"use strict";
let foldBtns = document.getElementsByClassName("fold-button");
for (let i = 0; i < foldBtns.length; i++) {
  foldBtns[i].addEventListener("click", function (event) {
    event.target.onmouseover = () => event.target.style.color = "red";
    if (event.target.parentNode.parentNode.parentNode.nextElementSibling.className == "box") {
      event.target.parentNode.parentNode.parentNode.nextElementSibling.className = "no-box";
      event.target.style.color = "white"      
      event.target.onmouseout = () => event.target.style.color = "white";
      event.target.innerHTML = "Раскрыть";
    } else if (event.target.parentNode.parentNode.parentNode.nextElementSibling.className == "no-box") {
      event.target.parentNode.parentNode.parentNode.nextElementSibling.className = "box";
      event.target.style.color = "orange"
      event.target.onmouseout = () => event.target.style.color = "orange";
      event.target.innerHTML = "Скрыть";

    }
  });
}