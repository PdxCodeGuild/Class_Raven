const ELEMENTS = document.getElementsByClassName('helptext')
console.log(ELEMENTS)

function hideHelpText(){
    for (let i = 0; i < ELEMENTS.length; i++){
        let element = ELEMENTS[i]
        console.log(element)
        // const TEXT = element.innerHTML
        // element.innerHTML = ''
        // console.log(TEXT)
        element.classList.add('visually-hidden')
    }
}

function toggleHelpText(){
    for (let i = 0; i < ELEMENTS.length; i++){
        let element = ELEMENTS[i]
        console.log(element)
        element.classList.toggle('visually-hidden')
    }
}