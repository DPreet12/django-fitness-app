const dateInput = document.getElementById("id_date");

const picker = MCDatepicker.create({
    el: '#id_date',
    dateFormat: 'yyyy-mm-dd',
    closeOnBlur: true,
   
});

dateInput.addEventListener("click", () => {
    picker.open();
})