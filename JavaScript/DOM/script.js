import randomInt from "../Modules/randomInt.js";

let body = document.querySelector("body");
// Exercise 1.6
let button1 = document.createElement("button");
let button2 = document.createElement("button");
let elementContainer = document.createElement("div");

button1.innerText = "Create";
button2.innerText = "Delete";

button1.style.fontSize = "25px";
button2.style.fontSize = "25px";

let elementCount = 1;
button1.addEventListener("click", () => {
	let newElement = document.createElement("p");
	newElement.textContent = `I am element Nr.${elementCount}`;
	elementCount++;
	elementContainer.append(newElement);
});
button2.addEventListener("click", () => {
	elementContainer.removeChild(elementContainer.lastChild);
	elementCount--;
});

body.append(button1, button2, elementContainer);

// Exercise 1.7
let button3 = document.createElement("button");
let clickViewer = document.createElement("span");
let clickCounter = 0;

clickViewer.textContent = clickCounter;

button3.style.margin = "25px 15px 0 0";
button3.innerText = "Clicker";

button3.addEventListener("click", () => {
	clickCounter++;
	clickViewer.textContent = clickCounter;
});

body.append(button3, clickViewer);

// Exercise 2.1 && 2.2
for (let i = 1; i <= 5; i++) {
	let newElement = document.createElement("p");
	newElement.setAttribute("class", "TOelement");
	newElement.textContent = `I am element Nr.${i}`;
	if (i % 2 != 0) {
		newElement.setAttribute("id", `spec${i / 2 - 0.5}`);
	}
	body.append(newElement);
}

// Exercise 2.3
document.getElementById("spec1").style.backgroundColor = "green";
for (let element of document.getElementsByClassName("TOelement")) {
	element.style.fontWeight = "700";
}
for (let element of document.getElementsByTagName("p")) {
	element.style.textDecoration = "underline";
}

// Exercise 2.4
let divContainer = document.createElement("div");
divContainer.setAttribute("class", "divContainer");

for (let i = 1; i <= 6; i++) {
	let newElement = document.createElement("div");
	newElement.setAttribute("class", "setDivs");

	newElement.style.height = "100px";
	newElement.style.width = "100px";
	newElement.style.border = "2px solid black";

	divContainer.append(newElement);
}

body.append(divContainer);

// Exercise 2.5
let button4 = document.createElement("button");

button4.style.fontSize = "25px";
button4.innerText = "Change";

let store = 0;
button4.addEventListener("click", () => {
	let random = 0;
	do {
		random = randomInt(1, 5);
	} while (random == store);
	let element = document.getElementsByClassName("setDivs");
	if (random == 1) {
		for (let value of element) {
			value.style.backgroundColor = "green";
		}
	} else if (random == 2) {
		for (let value of element) {
			value.style.backgroundColor = "red";
		}
	} else if (random == 3) {
		for (let value of element) {
			value.style.backgroundColor = "blue";
		}
	} else if (random == 4) {
		for (let value of element) {
			value.style.backgroundColor = "gray";
		}
	} else if (random == 5) {
		for (let value of element) {
			value.style.backgroundColor = "orange";
		}
	}
	console.log("changed");
	store = random;
});

body.append(button4);

// Exercise 2.6
let wordArray = [
	"sunset",
	"orchid",
	"zephyr",
	"echo",
	"marble",
	"oasis",
	"quartz",
	"ember",
];

for (let i = 0; i < 6; i++) {
	let newElement = document.createElement("p");
	let randomWords = "";

	for (let j = 0; j < randomInt(1, 6); j++) {
		randomWords += wordArray[randomInt(0, wordArray.length)] + " ";
	}

	newElement.textContent = randomWords;
	body.append(newElement);
}

// Exercise 3
let input1 = document.createElement("input");
let input2 = document.createElement("input");
let button5 = document.createElement("button");
let error = "Invalid input. Must be a number.";

input1.setAttribute("type", "text");
input1.setAttribute("id", "rows");
input1.setAttribute("placeholder", "Input table Rows");
input2.setAttribute("type", "text");
input2.setAttribute("id", "cols");
input2.setAttribute("placeholder", "Input table Columns");
button5.setAttribute("id", "createTable");
button5.innerText = "Create Table";

button5.addEventListener("click", () => {
	// Convert string inputs to numbers
	let rows = Number(input1.value);
	let columns = Number(input2.value);
	if (typeof rows != "number" || typeof columns != "number") {
		body.append(error);
	} else {
		// Create table element
		let table = document.createElement("table");
		body.append(table);

		// Create and stylize Caption
		let caption = document.createElement("caption");
		caption.textContent = "This is your table";
		caption.style.fontWeight = 800;
		caption.style.fontSize = "30px";
		caption.style.margin = "10px auto 0";
		table.append(caption);

		// Create rows
		for (let i = 0; i < rows; i++) {
			let newRow = document.createElement("tr");
			newRow.setAttribute("class", "row");

			// Create columns
			for (let j = 0; j < columns; j++) {
				let newCol = document.createElement("td");
				newCol.setAttribute("class", "col");
				newRow.append(newCol);
			}

			table.append(newRow);
		}
	}
});

body.append(input1, input2, button5);
