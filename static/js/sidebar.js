function openNav() {
    let sideBarWidth = document.getElementById("mySidebar").clientWidth;
    let sideBar = document.getElementById("mySidebar");
    let main = document.getElementById("main")
    
    if ($(window).width() < 992) {
        if (sideBarWidth == 0) {
            sideBar.style.width = "250px";
            main.style.marginLeft = "0px";
        } else if (sideBarWidth != 0) {
            sideBar.style.width = "0px";
            main.style.marginLeft = "0px";
        }
     }
     else {
        if (sideBarWidth !== 0) {
            sideBar.style.width = "0px";
            main.style.marginLeft = "0px";
        } else if (!sideBarWidth || sideBarWidth == 0) {
            sideBar.style.width = "250px";
            main.style.marginLeft = "250px";
        }
     }
}