const fs = require('fs');

export function publicList() {
    let fileContent = fs.readFileSync('../../public/photosFromInstagram.json', 'utf8');
    const data = JSON.parse(fileContent);
    return data;
}