

var clipboard = new ClipboardJS('#event.target.id');
    
      clipboard.on('success', function (e) {
        console.log(e.text);
      });

      clipboard.on('error', function (e) {
        console.log(error);
      });







      console.log('HELLOOOO HI HEY')

      const copybutton = document.querySelector('.copy_button')
      copybutton.addEventListener('click', (event) => {
        event.preventDefault()
        const url = event.target.id 
        console.log(url)
        fetch(url, {
          headers: { 'X-Requested-With': 'XMLHttpRequest' },
        })
          .then((res) => res.json())
          .then((data) => {
            
            console.log(data)
          })
      })