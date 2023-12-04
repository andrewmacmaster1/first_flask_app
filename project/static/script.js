var light = true;

function addNewTask() {
    // fetch input and validate that it isn't empty
    let input = document.getElementById("new-task").value;
    if (input.trim() == "") {
        document.getElementById("new-task").value = "";
        return;
    }
    //fetch incomplete tasks and instantiate new list element
    let list = document.getElementById("incomplete-tasks");
    var li = document.createElement("li");

    // create checkbox element and add to li
    var checkbox = document.createElement('input');
    checkbox.setAttribute("type", "checkbox");
    // checkbox.setAttribute("checked", "false");
    // checkbox.setAttribute()
    checkbox.setAttribute("onclick", "moveTask()");
    li.appendChild(checkbox);

    // create label element and add to li
    var label = document.createElement("label");
    label.innerText = input;
    li.appendChild(label);

    //create edit button and add to li
    var editButton = document.createElement("button");
    editButton.setAttribute("class", "edit");
    editButton.setAttribute("onclick", "editTask()");
    editButton.innerText = "Edit";
    li.appendChild(editButton)
    
    //create edit button and add to li
    var deleteButton = document.createElement("button");
    deleteButton.setAttribute("class", "delete");
    deleteButton.setAttribute("onclick", "deleteTask()");
    deleteButton.innerText = "Delete";
    li.appendChild(deleteButton)
    
    list.appendChild(li);

    // reset input box
    document.getElementById("new-task").value = "";
}

function deleteTask() {
    var currentTask = document.activeElement.parentElement;
    currentTask.remove();
}

function moveTask() {
    var currentTask = document.activeElement.parentElement;
    var otherList;
    if (currentTask.parentElement.id == "incomplete-tasks") {
        otherList = document.getElementById("completed-tasks");
    }
    else if (currentTask.parentElement.id == "completed-tasks") {
        otherList = document.getElementById("incomplete-tasks");
    }
    otherList.appendChild(currentTask);
}

function editTask() {
    var currentTask = document.activeElement.parentElement;
    var taskLabel = currentTask.children[1];
    var editButton = currentTask.children[2];

    var inputBox = document.createElement("input");
    inputBox.setAttribute("type", "text");
    inputBox.setAttribute("value", taskLabel.innerText);
    inputBox.style.display = 'block';

    var saveButton = document.createElement("button");
    saveButton.setAttribute("class", "save");
    saveButton.setAttribute("onclick", "saveTask()");
    saveButton.innerText = "Save";

    currentTask.replaceChild(inputBox, taskLabel);
    currentTask.replaceChild(saveButton, editButton);
}

function saveTask() {
    var currentTask = document.activeElement.parentElement;
    var taskInput = currentTask.children[1];
    var saveButton = currentTask.children[2];

    var label = document.createElement("label");
    label.innerText = taskInput.value;

    var editButton = document.createElement("button");
    editButton.setAttribute("class", "edit");
    editButton.setAttribute("onclick", "editTask()");
    editButton.innerText = "Edit";

    currentTask.replaceChild(label, taskInput);
    currentTask.replaceChild(editButton, saveButton);
}

function clearList() {
    document.getElementById("completed-tasks").innerHTML = "";
}

