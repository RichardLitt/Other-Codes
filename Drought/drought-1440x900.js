// Get rid of the sections you don't like
function clear_page() {
    // I'm personally not a fan of the blue Status bar
    document.getElementsByClassName('_li')[0] = document.getElementsByClassName('_li')[0].removeChild(document.getElementById('pagelet_bluebar'));
    // Or the rest of the page, to be honest
    document.getElementsByClassName('_li')[0] = document.getElementsByClassName('_li')[0].removeChild(document.getElementById('globalContainer'));
    // The sidebar might be nice, if you want to know which friends are on.
    // Of course you can detach the chat bar, in the lower right corner. I suggest doing this, as it makes it easier, and you can have it there, but not be distracted by it all of the time. If you don't detach it, you can't see friends - which might be another good option. To re-enable, simply disable the extension, and refresh. 
    document.getElementsByClassName('_li')[0] = document.getElementsByClassName('_li')[0].removeChild(document.getElementById('pagelet_sidebar'));
    // I don't even like the translation globe. Who speaks in other languages?
    // This seems to break it. Needs to be fixed.
    // document.getElementsByClassName('clearfix nubContainer rNubContainer')[0] = document.getElementsByClassName('clearfix nubContainer rNubContainer')[0].removeChild(document.getElementById('fbTranslationsNub'));
};

function add_image() {
    var mydiv = document.getElementsByClassName('_li');
    var newcontent = document.createElement('div');
    // Edit the src to point to a wallpaper you, you know, like.
    newcontent.innerHTML = '<div style="background-image:url(http://i.imgur.com/yXABw.jpg);height:950px;background-size:contain;"></div>';


    while (newcontent.firstChild) {
        mydiv[0].appendChild(newcontent.firstChild);
    }
};

// And we're done here, folks.
clear_page();
add_image();

