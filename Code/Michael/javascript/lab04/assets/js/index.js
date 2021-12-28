function addItem(item) {
	// Add item to todo-list.
	// Do not add item if it already exists on either list or is empty.
	var li = document.getElementById("li-" + item); // Attempt to get item.
	var li2 = document.getElementById("completed-li-" + item); // Attempt to get item.
	if (li2 != null || li != null || item == "") {
		//If item exists in a list or if it is empty.
		return; //Do not add item.
	}
	var ul = document.getElementById("todo-list"); // Get todo-list.
	var li = document.createElement("li"); // Create li element.
	var label = document.createElement("label"); // Create label element.
	li.setAttribute("id", "li-" + item); //Set id of item.
	var checkbox = document.createElement("input"); //Create checkbox.
	label.innerHTML = "&nbsp;" + item; //Set label text.
	label.setAttribute("for", "checkbox-" + item); //Set for attribute.
	label.setAttribute("id", "label-" + item); //Set id attribute.
	checkbox.setAttribute("type", "checkbox"); //Set type to checkbox.
	checkbox.setAttribute("id", "checkbox-" + item); //Set id of checkbox.
	checkbox.setAttribute("onclick", "markItem('li-" + item + "')"); //Add onclick attribute.
	ul.appendChild(li); //Add item to list.
	li.appendChild(checkbox); //Add checkbox to item.
	li.appendChild(label); //Add label to item.
}

function removeItem(list, item) {
	// Remove item from list.
	var ul = document.getElementById(list); // Get list.
	var li = document.getElementById(item); // Get item.
	ul.removeChild(li); // Remove item from list.
}

function markItem(item) {
	// Mark item as completed.
	var ul = document.getElementById("todo-list"); // Get todo-list.
	var li = document.getElementById(item); // Get item.
	var label = li.getElementsByTagName("label")[0]; // Get label.
	var lineThrough = document.createElement("s"); // Create line-through element.
	lineThrough.innerHTML = label.innerHTML; // Set innerHTML of line-through element to innerHTML of label.
	lineThrough.setAttribute("id", "completed-" + item.substring(3)); //Set id of line-through element.
	label.innerHTML = ""; // Remove label text.
	ul.removeChild(li); // Remove li item from list.
	var ul2 = document.getElementById("completed-list"); // Get completed list.
	li.setAttribute("id", "completed-" + item); // Set id of li item.
	ul2.appendChild(li); // Add li item to completed-list.
	var checkbox = document.getElementById("checkbox-" + item.substring(3)); // Get checkbox but remove `li-` from item.
	checkbox.remove(); // Remove checkbox.
	li.appendChild(lineThrough); // Add line-through element to label.
}

document.getElementById("button").addEventListener("click", function () {
	// Add event listener to button.
	var item = document.getElementById("task").value; //Get value of task input.
	addItem(item); //Add item to list.
});

document.getElementById("task").addEventListener("keyup", function (event) {
	// Add event listener to input.
	if (event.code === "Enter") {
		// If enter key is pressed.
		event.preventDefault(); //Prevent form from submitting with default.
		document.getElementById("button").click(); //Call button click event.
	}
});

document
	.getElementById("todo-list")
	.addEventListener("contextmenu", function (event) {
		// Add event listener to todo-list.
		event.preventDefault(); // Prevent default context menu.
		removeItem("todo-list", "li-" + event.target.id.substring(6)); // Remove item from todo-list.
	});

document
	.getElementById("completed-list")
	.addEventListener("contextmenu", function (event) {
		// Add event listener to completed-list.
		event.preventDefault(); //Prevent default context menu.
		if (event.target.id.includes("completed-li-")) {
			// If item includes `completed-li-`.
			removeItem("completed-list", event.target.id); // Remove item from completed-list.
		} else {
			// If item does not include `completed-li-`.
			removeItem(
				// Remove item from completed-list.
				"completed-list",
				"completed-li-" + event.target.id.substring(10)
			);
		}
	});
