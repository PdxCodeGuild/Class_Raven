// Manipulate the DOM!
let taskContent = document.querySelector("#content")
let taskTopic = document.querySelector("#subTitle")
let taskTitle = document.querySelector("#title")
let createTask = document.querySelector("#submit")
let outPutTask = document.querySelector("#madeTask")
let templateCard = document.querySelector("#templateCard")

let toDos = []

function createTodo(title, topic, body) {
    let createTodoTask = {
        title: title,
        topic: topic,
        body: body
    }
    // console.log(createTodoTask)

    toDos = toDos.concat(createTodoTask)
    // console.log(toDos)
    showToDoItem(toDos)
}

// Listen for the click event
createTask.addEventListener("click", () => {
    toDos = createTodo(taskTitle.value, taskTopic.value, taskContent.value)
    // console.log(taskContent.value, taskTopic.value, taskTitle.value)
    // Clears the field
    taskContent.value = ""
    taskTopic.value = ""
    taskTitle.value = ""    
    // console.log(toDos)
})

function showToDoItem(toDos) {

    // let todo

    // for (todo of toDos) {
    let newTodoItem = document.createElement("div")

    let templateCardThing = templateCard.content.cloneNode(true)

    newTodoItem.appendChild(templateCardThing)
    // console.log(JSON.stringify(templateCard, null, 2))

    let todoTextTitle = newTodoItem.querySelector("#title-post")
    let todoTextTopic = newTodoItem.querySelector("#subTitle-post")
    let todoTextBody = newTodoItem.querySelector("#body-post")

    // console.log(newTodoItem)
    

    todoTextTitle.innerHTML = toDos.title
    todoTextTopic.innerHTML = toDos.topic
    todoTextBody.innerHTML = toDos.body

    outPutTask.appendChild(newTodoItem)
    // }
}