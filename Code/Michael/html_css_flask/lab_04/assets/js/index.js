var jumboTrigger = document.getElementById("jumbo-button");
if (jumboTrigger) {
	jumboTrigger.addEventListener("click", function () {
		document.getElementById("jumbotron").style.display = "none";
	});
}
