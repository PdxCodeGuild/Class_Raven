export default class Task{
  constructor(data){
    this.id = data.id
    this.name = data.name
    this.complete = false
    if (this.complete === false){
    this.template = `
    <div>
      <label for="task-${this.id}" id="label-${this.id}">${this.name}</label>
      <input type="checkbox" name="task-${this.id}" id="task-${this.id}">
    </div>
    `}
    if (this.complete === true){
      this.template =  `
      <div>
        <label class="complete" for="task-${this.id}" id="label-${this.id}">${this.name}</label>
        <input checked type="checkbox" name="task-${this.id}" id="task-${this.id}">
      </div>
      `
    }
  }

}
