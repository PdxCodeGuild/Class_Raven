// initializes mobile sidebar functionality
document.addEventListener('DOMContentLoaded', function() {
	var elems = document.querySelectorAll('.sidenav');
	var instances = M.Sidenav.init(elems, {edge: 'right'});
});

// save target's initial state

// move template form template to target
function load_contact_form(){
	let target = document.getElementById('contact-form-target').innerHTML;
	let form = document.getElementById('contact-form').innerHTML;
	document.getElementById('contact-form-target').innerHTML = form;
	document.getElementById('contact-form').innerHTML = target;
}
