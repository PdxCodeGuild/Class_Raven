// Toggle display of id edit-form when edit edit-button is clicked
$(document).ready(function () {
	$("#edit-form").toggle();
	$("#edit-button").click(function () {
		$("#edit-form").toggle();
	});
});
