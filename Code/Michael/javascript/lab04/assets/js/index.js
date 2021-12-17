//Add item to the list.
function addItem(item) {
	//Do not add item if exists in a list or if it is empty.
	var li = document.getElementById("li-" + item); //Attempt to get item.
	var li2 = document.getElementById("completed-li-" + item); //Attempt to get item.
	if (li2 != null || li != null || item == "") {
		//If item exists in a list or if it is empty.
		return; //Do not add item.
	}

	var ul = document.getElementById("todo-list");
	var li = document.createElement("li");
	var label = document.createElement("label");

	li.setAttribute("id", "li-" + item); //Set id of item.
	li.setAttribute("onclick", "removeItem(this.id)"); //Set onclick attribute.
	var checkbox = document.createElement("input"); //Create checkbox.
	label.innerHTML = "&nbsp;" + item; //Set label text.
	label.setAttribute("for", "checkbox-" + item); //Set for attribute.
	checkbox.setAttribute("type", "checkbox"); //Set type to checkbox.
	checkbox.setAttribute("id", "checkbox-" + item); //Set id of checkbox.
	checkbox.setAttribute("onclick", "markItem('li-" + item + "')"); //Add onclick attribute.

	ul.appendChild(li); //Add item to list.
	li.appendChild(checkbox); //Add checkbox to item.
	li.appendChild(label); //Add label to item.
}

//Remove item from the list.
function removeItem(item) {
	var ul = document.getElementById("todo-list");
	var li = document.getElementById(item);
	ul.removeChild(li); //Remove item from list.
}

//Mark item as completed.
function markItem(item) {
	var ul = document.getElementById("todo-list");
	var li = document.getElementById(item);
	var label = li.getElementsByTagName("label")[0]; //Get label.
	var lineThrough = document.createElement("s"); //Create line-through element.
	lineThrough.innerHTML = label.innerHTML;
	label.innerHTML = "";
	label.appendChild(lineThrough); //Add line-through element to label.
	ul.removeChild(li); //Remove item from list.
	var ul2 = document.getElementById("completed-list");
	li.setAttribute("id", "completed-" + item); //Set id of item.
	li.removeAttribute("onclick"); //Remove onclick attribute.
	ul2.appendChild(li); //Add item to completed list.
	var checkbox = document.getElementById("checkbox-" + item.substring(3)); //Get checkbox but remove `li-` from item.
	checkbox.remove(); //Remove checkbox.
}

//Listen for the form to be submitted.
document.getElementById("button").addEventListener("click", function () {
	var item = document.getElementById("task").value;
	addItem(item);
});
