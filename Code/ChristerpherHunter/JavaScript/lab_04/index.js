// Manipulate the DOM!
let taskContent = document.querySelector("#content")
let taskTopic = document.querySelector("#subTitle")
let taskTitle = document.querySelector("#title")
let createTask = document.querySelector("#submit")
let outPutTask = document.querySelector("#madeTask")
let templateCard = document.querySelector("#templateCard")



let toDos = [   
]

function createTodo(title, topic, body) {
    let createTodoTask = {
        title: title,
        topic: topic,
        body: body
    }
    // console.log(createTodoTask)

    toDos = toDos.concat(createTodoTask)
    // console.log(toDos)
}

// Listen for the click event
createTask.addEventListener("click", () => {
    createTodo(taskTitle.value, taskTopic.value, taskContent.value)
    // console.log(taskContent.value, taskTopic.value, taskTitle.value)
    // Clears the field
    taskContent.value = ""
    taskTopic.value = ""
    taskTitle.value = ""
    // console.log(toDos)
})

function showToDoItem(itemAdded) {

    let newTodoItem = document.createElement("div")

    let templateCardThing = templateCard.textContent.cloneNode(true) 

    let 

}