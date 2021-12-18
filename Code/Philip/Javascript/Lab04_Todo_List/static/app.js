//Create an empty array to store the task objects
honeydoList = [];

//Declare variables
  //Object to store in Array
let honeydoObject;
  //Store form value
let honeydoText;
  //Variable to hold list item element
let honeydoListElement;
  //Variable to hold the li list element
let listElement;
  //Variable to hold the trashcan icon
let trashcan;
  //Variable to hold the Object id value for marking a task complete
let updateId
  //Variable to hold the Object index for marking a task complete
let updateHoneydoIndex
  //Variable to hold the Object Id value for deleting a task
let deleteId
  //Variable to hold index of Object to be deleted
let deleteIndex

//Create a variable to hold the items that will go into each list item
honeydoListElement = document.getElementById("task");

//--------CREATE-------------------------------------------
//First we are going to create an event listener to monitor for a click on the submit button
//Second we are going to create a function to add the text value to the array as an Object and create an ID for the ID property

//1. Create event listener when the submit button is clicked to run the function to add a new Object to the array
document.getElementById("submit_button").addEventListener("click", addHoneydo);

//2. Create function to get text value from form as an Object
function addHoneydo() {
  //2.a. Get text value from the form and store as a variable
  honeydoText = document.getElementById("enterTask").value;
  //2.b. Build an array Object
    honeydoObject = {
      id: honeydoList.length, 
      honeydoText: honeydoText,
      complete: false,
    };
  //2.c. Add the new Object to the array
    honeydoList.push(honeydoObject);
  //2.d. Delete the information from the form text input after the user submits
    document.getElementById("enterTask").value = "";
  //2.e. Invoke function to display the new results
    displayHoneydos();
  }

//---------Retrieve-------------------------------------------
//We are going to create a function that will display each array Object as a list element when invoked

//1. Create a function that will display all of the items on screen
function displayHoneydos() {
    //1.a. Clear whats there or else it will infinte loop
  honeydoListElement.innerHTML = "";  
  
  //1.b. Run a forEach loop to retrieve the tasks text for each Object in the array
  honeydoList.forEach((item) => {
    //1.b.1. Create a list item element for the Object and store in listElement variable
    listElement = document.createElement("li");
    //1.b.2. Insert the Objects text into the listElement variable
    listElement.innerHTML = item.honeydoText;
    //1.b.3. Assign an id attribute to the listElement with the value from the Object id for use in deleting
    listElement.setAttribute("data-id", item.id);
    //1.b.4. Create an element for the trashcan icon and store in the trashcan variable
    trashcan = document.createElement("i");
    //1.b.5. Assign a "data-id" attribute to the trashcan with the value from the Object id for use in deleting
    trashcan.setAttribute("data-id", item.id);
    //1.b.6. Give the trash can a class of "fas" from Font Awesome
    trashcan.classList.add("fas");
    //1.b.7. Give the trash can a class of "fa-trash" from Font Awesome (Note that you have to declare a separate attribute for each attribute)
    trashcan.classList.add("fa-trash");
 
   
  
    //1.b.8. Check to see if the Object complete property is true
    if (item.complete) {
      //1.b.8.a. If true, assign the class of completed which will use CSS to line through the item
      listElement.classList.add("completed");
    }

    //--------------UPDATE--------------------------------------------------
    //First we are going to create an event listener to monitor for a click on the element
    //Second we are going to run a function that will 

    //1. Add event listener for a completed list element
    listElement.addEventListener("click", getUpdateId);
    
    //2. Function to get the "data-id" attribute and store as a variable
    function getUpdateId() {
      //2.a. Get the element "data-id" attribute and pass to the variable
      updateId = this.getAttribute("data-id");
      //2.b. Run the completed honeydo function and pass it the variable which contains the "data-id"
      doneHoneydo(updateId);
    }

    //3. Function to change Object complete to true
    function doneHoneydo(updateId) {
      //3.a. Find the index of the Object by the Object id property
      updateHoneydoIndex = honeydoList.findIndex((item) => item.id == updateId);
      //3.b. Change the value of the Objects complete (boolean) property
      honeydoList[updateHoneydoIndex].complete = !honeydoList[updateHoneydoIndex].complete;
      //3.c. Invoke the function to display all Objects
      displayHoneydos();
    }

    //----------------Delete--------------------------------------------------
    //First we are going to add an event listener for the trashcan click and invoke a function to grab the id
    //Second we are going to create a function that grabs the id
    //Third we are going to use the id to find and remove the data from the Object

    //1. Add an event listener to the trashcan to run when the trashcan is clicked
    trashcan.addEventListener("click", getDeleteId);

    //2. Function to get the "data-id" attribute and store as a variable
    function getDeleteId() {
      //2.a. Get the element "data-id" attribute and pass it to the variable
      deleteId = this.getAttribute("data-id");
      //2.b. Run the deleteItem function and pass it the variable which contains the "data-id"
      deleteItem(deleteId);
    }

    //3. Function to delete item by passing the "data-id" to it
    function deleteItem(deleteId) {
      //3.a. Find the index of the Object by the Object id property
      deleteIndex = honeydoList.findIndex((item) => item.id == deleteId)
      //3.b. Invoke the splice method to remove the object
      honeydoList.splice((deleteIndex),1);
      //3.c. Invoke the function to display all Objects
      displayHoneydos();
    }
    //---------------------Clean up---------------------------------------------

       //1. Add the listElement as a child of the honeydoListElement
       honeydoListElement.appendChild(listElement);
       //2. Add the trashcan as a child of the list element
       listElement.appendChild(trashcan);
       //3. Sort the array to place completed tasks on the bottom of the list
       honeydoList.sort((b, a) => b.complete - a.complete);
  });
}


    
