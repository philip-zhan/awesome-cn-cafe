var speedTest = require('speedtest-net');
var test = speedTest({maxTime: 5000});

test.on('result', url => {
    if (!url) {
      console.log('Could not successfully post test results.');
    } else {
      console.log('Test result url:', url);
    }
});

test.on('data', data => {
    console.dir(data);
});

test.on('error', err => {
    console.error(err);
});
