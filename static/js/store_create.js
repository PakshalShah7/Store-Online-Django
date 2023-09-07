// for store create

let hourForm = document.querySelectorAll("#hour-form")
let container = document.querySelector("#create_form")
let addButton = document.querySelector("#add_more")
let totalForms = document.querySelector("#id_stores-TOTAL_FORMS")

let formNum = hourForm.length-1
let formRegex = RegExp(`stores-(\\d){1}-`,'g')

addButton.addEventListener('click', addForm)

function addForm(e){
    e.preventDefault()

    let newForm = hourForm[0].cloneNode(true)

    formNum++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `stores-${formNum}-`)
    container.insertBefore(newForm, addButton)
    totalForms.setAttribute('value', `${formNum+1}`)

    console.log(formNum)
}
