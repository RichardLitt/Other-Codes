// Get rid of the sections you don't like
function clear_page() {
    // I'm personally not a fan of the blue Status bar
    document.getElementsByClassName('_li')[0] = document.getElementsByClassName('_li')[0].removeChild(document.getElementById('pagelet_bluebar'));
    // Or the rest of the page, to be honest
    document.getElementsByClassName('_li')[0] = document.getElementsByClassName('_li')[0].removeChild(document.getElementById('globalContainer'));
    // The sidebar might be nice, if you want to know which friends are on.
    document.getElementsByClassName('_li')[0] = document.getElementsByClassName('_li')[0].removeChild(document.getElementById('pagelet_sidebar'));
};

function add_image() {
    var mydiv = document.getElementsByClassName('_li');
    var newcontent = document.createElement('div');
    // Edit the src to point to a wallpaper you, you know, like.
    newcontent.innerHTML = '<div style="background-image:url(http://i.imgur.com/wvunc.jpg);height:850px;background-size:contain;"></div>';

    while (newcontent.firstChild) {
        mydiv[0].appendChild(newcontent.firstChild);
    }
};

// And we're done here, folks.
clear_page();
add_image();

