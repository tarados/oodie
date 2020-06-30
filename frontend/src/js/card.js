export function getItems() {
    let items = localStorage.getItem('card');
    if (items) {
        items = JSON.parse(items);
    } else {
        items = [];
    }
    return items
}

export function clearLocalStorage() {
    localStorage.removeItem("card");
}

export function setItems(items) {
    items = JSON.stringify(items);
    localStorage.setItem('card', items);
}