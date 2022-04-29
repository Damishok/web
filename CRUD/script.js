function newTask() {
    if (document.getElementById("new-task").value != "") {

        let block1 = document.createElement("div");

        let check1 = document.createElement("input");

        let txt1 = document.createElement("p");

        let deleteButton = document.createElement("button");

        check1.id = "check";
        check1.className = "checkclass"
        check1.type = "checkbox"
        block1.id = "task";
        block1.className = "taskclass";
        txt1.id = "txt";
        txt1.className = "txtclass";

        deleteButton.id = "btn2";
        deleteButton.className = "button";
        deleteButton.textContent = "X";
        deleteButton.addEventListener("click", myDelete);

        txt1.textContent = document.getElementById("new-task").value;

        block1.appendChild(check1);
        block1.appendChild(txt1);
        block1.appendChild(deleteButton);

        document.getElementById("right-part").appendChild(block1);
        document.getElementById("new-task").value = "";

    }
    else {
        alert("Write something!")
    }


}


function myDelete() {
    this.parentNode.remove();

}
