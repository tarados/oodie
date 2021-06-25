require('dotenv').config();
const Instagram = require('instagram-web-api');
const fs = require('fs');
const request = require('request');

const download = (url, path, callback) => {
    request.head(url, (err, res, body) => {
        request(url)
            .pipe(fs.createWriteStream(path))
            .on('close', callback)
    })
};

const client = new Instagram({username: 'zvada53', password: 'root2827'});

(async () => {
    await client.login();
    const photos = await client.getPhotosByUsername({username: 'hoodiyalko'});
    const publicList = photos.user.edge_owner_to_timeline_media.edges;
    let photosList = [];
    publicList.forEach((item, index) => {
        const url = item.node.thumbnail_src;
        const path = `image${index}.jpeg`;
        download(url, process.env.PATH_FILE_IMAGE + path, () => {
            console.log('✅ Done!')
        });
        photosList.push({
            image: process.env.SITE_URL + process.env.PATH_MEDIA + path,
            comment: item.node.edge_media_to_caption.edges[0].node.text,
            shortcode: item.node.shortcode
        });
    });
    let file = fs.createWriteStream(process.env.RESULT_FILE);
    file.on('error', function (err) { /* error handling */
    });
    let jsonData = JSON.stringify(photosList);
    file.write(jsonData);
    file.end();
})();
