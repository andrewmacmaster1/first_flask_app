var light = true;


function editTask() {
    var currentTask = document.activeElement.parentElement;
    var taskLabel = currentTask.children[1];
    var editButton = currentTask.children[2];

    var postFrame = document.createElement("form")
    postFrame.setAttribute("method", "post")
    postFrame.action = `${taskLabel.id}\\edit`

    var inputBox = document.createElement("input");
    inputBox.setAttribute("type", "text");
    inputBox.setAttribute("id", taskLabel.id)
    inputBox.setAttribute("value", taskLabel.innerText);
    inputBox.setAttribute("name", "edit_task");
    inputBox.style.display = "block";

    var saveButton = document.createElement("button");
    saveButton.setAttribute("class", "save");
    if (light) {
        saveButton.classList.toggle("light-mode");
    } else {
        saveButton.classList.toggle("dark-mode");
    }
    saveButton.setAttribute("type", "submit");
    saveButton.innerText = "Save";

    postFrame.appendChild(inputBox)
    postFrame.appendChild(saveButton)

    currentTask.removeChild(taskLabel);
    currentTask.replaceChild(postFrame, editButton);
}

function switchTheme() {
    console.clear();
    if (light) {
        elements=Array.prototype.slice.call(document.getElementsByClassName('light-mode'));
        light = false;
    } else {
        elements=Array.prototype.slice.call(document.getElementsByClassName('dark-mode'));
        light = true;
    }
    for (element of elements) {
        console.log(element)
        element.classList.toggle("light-mode");
        element.classList.toggle("dark-mode");
    }
    
    console.log(light)
}