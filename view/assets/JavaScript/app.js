// showing navbar when click menu on mobile view
const mobile = document.querySelector('.menu-toggle');
const mobileLink = document.querySelector('.sidebar');

mobile.addEventListener("click", function (){
    mobile.clickList.toggle(is-active);
    mobileLink.classList.toggle("active");
})

// close menu when click
mobileLink.addEventListener("click", function (){
    const menuBars = document.querySelector(".is-active");
    if (window.innerWidth<=768 && menuBars){
        mobile.classList.toggle("is-active");
        mobileLink.classList.toggle("active");
    }
})

// move menu left and right when click on back  and next
var step = 100;
var stepFilter = 60;
var scrolling = true;

$(".back").bind("click", function (e){
    e.preventDefault();
    $(".hilight-wrapper").animate({
        scrollLeft: "-=" + step + "px"
    });
});

$(".next").bind("click", function (e){
    e.preventDefault();
    $(".hilight-wrapper").animate({
        scrollLeft: "-=" + step + "px"
    });
});

// when click back and next on menu filters
$(".back-menus").bind("click", function (e){
    e.preventDefault();
    $(".hilight-wrapper").animate({
        scrollLeft: "-=" + stepFilter + "px"
    });
});

$(".next-menus").bind("click", function (e){
    e.preventDefault();
    $(".hilight-wrapper").animate({
        scrollLeft: "-=" + stepFilter + "px"
    });
});


