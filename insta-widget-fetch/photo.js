const fs = require('fs');
let exif = require('exiftool');
fs.readFile('1.jpg', function (err, data) {
    if (err)
      throw err;
    else {
      exif.metadata(data, function (err, metadata) {
        if (err)
          throw err;
        else
          console.log(metadata);
      });
    }
  });