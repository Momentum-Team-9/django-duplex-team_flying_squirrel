
let previous = null

const copyBtns = [...document.getElementsByClassName('copy_button')]
console.log(copyBtns)
copyBtns.forEach(btn=> btn.addEventListener('click',e=>{

    const copyURL =`/snippet/${e.target.id}/copy`
    btn.textContent = 'Copied to Profile'

    if (previous){
        previous.textContent = 'Copy Snippet'
    }
    previous = btn

    fetch(copyURL, {
      headers: { 'X-Requested-With': 'XMLHttpRequest' },
        })
        .then((res) => res.json())
        .then((data) => {
          
          console.log(data)
          
    })}))



// Script to toggle mobile nav view

const burgerIcon = document.getElementById('burger')
const navbarMenu = document.getElementById('nav-links')

burgerIcon.addEventListener('click', () => {
  navbarMenu.classList.toggle('is-active')
})