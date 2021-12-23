export default class Task{
  constructor(data){
    this.id = data.id
    this.name = data.name
    this.complete = data.complete
    this.template = `
      <div>
        <label for="task-${this.id}" id="label-${this.id}">${this.name}</label>
        <input type="checkbox" name="task-${this.id}" id="task-${this.id}">
      </div>
    `
  }
}
