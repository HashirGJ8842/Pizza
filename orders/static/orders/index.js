document.addEventListener("DOMContentLoaded", () => {
       document.querySelectorAll('button').forEach(button => {
            button.onclick = () => {
                button.disabled = true
                p = button.parentNode
                q = p.parentNode
                console.log(q.nodeName)
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
       })
    });