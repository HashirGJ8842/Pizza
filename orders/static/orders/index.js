document.addEventListener("DOMContentLoaded", () => {
        var shopping_list = []
       document.querySelectorAll('button').forEach(button => {
            if(button.name == "navbar")
            {

            }
            else if(button.name == "main")
            {

            }
            else
            {
            button.onclick = () => {
                shopping_list.push(button.value)
                console.log(shopping_list)
                document.querySelector('#main').setAttribute('value', shopping_list)
                button.disabled = true
                p = button.parentNode
                q = p.parentNode
                q.setAttribute("style", " text-decoration: line-through ")
                q.childNodes.forEach(child => {
                    if(child.className == "price")
                    {
                        x = document.querySelector("#total_price").innerHTML
                        x = parseFloat(x)
                        y = parseFloat(child.innerHTML)
                        document.querySelector("#total_price").innerHTML = x+y
                    }
                })
            }
            }
       })
    });