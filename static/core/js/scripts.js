
let copyButton = document.querySelector('.btn');
let clip = new ClipboardJS('.btn');
let copyBtns = document.querySelectorAll('.copy_button')

      clip.on('success', function (e) {
        console.log(e);
      });

      clip.on('error', function (e) {
        console.log(e);
      });

      copyBtns.forEach(btn=> btn.addEventListener('click',()=>{
        console.log('click')
        window.location.replace('http://127.0.0.1:8000/snippet/copy')
      }))







      console.log('HELLOOOO HI HEY')

      // const copybutton = document.querySelector('.copy_button')
      // copybutton.addEventListener('click', (event) => {
      //   event.preventDefault()
      //   const url = event.target.id 
      //   console.log(url)
      //   fetch(url, {
      //     headers: { 'X-Requested-With': 'XMLHttpRequest' },
      //   })
      //     .then((res) => res.json())
      //     .then((data) => {
            
      //       console.log(data)
      //     })
      // })