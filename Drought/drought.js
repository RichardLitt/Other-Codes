function removeElement(parentDiv, childDiv){
     if (childDiv == parentDiv) {
          alert("The parent div cannot be removed.");
     }
     else if (document.getElementById(childDiv)) {     
          var child = document.getElementById(childDiv);
          var parent = document.getElementsByClassName(parentDiv);
          parent[0].removeChild(child);
     }
     else {
          alert("Child div has already been removed or does not exist.");
          return false;
     }
}

function doMagic() {
    removeElement('-cx-PRIVATE-fbLayout__root','pagelet_bluebar');  
    //removeElement('-cx-PRIVATE-fbLayout__root','globalContainer');
};

chrome.browserAction.onClicked.addListener(doMagic);
