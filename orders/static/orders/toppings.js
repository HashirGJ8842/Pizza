document.addEventListener("DOMContentLoaded", () => {
        var topping_list = []
       document.querySelectorAll('select').forEach(select => {
            select.onchange = () => {
                id = select.selectedIndex
                topping_list.push(select.value)
                console.log(topping_list)
                document.querySelector('#main').setAttribute('value', topping_list)
                select.disabled = true
            }
       })
    });