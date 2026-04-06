let topBtn = document.getElementById("topButton");

window.onscroll = function() {
	scrollFunction();
}

function scrollFunction() {
	if (document.body.scrollTop > 20 || document.document.scrollTop > 20) {
		mybutton.style.display = "block";
	} else {
		mybutton.style.display = "none";
	}
}

function top() {
	document.body.scrollTop = 0;
	document.documentElement.scrollTop = 0;
}
