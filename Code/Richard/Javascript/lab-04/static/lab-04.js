let task, create, vanish, finish, done, disappear;

const incompleteTodosDiv = document.querySelector("#incomplete-todos");
const completeTodosDiv = document.querySelector("#complete-todos");

let incomplete = ["cut grass", "hide eggs", "fill baskets"];

let complete = ["buy grass", "buy eggs", "buy baskets"];

function loadTodo() {
  let todo, finish, vanish;
  incompleteTodosDiv.innerHTML = "";
  for (i in incomplete) {
    task = incomplete[i];
    todo = document.createElement("div");
    todo.innerText = task;
    todo.id = `incomplete-${i}`;

    finish = document.createElement("button");
    finish.id = `Incomplete-${i}`;
    finish.innerText = "Done!";
    finish.addEventListener('click', function (event){
        let todoId= event.target.parentNode.id
        let cut= todoId.split('-')
        let num = parseInt(cut[1])
        complete.push(incomplete[num])
        incomplete.pop(num)
        loadTodo()
        loadDone()
    })

    vanish = document.createElement("button");
    vanish.id = `Incomplete-${i}`;
    vanish.innerText = "Delete";
    vanish.addEventListener('click', function (event){
        let todoId= event.target.parentNode.id
        let cut= todoId.split('-')
        let num = parseInt(cut[1])
        complete.pop(num)
        console.log(complete)
        loadTodo()
        loadDone()
    })
    todo.appendChild(finish);

    todo.appendChild(vanish);

    incompleteTodosDiv.appendChild(todo);
  }
}

function loadDone() {
  let todo, vanish;
  completeTodosDiv.innerHTML = "";
  for (let i in complete) {
    task = complete[i];

    todo = document.createElement("div");
    todo.innerText = task;
    todo.id = `complete-${i}`;

    vanish = document.createElement("button");
    vanish.id = `Complete-${i}`;
    vanish.innerText = "Delete";
    vanish.addEventListener('click', function (event){
        let todoId= event.target.parentNode.id
        let cut= todoId.split('-')
        let num = parseInt(cut[1])
        complete.pop(num)
        console.log(complete)
        loadDone()
    })

    todo.appendChild(vanish);

    completeTodosDiv.appendChild(todo);
  }
}

create = document.querySelector("#create");
create.addEventListener("click", function createtodo() {
  incomplete.push(text.value);
  text.value = "";
  loadTodo();
});

loadTodo();
loadDone();

