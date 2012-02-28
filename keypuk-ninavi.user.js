// Keypuk nìNa'vi! v .1
// Translated and edited by Richard Littauer
// No (c) on the translations, whatsoever. 
// https://github.com/RichardLitt/Other-Codes/blob/master/keypuk-ninavi.user.js
// 
// Based on:
// Secwepemc Facebook!
// version 0.1 BETA!
// 2010-08-25
// Copyright (c) 2010, Neskie Manuel
// Released under the GPL license
// http://www.gnu.org/copyleft/gpl.html
//
// --------------------------------------------------------------------
//
// This is a Greasemonkey user script.  To install it, you need
// Greasemonkey 0.3 or later: http://greasemonkey.mozdev.org/
// Then restart Firefox and revisit this script.
// Under Tools, there will be a new menu item to "Install User Script".
// Accept the default configuration and install.
//
// To uninstall, go to Tools/Manage User Scripts,
// select "Secwepemctsin Facebook", and click Uninstall.
//
// To install on Chrome, just drag it into a window. It'll work.
//
// --------------------------------------------------------------------
//
// ==UserScript==
// @name          Nìna'vi Facebook
// @namespace     https://github.com/RichardLitt/Other-Codes
// @description   script to change the Facebook
// @include       http://www.facebook.com/*
// ==/UserScript==

