// console.log("i am working");
let loader = document.getElementById("preloader");

window.addEventListener("load", ()=>{
    loader.classList.add('disappear');
})

// JavaScript code to update the displayed value
const progressBar = document.getElementById("progress");
const selectedValue = document.getElementById("selectedValue");

progressBar.addEventListener("input", function() {
    selectedValue.textContent = progressBar.value;
});

