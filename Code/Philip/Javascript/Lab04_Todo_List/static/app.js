let honeydoList
let honeydoObjList = []
let completedList
let honeydoButton
let completedButton
let trashcan
let honeydoText
let counter = 0
let honeydoDiv
let newHoneydo
let item
let honeydo

completedList = document.querySelector ('.completed_list');
honeydoList = document.querySelector('.honeydo_list');
honeydoButton = document.querySelector('.honeydo_button');
honeydoButton.addEventListener("click", addHoneydo)
honeydoList.addEventListener("click", trashOrComplete)
completedList.addEventListener("click", trashOrComplete)

function addHoneydo(action) {
    //prevent form from submitting and refreshing
    action.preventDefault();
    //create todo DIV
    honeydoDiv = document.createElement('div');
    //assign the new DIV a todo class that will be used to style the div
    honeydoDiv.classList.add('honeydo');
    //create todo li that will be used to display the text value of the input
    newHoneydo = document.createElement('li');
    //get input value and save to the honeydoText variable
    honeydoText = document.getElementById("enterTask").value;
    //bind the newTodo element with the text value
    newHoneydo.innerText = honeydoText;
    //assign the element a class of honeydo_item
    newHoneydo.classList.add('honeydo_item');
    //place the element inside of the todoDiv as a child
    honeydoDiv.appendChild(newHoneydo);
    //if nothing is entered in the input return null
    //if(honeydoText === ""){
    //    return null
    //}
    //create counter to populate object id
    counter++;
    //build an object for the honeydoObjList
    honeydoObject = {
        id: counter,
        honeydoText: honeydoText,
        complete: false,
      };
    //Add the new Object to the array
    honeydoObjList.push(honeydoObject);
    
    //add check mark to complete an item
    //create an element for the check mark
    completedButton = document.createElement('button');
    //add the check icon to the element
    completedButton.innerHTML = '<i class="fas fa-check"></i>';
    //give the check icon a class of complete_btn
    completedButton.classList.add('complete_btn')
    //place the new check mark elememnt inside the honeydoDiv
    honeydoDiv.appendChild(completedButton);
    
    //add delete to the todoDiv
    //create an element for the trashcan
    trashcan = document.createElement('button');
    //add the trashcan icon to the element
    trashcan.innerHTML = '<i class="fas fa-trash"></i>';
    //give the trash icon a class of trash_btn
    trashcan.classList.add('trash_btn')
    //place the new delete icon element with the trash_btn class in the honeydoDiv
    honeydoDiv.appendChild(trashcan);
    //Take the entire todoDiv and add it to the honeydoList
    honeydoList.appendChild(honeydoDiv);
    //Clear input value
    document.getElementById("enterTask").value = "";
    console.log(honeydoList)
}

//Build function to check the item class to delete or complete
function trashOrComplete(ele) {
    //Get the target of an event and store as a variable item
    item = ele.target;

    //if the class of the target variable is trash_btn then continue with if statement
    if (item.classList[0] === "trash_btn") {
        //set a new variable to capture the parent element of the item
        honeydo = item.parentElement;
        //remove that item
            honeydo.remove()
    }

    //if the class of the target variable was complete_btn then continue with if statement
    if (item.classList[0] === "complete_btn") {
        //set a new variable to capture the parent element of the item
        honeydo = item.parentElement;
        //use the toggle method to easily turn the completedItem class on and off
        honeydo.classList.toggle("completedItem")
        console.log(honeydo.classList);
        if(honeydo.classList.contains("completedItem")) {
            completedList.appendChild(honeydo);
        } else {
            honeydoList.appendChild(honeydo);
        }
    }
}

