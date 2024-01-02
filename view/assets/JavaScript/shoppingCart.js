let cartItems = [];
let total = 0;

function addToCart(name, price, image) {
    const product = {
        name: name,
        price: price,
        image: image
    };

    cartItems.push(product);
    total += product.price;

    updateCartUI();
}

function removeFromCart(index) {
    const removedItem = cartItems.splice(index, 1)[0];
    total -= removedItem.price;

    updateCartUI();
}

function updateCartUI() {
    const cartElement = document.getElementById("cart");
    const cartItemsElement = document.getElementById("cart-items");
    const totalElement = document.getElementById("total");

    // Clear existing cart items and total
    cartItemsElement.innerHTML = "";
    totalElement.innerHTML = "";

    // Populate cart items
    cartItems.forEach((item, index) => {
        const listItem = document.createElement("li");
        listItem.classList.add("cart-item");

        listItem.innerHTML = `
           <span>${item.name}</span>
            <span>$${item.price.toFixed(2)}</span>
            <button onclick="removeFromCart(${index})">Remove</button>
        `;

        cartItemsElement.appendChild(listItem);
    });

    // Update total
    totalElement.innerHTML = `<p>Total: $${total.toFixed(2)}</p>`;

    // Append total section to the cart
    cartElement.appendChild(totalElement);
}

function toggleSidebar() {
            var sidebar = document.querySelector('.right-sidebar');
            var content = document.querySelector('content');

            if (right-sidebar.style.right === "0px") {
                sidebar.style.right = "-250px";
                content.style.marginRight = "0";
            } else {
                sidebar.style.right = "0";
                content.style.marginRight = "250px";
            }
        }



