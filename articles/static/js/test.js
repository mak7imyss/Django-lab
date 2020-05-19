"use strict";
let foldBtns = document.getElementsByClassName("fold-button");
for (let i = 0; i < foldBtns.length; i++) {
  foldBtns[i].addEventListener("click", function (event) {
    console.log(event.target.parentNode.parentNode.parentNode.nextElementSibling.className)
    if (event.target.parentNode.parentNode.parentNode.nextElementSibling.className == "box") {
      event.target.parentNode.parentNode.parentNode.nextElementSibling.className = "no-box";
      event.target.innerHTML = "Раскрыть";
      console.log('True', event.target.parentElement.className);
      console.log(event.target.parentElement.className);
    } else if (event.target.parentNode.parentNode.parentNode.nextElementSibling.className == "no-box") {
      event.target.parentNode.parentNode.parentNode.nextElementSibling.className = "box";
      event.target.innerHTML = "Скрыть";
      console.log('False', event.target.parentElement.className);
      console.log(event.target.parentElement.className);
    }
  });
}

// let foldBtns = document.getElementsByClassName("fold-button");
// for (let i = 0; i<foldBtns.length; i++){ 
//     foldBtns[i].addEventListener("click", function(event) {
//         event.target
//         .parentElement
//         .getElementsByClassName('article-author')[0]
//         .style.display = "none";
//         event.target
//         .parentElement
//         .getElementsByClassName('article-created-date')[0]
//         .style.display = "none";
//         event.target
//         .parentElement
//         .getElementsByClassName('article-text')[0]
//         .style.display = "none";
//         e.target.innerHTML = "развернуть";
        

        // if (event.target.parentElement.className == "fold-button"){
            // event.querySelectorAll('tablevent.form-post tr.fold-table')}
        //     event.getElementById("fold-table").className = 'fold-table-none';
        //     event.target.value = 'Раскрыть';
        // }
        // else if(event.target.parentElement.className == 'fold-table-none'){
        //     event.getElementById("fold-table-none").className = 'fold-table';
        //     event.target.value = 'Раскрыть';
        // }
        // if (event.target.parentElement.className == "form-post"){
        //     let a = 'True';
        // }
        // else {
        //     a = 'False';}
//         consolevent.log(event.target.querySelectorAll('tablevent.form-post tr.fold-table'))
//     });
// }