// Manipulate the DOM!
let taskContent = document.querySelector("#content"),
    taskTopic = document.querySelector("#subTitle"),
    taskTitle = document.querySelector("#title"),
    createTask = document.querySelector("#submit"),
    outPutTask = document.querySelector("#madeTask"),
    templateCard = document.querySelector("#templateCard")

    let toDos = []

function createTodo(title, topic, body) {
    let createTodoTask = {
        title: title,
        topic: topic,
        body: body
    }
    // console.log(createTodoTask)

    toDos = toDos.concat(createTodoTask)
}

function removeTodo() {

    let deleteTodoItem = document.createElement("div")
    let templateCardThing = templateCard.content.cloneNode(true)
    deleteTodoItem.removeChild(templateCardThing)

    // let todoTextTitle = deleteTodoItem.querySelector("#title-post")
    // let todoTextTopic = deleteTodoItem.querySelector("#subTitle-post")
    // let todoTextBody = deleteTodoItem.querySelector("#body-post")

    // toDos = toDos.filter(task => task.title !== currentToDo.title)
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
    showToDoItem(toDos)
})

function showToDoItem(toDos) {

    let newTodoItem = document.createElement("div")

    let templateCardThing = templateCard.content.cloneNode(true)

    newTodoItem.appendChild(templateCardThing)
    // console.log(JSON.stringify(templateCard, null, 2))

    let todoTextTitle = newTodoItem.querySelector("#title-post")
    let todoTextTopic = newTodoItem.querySelector("#subTitle-post")
    let todoTextBody = newTodoItem.querySelector("#body-post")
    // console.log(toDos)
    if (!toDos[toDos.length - 1].title && !toDos[toDos.length - 1].topic && !toDos[toDos.length - 1].body) {
        alert("Input Required")
        return
    }

    todoTextTitle.innerHTML = toDos[toDos.length - 1].title
    todoTextTopic.innerHTML = toDos[toDos.length - 1].topic
    todoTextBody.innerHTML = toDos[toDos.length - 1].body

    outPutTask.appendChild(newTodoItem)

}


outPutTask.addEventListener("click", () => {

    removeTodo()
})