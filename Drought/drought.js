function clear_page() {
    document.getElementsByClassName('_li')[0] = document.getElementsByClassName('_li')[0].removeChild(document.getElementById('pagelet_bluebar'));
    document.getElementsByClassName('_li')[0] = document.getElementsByClassName('_li')[0].removeChild(document.getElementById('globalContainer'));
    document.getElementsByClassName('_li')[0] = document.getElementsByClassName('_li')[0].removeChild(document.getElementById('pagelet_sidebar'));
};

function add_image() {
    var mydiv = document.getElementsByClassName('_li');
    var newcontent = document.createElement('div');
    newcontent.innerHTML = '<img style="-webkit-user-select: none; cursor: -webkit-zoom-in;" src="http://i.imgur.com/wvunc.jpg" width="1280">';

    while (newcontent.firstChild) {
        mydiv[0].appendChild(newcontent.firstChild);
    }
};

//chrome.browserAction.onClicked.addListener(clear_page);
//chrome.browserAction.onClicked.addListener(add_image);
clear_page();
add_image();

