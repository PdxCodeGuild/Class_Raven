// Manipulate the DOM!
let taskContent = document.querySelector("#content")
let taskTopic = document.querySelector("#subTitle")
let taskTitle = document.querySelector("#title")
let createTask = document.querySelector("#submit")



let toDos = [

]


// Listen for the click event
createTask.addEventListener("click", () => {
    createTodo(taskTitle.value, taskTopic.value, taskContent.value)
    // Clears the field
    taskContent.value = ""
    taskTopic.value = ""
    taskTitle.value = ""
})

function createTodo(title, topic, body) {
    let createTodoTask = {
        title: title,
        topic: topic,
        body: body
    }

    toDos = toDos.concat(createTodoTask)
}

console.log(toDos)
