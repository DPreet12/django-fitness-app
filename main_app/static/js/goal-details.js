const dateInput = document.getElementById("id_target_date");
const heading = document.querySelector(".script-goals")

const picker = MCDatepicker.create({
    el: '#id_target_date',
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