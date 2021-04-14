const Instagram = require('instagram-web-api');
const fs = require('fs');

const client = new Instagram({username: 'zvada53', password: 'root2827'});
(async () => {
    await client.login();
    const photos = await client.getPhotosByUsername({username: 'hoodiyalko'});
    const publicList = photos.user.edge_owner_to_timeline_media.edges;
    let photosList = [];
    publicList.forEach(item => {
        photosList.push({
            image: item.node.display_url,
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