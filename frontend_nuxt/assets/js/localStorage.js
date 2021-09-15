export function getItems() {
    let items = localStorage.getItem('cart');
    if (items) {
        items = JSON.parse(items);
    } else {
        items = [];
    }
    return items
}

export function clearLocalStorage() {
    localStorage.removeItem("cart");
}

export function setItems(items) {
    items = JSON.stringify(items);
    localStorage.setItem('cart', items);
}