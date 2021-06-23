function toggleCart() {

}

function addProductToCart(trigger) {
    id = trigger.parentNode.parentNode.childNodes[1].innerHTML
    name = trigger.parentNode.parentNode.childNodes[3].innerHTML
    price = trigger.parentNode.parentNode.childNodes[7].innerHTML
    console.log("Added", id, name, price)
}

function removeProductFromCart(trigger) {
    id = trigger.parentNode.parentNode.childNodes[1].innerHTML
    name = trigger.parentNode.parentNode.childNodes[3].innerHTML
    price = trigger.parentNode.parentNode.childNodes[7].innerHTML
    console.log("Removed", id, name, price)
}