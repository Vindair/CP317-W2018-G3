/* Opening functions for favourite nav bar */
function open_fav_menu() {

    var text = document.getElementById("favourite-menu-button").textContent

    if(text == "Favourites"){
    //open the favourites nav

        document.getElementById("favourite-menu-button").textContent = "Close";
        document.getElementById("favNav").style.width = "35%";
        document.getElementById("main-page").style.marginLeft = "35%";

    } else{
    //close the favourites nav

    	document.getElementById("favourite-menu-button").textContent = "Favourites";
        document.getElementById("favNav").style.width = "0";
        document.getElementById("main-page").style.marginLeft = "0";
    }

}
