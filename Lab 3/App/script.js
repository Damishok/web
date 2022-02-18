let task = [{
    name: "Do Hw",
},
{
    name: "Dishes",
},
{
    name: "Pick up the parcel",
}
]


const TaskDiv = document.getElementById("task");

function showTask() {
TaskDiv.innerHTML = task.map((item, index) =>
    `<div class="task-item">
            <div><input type="checkbox" id="subscribeNews${index+1}" name="subscribe" value="newsletter"></div>
            <div>${item.name}</div>
            <div> <span onclick="deleteTask(${index})"> Delete </span> </div>
            
    </div>`
).join('');
}

showTask()

const name = document.querySelector("#name")


function addTask() {
task.push({
    name: name.value,

})
name.value = "";

showTask();
}


function deleteTask(i) {
task.splice(i, 1);

showTask()
}

function clear () {
TaskDiv.innerHTML = task.map((item, index) =>
    task.length = 0);
}