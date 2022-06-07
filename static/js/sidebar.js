function openNav() {
    let sideBarWidth = document.getElementById("mySidebar").style.width;
    
    if ($(window).width() < 992) {
        if (sideBarWidth !== "0px") {
            document.getElementById("mySidebar").style.width = "0px";
            document.getElementById("main").style.marginLeft = "0px";
        } else if (!sideBarWidth || sideBarWidth == "0px") {
            document.getElementById("mySidebar").style.width = "250px";
            document.getElementById("main").style.marginLeft = "0px";
        }
     }
     else {
        if (sideBarWidth !== "0px") {
            document.getElementById("mySidebar").style.width = "0px";
            document.getElementById("main").style.marginLeft = "0px";
        } else if (!sideBarWidth || sideBarWidth == "0px") {
            document.getElementById("mySidebar").style.width = "250px";
            document.getElementById("main").style.marginLeft = "250px";
        }
     }
}