// assigning variable to the add task button
let addTask = document.getElementById("enter");
//assigning variable to input user enters in the add new task input section
let input = document.getElementById("userinput");
// returns the element that matches the CSS selector of 'ul' (vs the ID for getElementbyID)
let ul = document.querySelector("ul");
// created variable to assign to ul where I will append completed tasks
let completedTasks = document.getElementById("completedTaskList");

// simple function that calculates length of user input(really just making sure it's > 0)
function inputLength() {
  return input.value.length;
}

// function to create new task list item and corresponding delete button
function newTaskList() {
  // var myList = document.getElementsByTagName("li");
  // assigning variable to the li item we are creating when function is ran
  let li = document.createElement("li");
  let completedLi = document.createElement("li");
  //appending the user's input value to the li element we just created
  li.appendChild(document.createTextNode(input.value));
  //now appending that li with the user input to the ul(we assigned ul variable to the ul in document using queryselector)
  ul.appendChild(li);
  // clearing input value of user when function is ran
  let completed = input.value;
  input.value = "";
  // assigning the creation of delete button to the deleteButton variable
  let deleteButton = document.createElement("button");
  let deleteButton2 = document.createElement("button");
  // styling that delete button
  deleteButton.style.border = "none";
  deleteButton.style.transition = "all .3s ease-in-out";
  deleteButton.style.backgroundColor = "#ffffff";
  deleteButton.style.margin = "20px";
  deleteButton2.style.border = "none";
  deleteButton2.style.transition = "all .3s ease-in-out";
  deleteButton2.style.backgroundColor = "#ffffff";
  deleteButton2.style.margin = "20px";

  //adding event listeners to grow and remove grow when item is hovered with mouse
  deleteButton.addEventListener("mouseenter", function () {
    deleteButton.classList.add("grow");
  });
  deleteButton.addEventListener("mouseleave", function () {
    deleteButton.classList.remove("grow");
  });
  deleteButton2.addEventListener("mouseenter", function () {
    deleteButton2.classList.add("grow");
  });
  deleteButton2.addEventListener("mouseleave", function () {
    deleteButton2.classList.remove("grow");
  });
  //assigning text to delete button with createTextNode
  deleteButton.appendChild(document.createTextNode("🗑️"));
  // appending the delete button to each li that is created
  li.appendChild(deleteButton);
  deleteButton2.appendChild(document.createTextNode("🗑️"));

  // creating function that gives us access to parent element of delete button (which is li)
  // and deletes it when we click delete
  deleteButton.onclick = function () {
    completedLi.style.textDecoration = "line-through";
    completedTasks.appendChild(completedLi);
    completedLi.appendChild(document.createTextNode(completed));
    completedLi.appendChild(deleteButton2);
    this.parentElement.style.display = "none";
    deleteButton2.onclick = function () {
      this.parentElement.style.display = "none";
    };
  };
}

//creating function that indicates to run addTaskList only if length of input from user is >0(they actually wrote something)
function addTaskList() {
  if (inputLength() > 0) {
    newTaskList();
  }
}

// create event listener to have addTaskList function run if user clicks on add task button (variable we already created assinged to id of add button)
addTask.addEventListener("click", addTaskList);
