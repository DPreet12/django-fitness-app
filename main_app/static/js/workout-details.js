const dateInput = document.getElementById("id_date");
const heading = document.querySelector(".script-workouts")

const picker = MCDatepicker.create({
    el: '#id_date',
    dateFormat: 'yyyy-mm-dd',
    closeOnBlur: true,
   
});

dateInput.addEventListener("click", () => {
    picker.open();
})

const typed = new Typed( heading, {
    strings: [heading.textContent],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 500,
    loop: true,
    showCursor: false,
})