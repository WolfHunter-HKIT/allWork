import { result } from "./data.js";

let favorites = [];
let uniqueArray = [];

function favoriteMovies(...ids) {
	// Makes all ids values unique (no duplicates)
	uniqueArray = ids.filter(
		(value, index, self) => self.indexOf(value) === index
	);
	console.log(uniqueArray);
	// Runs a loop for each item in uniqueArray
	for (let item of uniqueArray) {
		// Runs a loop for each item in the books object
		for (let element in result) {
			// Checks if any of the items match, then pushes it to favorites array
			if (result[element].id == item) {
				favorites.push([result[element].id, result[element].title]);
			}
		}
	}
	// Sets local storage favorites
	localStorage.setItem("favorites", JSON.stringify(favorites));
}

function getFavorites() {
	// Gets favorites as an object
	let list = JSON.parse(localStorage.getItem("favorites"));
	// Runs a loop for each element in list and displays it in console log
	for (let element of list) {
		console.log(`ID: ${element[0]}, Title: ${element[1]}`);
	}
}

function removeFavorites(...ids) {
	// Makes all ids values unique (no duplicates)
	uniqueArray = ids.filter(
		(value, index, self) => self.indexOf(value) === index
	);
	console.log(favorites);
	// Runs a loop for each favorites array element
	for (let i = 0; i < favorites.length; i++) {
		// Runs a loop for each element in Unique array to check if it matches with the elements ran from the loop above.
		for (let element of uniqueArray) {
			console.log(favorites[i][0] == element);
			// If the elements match, the values from favorites array get removed
			if (favorites[i][0] == element) {
				favorites.splice(favorites.indexOf(element), 1);
				console.log("spliced");
			}
		}
	}
	// Sets local storage favorites
	localStorage.setItem("favorites", JSON.stringify(favorites));
}

favoriteMovies(414906, 284054, 361743, 284054);
getFavorites();
removeFavorites(414906);
