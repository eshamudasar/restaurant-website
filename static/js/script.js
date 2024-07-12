document.addEventListener('DOMContentLoaded', () => {
    const cartElement = document.getElementById('cart');
    const sidebarCartElement = document.getElementById('sidebar-cart');
  
    function updateCartUI() {
      const cartItems = session['cart'];
      const total_price = 0;
      cartItems.forEach((item) => {
        total_price += item.price * item.quantity;
      });
      sidebarCartElement.querySelector('p').textContent = `Total: £${total_price}`;
    }
  
    function addToCart(itemId, itemName, itemPrice) {
      fetch('/cart', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ item_id: itemId, item_name: itemName, item_price: itemPrice })
      })
      .then(response => response.json())
      .then(data => {
        updateCartUI();
        const itemElement = cartElement.querySelector(`[data-item-id="${itemId}"]`);
        if (itemElement) {
          const quantityElement = itemElement.querySelector('td:nth-child(2)');
          quantityElement.textContent = `x${data.quantity}`;
        } else {
          const newRow = document.createElement('tr');
          newRow.innerHTML = `
            <td>${itemName}</td>
            <td>x${data.quantity}</td>
            <td>£${itemPrice}</td>
            <td><button class="remove-from-cart" data-item-id="${itemId}">Remove</button></td>`;
            cartElement.appendChild(newRow);
        }
      })
      .catch(error => console.error('Error adding item to cart:', error));
    }
  
    document.querySelectorAll('.add-to-cart').forEach(button => {
      button.addEventListener('click', () => {
        const itemId = button.dataset.itemId;
        const itemName = button.dataset.itemName;
        const itemPrice = button.dataset.itemPrice;
        addToCart(itemId, itemName, itemPrice);
      });
    });
  
    document.querySelectorAll('.remove-from-cart').forEach(button => {
      button.addEventListener('click', () => {
        const itemId = button.dataset.itemId;
        fetch('/cart/remove', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ item_id: itemId })
        })
       .then(response => response.json())
       .then(data => {
          // Remove the item from the cart UI
          const itemElement = cartElement.querySelector(`[data-item-id="${itemId}"]`);
          if (itemElement) {
            itemElement.remove();
          }
        })
        .catch(error => console.error('Error removing item from cart:', error));
    });
  });

document.getElementById('checkout-form').addEventListener('submit', (event) => {
    event.preventDefault();
    fetch('/checkout', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('order-status').textContent = `Order placed successfully! Order ID: ${data.orderId}`;
        cartElement.innerHTML = ''; // Clear the cart UI
    })
    .catch(error => console.error('Error during checkout:', error));
  });
});  