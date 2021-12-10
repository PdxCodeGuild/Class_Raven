var toastTrigger1 = document.getElementById("contact-now");
var toastTrigger2 = document.getElementById("nav-contact");
var toastLive = document.getElementById("liveToast");
var toast = new bootstrap.Toast(toastLive);
setTimeout(function () {
	toast.show();
}, 15000);
if (toastTrigger1) {
	toastTrigger1.addEventListener("click", function () {
		toast.show();
		document.getElementById("jumbotron").style.display = "none";
		if (window.matchMedia("(min-width: 768px)").matches) {
			document.getElementById("jumbo-hidden").style.display = "block";
		}
	});
}
if (toastTrigger2) {
	toastTrigger2.addEventListener("click", function () {
		toast.show();
		document.getElementById("jumbotron").style.display = "none";
		if (window.matchMedia("(min-width: 768px)").matches) {
			document.getElementById("jumbo-hidden").style.display = "block";
		}
	});
}
setTimeout(function () {
	document.getElementById("jumbotron").style.display = "none";
	if (window.matchMedia("(min-width: 768px)").matches) {
		document.getElementById("jumbo-hidden").style.display = "block";
	}
}, 15000);