//Array of words to change.
var es = new Array();
es["Home"] = "Kelutral";
es["No"] = "Kehe";
es["Yes"] = "Srane";
es["Maybe"] = "Kxawm";
es["News Feed"] = "Fmawnä Payfya";
es["Friends"] = "Eylan";
es["Like"] = "Fì'u sunu";
es["Unlike"] = "Fì'u ke sunu";
es["Comment"] = "Plltxe";
es["Books"] = "Fuk";
es["Female"] = "Tuté";
es["Male"] = "Tutan";
es["Say hello."] = "Plltxe san kaltxì";
es["Say hi."] = "Plltxe san kaltxì";
es["on Friday."] = "Trrpuvemì.";
es["on Saturday."] = "Trrkivemì.";
es["Tomorrow"] = "Trray";
es["Today"] = "Fìtrr";
es["Yesterday"] = "Trram";
es["What are you planning?"] = "Pekemìt ngal hawl?";
es["Where?"] = "Peseng?";
// es["Mobile Phone"] = "K̓woyí7se	T̓e Xqweltálkweten";
// es["Phone"] = "Xqweltálkweten";
es["Children:"] = "Eveng:";
es["Birthday:"] = "Ftxozä:";
es["See All"] = "Tse'a Nìwotx";
es["Who's invited?"] = "Pesu ziva'u?";
//es["What's on your mind?"] = "’ìn ngeyä fyape nìfkrr?";
//es["October"] = "Pesllwélsten";
es["This Month"] = "Fìvospxì";
es["Share"] = "Käsrin fì'ut";
es["shared a"] = "käsrin";
es["via"] = "ìlä";
es["Friday"] = "Trrpuve";
es["Monday"] = "Trrmuve";
es["Tuesday"] = "Trrpxeyve";
es["Wednesday"] = "Trrtsìve";
es["Thursday"] = "Trrmrrve";
es["Saturday"] = "Trrkive";
es["Sunday"] = "Trr'awve";
es["minutes ago"] = "ayswawkam";
es["Who are you with?"] = "Pesumì nga lu?";
es["Where are you?"] = "Tsengpe nga lu?";
es["via Twitter"] = "ìlä Yayotsyìp"; 
es["Post"] = "Fpe'";
es["Upload photo/video"] = "Fpe' rusikxa relit/relit";
es["Create photo album"] = "Relä pukit ngop"; 
es["Create event"] = "Tìlenit ngop";
es["Update status"] = "Latem tìfkeytokit";
es["Add photo/video"] = "Fpe' rusikxa relit/relit";
es["Ask question"] = "Pawm fì'ut";
// es["SORT"] = "Kame";
es["Top stories"] = "Vurä fäpa";
es["Most Recent"] = "Vur asok";
es["Account Settings"] = "Fìpoä Sìfkeytok";
es["Privacy Settings"] = "Le'aw 'awpoä Sìfkeytok";
es["Log out"] = "Hum";
es["Help"] = "Srung";
es["and"] = "sì";
es["Photos"] = "Ayrel";
es["Music"] = "Pamtseo";
es["Notes"] = "Famreltsyìp";
// es["Questions"] = "";
// es["Links"] = "";
// es["Apps and Games"] = "";
// es["Apps"] = "";
// es["Pages"] = "";
// es["Groups"] = "";
// es["Events"] = "";
// es["Messages"] = "";
// es["Favourites"] = "";
es["Facebook"] = "Keypuk";
es["Use webcam"] = "Sar kusrrnekxti rusikxa ayrelä";
es["English (US)"] = "'Ìnglìsì";
es["English (UK)"] = "'Ìnglìsì";
es["Privacy"] = "Kxukea Säomum";
es["Terms"] = "Lawa Aylì'u";
es["More"] = "Nì'ul";
es["About"] = "Teri";
es["Advertising"] = "Txanewa Lusawk";
es["Careers"] = "Fnetxintìn";
es["Create a Page"] = "Ngop Rìkti";
es["Developers"] = "Ayngopyu";
// es["Add to my page's favourites"] = "";
es["Get updates via RSS"] = "Tel ayfmawnit ìlä RSS";
// es["Report Page"] = "";
es["like this"] = "fì'u sunu";
es["talking about this"] = "";
es["Wall"] = "'Awkx";
es["Info"] = "Säomum";
es["Friend activity"] = "Tìn eylanä";
es["Photos"] = "Ayrel";
es["See all"] = "Kame nìwotx";
// es["Recommended Pages"] = "";
es["Discover new games"] = "Run mipa ayuvanti";
// es["There are no more posts to show."] = "";
es["Find friends"] = "Run eylanit";
es["Product/Service"] = "Kìte'e";
es["Lives in"] = "Kelku si mì";
es["In a relationship with"] = "Muntxa susi mì";
es["Life event"] = "Tìlen tìreyä";
es["Place"] = "Tsenge";
es["Photo"] = "Rel";
es["Status"] = "Tìfkeytok";
// es["mutual friends"] = "";
// es["Update info"] = "";
es["Activity log"] = "Sìnä 'ok";
es["Likes"] = "Susunua ayfì'u";
es["Map"] = "Atxkxerel";
es["Born"] = "'Amongokx";
es["Richard Littauer"] = "Skxawng Makto alu Taronyu";
es["See friendship"] = "Tse'a tì'eylanti";
es["Sponsored"] = "Awneyk";
es["Create an advert"] = "Ngop nusewìt";
es["Subscriptions"] = "Tsawne'a";
es["More Recent Activity"] = "";
es["View As..."] = "Tse'a tengfya...";
// es["Add a badge to your site"] = "";
es["Edit"] = "Latem";
es["Timeline"] = "Krrä Payfya";
es["Now"] = "Set";
es["Use Facebook as:"] = "Sar Keypukit tengfya:";
// es["Search"] = "Fwew"; // This breaks the top search bar, but not the chat search function.
es["Translations"] = "";
es["Friend requests"] = "'Eylan ätxäle";
es["No new requests"] = "Kea mipa ayätxäle";
es["See all friend requests"] = "Tse'a eylanìri ayätxäleti nìwotx";
es["Messages"] = "'Upxare";
es["Send a new message"] = "Fpe' mipa 'upxareti";
es["See all messages"] = "Tse'a upxare nìwotx";
es["Notifications"] = "Ayfmawn";
es["See all notifications"] = "Tse'a ayfmawnit nìwotx";
es["Post"] = "Plltxe";
es["Cancel"] = "Ftang";
//es["Select an image or video file on your computer"] = "";
//es["Choose file"] = "";
//es["No file chosen"] = "";
es["Add year"] = "Sung zìsìtit";
es["January"] = "'Awve vospxì";
es["February"] = "Muve vospxì";
es["March"] = "Pxeyve vospxì";
es["April"] = "Tsìve vospxì";
es["May"] = "Mrrve vospxì";
es["June"] = "Puve vospxì";
es["July"] = "Kive vospxì";
es["August"] = "Volve vospxì";
es["September"] = "Volawve vospxì";
es["October"] = "Vomuve vospxì";
es["November"] = "Vopeyve vospxì";
es["December"] = "Vosìve vospxì";
es["Change Cover"] = "Latem Keyit";
es["Edit Profile Picture"] = "Latem Txina Key Relä";
es["Chat Sounds"] = "Puslltxe Fam";
es["Advanced Settings"] = "Ngäzìka Sìfkeytok";
es["Go offline"] = "Kämakto!";
es["Hide Sidebar"] = "Wan Pa'oä Payfya";
es["Subscribed"] = "Tsuse'a";
es["More stories"] = "Nì'ul ayvul";
es["Edit options"] = "Latem sìftxeyt";
es["Find friends"] = "Fwew eylanit";

//Basic Tag altering.
function translate_tag(tag) {
	var fbelem = document.getElementsByTagName(tag);
	for (var i = 0; i < fbelem.length; i++) {
	    var thisElem = fbelem[i];
	    if (thisElem.textContent in es) {
		thisElem.textContent = es[thisElem.textContent];
	    }
	}
}

//Basic Tag altering.
function translate_class(classname) {
	var fbelem = document.getElementsByClassName(classname);

	for (var i = 0; i < fbelem.length; i++) {
	    var thisElem = fbelem[i];
	    if (thisElem.textContent in es) {
		thisElem.textContent = es[thisElem.textContent];
	    }
	}
}

