const Instagram = require('instagram-web-api');

const client = new Instagram({username: 'zvada53', password: 'root2827'});
(async () => {
  await client.login();
  const photos = await client.getPhotosByUsername({username: 'hoodiyalko'});

  // console.log(JSON.stringify(photos));
  const publicList = photos.user.edge_owner_to_timeline_media.edges;
  let photosList = [];
  publicList.forEach(item => {
    photosList.push({
      image: item.node.display_url,
      comment: item.node.edge_media_to_caption.edges[0].node.text
    });
  });
  console.log(photosList);
})()