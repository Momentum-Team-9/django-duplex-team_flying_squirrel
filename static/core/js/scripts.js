
const copyBtns = [...document.getElementsByClassName('copy_button')]
console.log(copyBtns)

let previous = null

copyBtns.forEach(btn=> btn.addEventListener('click',e=>{
    const snippetBox = e.target.parentElement.parentElement;
    const snippet = btn.getAttribute('data-id')
    const copyURL =`/snippet/${e.target.id}/copy`
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