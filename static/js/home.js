function addProductToCart(trigger) {
    cartProducts = document.getElementsByClassName("cart-item");
    product = trigger.parentNode.parentNode.childNodes[1].childNodes[1].innerHTML;
    price = trigger.parentNode.childNodes[1].childNodes[1].innerHTML;
    exists = false;
    Array.from(cartProducts).forEach(cartItem => {
        itemName = cartItem.childNodes[0].innerHTML;
        if(itemName == product) {
            itemPrice = cartItem.childNodes[2].childNodes[0].innerHTML;
            if(itemPrice == price) {
                itemQuantitySpan = cartItem.childNodes[1];
                itemQuantity = +(itemQuantitySpan.innerHTML) + 1;
                itemQuantitySpan.innerHTML = itemQuantity;
                exists = true;
                return; 
            }
        } 
    });
    if(!exists) {
        cart = document.getElementById("cart-body");
        cart.appendChild(getCartHolder(product, price));
    }
    updateCart();
    showFeedback('success', 'Producto añadido correctamente', false, 700, "rgba(80,80,80,0.4)")
}

function removeProductFromCart(trigger) {
    itemQuantitySpan = trigger.parentNode.childNodes[1];
    itemQuantity = +(itemQuantitySpan.innerHTML) - 1;
    itemQuantitySpan.innerHTML = itemQuantity;
    if(itemQuantity == 0) {
        trigger.parentNode.parentNode.removeChild(trigger.parentNode)
    }
    updateCart();
}

function updateCart() {
    cartProducts = document.getElementsByClassName("cart-item");
    if(cartProducts.length == 0) {
        document.getElementById("cart-header").style = "display: none !important;"
        document.getElementById("cart-footer").style = "display: none !important;"
        document.getElementById("cart-body-empty").style = "display: flex !important"
    } else {
        document.getElementById("cart-header").style = "display: flex !important;"
        document.getElementById("cart-footer").style = "display: flex !important;"
        document.getElementById("cart-body-empty").style = "display: none !important"
    }
    updateTotal();
}

function updateTotal() {
    cartProducts = document.getElementsByClassName("cart-item");
    total = 0.00;
    Array.from(cartProducts).forEach(cartItem => {
        itemQuantity = parseFloat(cartItem.childNodes[1].innerHTML);
        itemPrice = parseFloat(cartItem.childNodes[2].childNodes[0].innerHTML.replace(",", "."));
        total += itemQuantity * itemPrice;
    });
    document.getElementById("total-price").innerHTML = (Math.round(total * 100) / 100).toFixed(2).replace(",", ".");
}

function getCartHolder(name, price) {
    holder = create("div", "", "row cart-item dropdown-item d-flex align-items-center m-0");
    start = create("p", name, "m-0 col-5 text-truncate text-center");
    mid = create("p", "1", "m-0 px-1 col-3 text-center");
    end = create("p", "<span>" + price + "</span>€", "m-0 col-3 text-center")
    button = create("button", '<i class="fas fa-trash-alt">', "btn btn-outline-danger col-1");
    button.setAttribute("onclick", "removeProductFromCart(this)");
    holder.appendChild(start);
    holder.appendChild(mid);
    holder.appendChild(end);
    holder.appendChild(button);
    return holder;
}

function create(type, inner="", classes="") {
    element = document.createElement(type);
    if(inner.length > 0) {
        element.innerHTML = inner;
    }
    if(classes.length > 0) {
        element.setAttribute("class", classes);
    }
    return element;
}

function onSuccessOnClickBuyButton(data) {
    cartProducts = document.getElementsByClassName("cart-item");
    Array.from(cartProducts).forEach(cartItem => {
        cartItem.parentNode.removeChild(cartItem);
    });
    updateCart();
    $('#cart-trigger').removeClass('show');
    $('#cart').removeClass('show');
    showFeedback('success', 'Pedido realizado correctamente', false, 2000, "rgba(80,80,80,0.4)")
}

function onClickBuyButton() {
    cartProducts = document.getElementsByClassName("cart-item");
    products = [];
    quantities = [];
    prices = [];
    total = document.getElementById("total-price").innerHTML + '€';
    Array.from(cartProducts).forEach(cartItem => {
        itemName = cartItem.childNodes[0].innerHTML;
        itemQuantity = cartItem.childNodes[1].innerHTML;
        itemPrice = cartItem.childNodes[2].childNodes[0].innerHTML.replace(",", ".") + '€';
        products.push(itemName);
        quantities.push(itemQuantity);
        prices.push(itemPrice);
    });
    data = {
        'products': products,
        'quantities': quantities,
        'prices': prices,
        'total': total
    }
    ajaxToPostData('transaction/', data, onSuccessOnClickBuyButton);
}

document.getElementById("cart").addEventListener('click', function (event) {
    event.stopPropagation();
});
