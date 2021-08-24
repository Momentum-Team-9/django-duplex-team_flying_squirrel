var clipboard = new ClipboardJS('#copy');

      clipboard.on('success', function (e) {
        console.log(e.text);
      });

      clipboard.on('error', function (e) {
        console.log(e);
      });