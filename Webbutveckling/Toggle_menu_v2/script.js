let btn = document.querySelector(".btn");
let box = document.querySelector(".box");

btn.addEventListener("click", togglebox);
function togglebox(){
    box.classList.toggle("hidden");
}