function loadSecwepemc() {
	translate_tag('a');
	translate_tag('th');
	translate_tag('td');
	translate_tag('span');
	translate_tag('h3');
	translate_tag('dt');

	translate_class('ego_social_context');

	var fbelem = document.getElementsByTagName('input');
	for (var i = 0; i < fbelem.length; i++) {
	    var thisElem = fbelem[i];
	    if (thisElem.getAttribute('placeholder') in es) {
		thisElem.setAttribute('placeholder',es[thisElem.getAttribute('placeholder')]);
	    }
	    if (thisElem.getAttribute('value') in es) {
		thisElem.setAttribute('value',es[thisElem.getAttribute('value')]);
	    }
	}

	var fbelem = document.getElementsByTagName('textarea');
	for (var i = 0; i < fbelem.length; i++) {
	    var thisElem = fbelem[i];
	    if (thisElem.getAttribute('placeholder') in es) {
		thisElem.setAttribute('placeholder',es[thisElem.getAttribute('placeholder')]);
	    }
	    if (thisElem.getAttribute('title') in es) {
		thisElem.setAttribute('title',es[thisElem.getAttribute('title')]);
	    }
	    if (thisElem.textContent in es) {
		thisElem.textContent = es[thisElem.textContent];
	    }
	}

//	var fbelem = document.getElementsByClassName('UIImageBlock_Content UIImageBlock_ICON_Content');
//	for (var i = 0; i < fbelem.length; i++) {
//	    var thisElem = fbelem[i];
//	    //finds if one person likes this.
//	    if (thisElem.textContent.match('likes this.')){
//		icon = thisElem.childNodes[0]
//		link = thisElem.childNodes[1]
//		link.textContent = link.textContent.replace('likes this.', 'r xwexwistes.');
//		thisElem.textContent = '';
//		thisElem.appendChild(icon);
//		thisElem.appendChild(link);
//	    }
//	    if (thisElem.textContent.match('like this.')){
//		icon = thisElem.childNodes[0]
//		link = thisElem.childNodes[1]
//		link.textContent = link.textContent.replace('like this.', 'r xwexwistep.');
//		thisElem.textContent = '';
//		thisElem.appendChild(icon);
//		thisElem.appendChild(link);
//	    }
//	}

	var fbelem = document.getElementsByTagName('h2');
	for (var i = 0; i < fbelem.length; i++) {
	    var thisElem = fbelem[i];
	    if (thisElem.textContent in es) {
		icon = thisElem.childNodes[0]
		thisElem.textContent = es[thisElem.textContent];
		thisElem.appendChild(icon);
	    }
	}
}

loadSecwepemc();

function changedNode(e) {
	translate_tag('a');
	translate_tag('th');
	translate_tag('td');
	translate_tag('span');
	translate_tag('h3');
	translate_tag('dt');

	translate_class('ego_social_context');

	var fbelem = e.target.getElementsByTagName('input');
	for (var i = 0; i < fbelem.length; i++) {
		    var thisElem = fbelem[i];
		    if (thisElem.getAttribute('placeholder') in es) {
		    		thisElem.setAttribute('placeholder',es[thisElem.getAttribute('placeholder')]);
		    	    }
		    if (thisElem.getAttribute('value') in es) {
		    		thisElem.setAttribute('value',es[thisElem.getAttribute('value')]);
		    	    }
		}
	var fbelem = e.target.getElementsByTagName('textarea');
	for (var i = 0; i < fbelem.length; i++) {
	    var thisElem = fbelem[i];
	    if (thisElem.getAttribute('placeholder') in es) {
		thisElem.setAttribute('placeholder',es[thisElem.getAttribute('placeholder')]);
	    }
	    if (thisElem.getAttribute('title') in es) {
		thisElem.setAttribute('title',es[thisElem.getAttribute('title')]);
	    }
	    if (thisElem.textContent in es) {
		thisElem.textContent = es[thisElem.textContent];
	    }
	}

//	var fbelem = e.target.getElementsByClassName('UIImageBlock_Content UIImageBlock_ICON_Content');
//	for (var i = 0; i < fbelem.length; i++) {
//	    var thisElem = fbelem[i];
//	    //finds if one person likes this.
//	    if (thisElem.textContent.match('likes this.')){
//		icon = thisElem.childNodes[0]
//		link = thisElem.childNodes[1]
//		link.textContent = link.textContent.replace('likes this.', 'r xwexwistes.');
//		thisElem.textContent = '';
//		thisElem.appendChild(icon);
//		thisElem.appendChild(link);
// 	    }
//	    if (thisElem.textContent.match('like this.')){
//		    cnodes = thisElem.childNodes;
//		    for (var j = 0; j < cnodes.length; j++){
//			    cnode = cnodes[j];
//			    thisElem.appendChild(cnode);
//		    }
//	    }
//	}

	var fbelem = e.target.getElementsByTagName('h2');
	for (var i = 0; i < fbelem.length; i++) {
		    var thisElem = fbelem[i];
		    if (thisElem.textContent in es) {
		    		icon = thisElem.childNodes[0]
		    		thisElem.textContent = es[thisElem.textContent];
		    		thisElem.appendChild(icon);
		    	    }
		}
}

document.addEventListener('DOMNodeInserted', changedNode, false);
