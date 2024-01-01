let openShopping = document.querySelector('.shopping');
let closeShopping = document.querySelector('.closeShopping');
let list = document.querySelector('.list');
let listCard= document.querySelector('.listCard');
let body = document.querySelector('body');
let total = document.querySelector('.total');
let quantity = document.querySelector('.quantity');

openShopping.addEventListener('click' , () =>{
    body.classList.add('active');
})

closeShopping.addEventListener('click' , () =>{
    body.classList.remove('active');
})

let products = [
    {
        id: 1,
        name: 'PRODUCT NAME 1' ,
        image: 'burger.png',
        price: 50
    },
    {
        id: 2,
        name: 'PRODUCT NAME 2' ,
        image: 'coffee.png',
        price: 20
    },
    {
        id: 3,
        name: 'PRODUCT NAME 3' ,
        image: 'pizza.png',
        price: 60
    },
    {
        id: 4,
        name: 'PRODUCT NAME 4' ,
        image: 'salad.png',
        price: 30
    },
    {
        id: 5,
        name: 'PRODUCT NAME 5' ,
        image: 'seafood.png',
        price: 80
    },
    {
        id: 6,
        name: 'PRODUCT NAME 6' ,
        image: 'soup.png',
        price: 20
    },
];
let listCards = [];
function initApp(){
   products.forEach((value,key) => {
       let newDiv = document.createElement('div');
       newDiv.innerHTML = `
            <img src="/view/assets/img/${value.image}"/>
            <div class="title">${value.name}></div>
            <div class="price">${value.price.toLocaleString()}></div>
       `;
       list.appendchild(newDiv);
   })
}
initApp();
