// selction nessessary elements to make the website good
const light =  document.querySelector(".light");


// adding event listener to each element
light.addEventListener("click", () => {
    document.body.classList.toggle("active");
})
