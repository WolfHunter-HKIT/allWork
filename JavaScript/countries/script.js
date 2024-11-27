import { countries } from "./countries.js";

//  Fetches countries from local storage
let storageCountries = localStorage.getItem("countries");
// Creates an empty array to use for LS
let pushArray = [];
// Checks if countries inside LS has any values
if (storageCountries == null) {
	// Runs loop through all values inside our countries data file
	for (let i = 0; i < countries.length; i++) {
		// Creates error messages
		let nameError = `Data about Name was not found...`;
		let capitalError = `Data about Capital was not found...`;
		// Checks if Country Name and Country Capital both any values
		if (
			(countries[i].name.common == "" ||
				countries[i].name.common == null) &&
			(countries[i].capital == "" || countries[i].capital == null)
		) {
			pushArray.push([i + " Data", nameError, capitalError]);
		}
		// Checks if only Country Capital has any values
		else if (countries[i].capital == "" || countries[i].capital == null) {
			pushArray.push([
				i + " Data",
				countries[i].name.common,
				capitalError,
			]);
		}
		// Checks if only Country Name has any values
		else if (
			countries[i].name.common == "" ||
			countries[i].name.common == null
		) {
			pushArray.push([i + " Data", nameError, countries[i].capital]);
		}
		// Pushes data index, Country Name and Country Capitals into push array
		else {
			pushArray.push([
				i + " Data",
				countries[i].name.common,
				countries[i].capital,
			]);
		}
	}
	localStorage.setItem("countries", JSON.stringify(pushArray));
}

function displayCountries() {
	// Displays values from LS array to user (Console.log)
	for (let i = 0; i < pushArray.length; i++) {
		console.log(`${pushArray[i][0]}:\n`); // Data index
		console.log(`Country name: ${pushArray[i][1]}\n`); // Country Names
		console.log(`Capital: ${pushArray[i][2]}\n`); // Country Capital Names
		console.log(`--------------------------------\n`); // Divider
	}
}

// Runs function to display countries from localStorage
displayCountries();
// Clears localStorage (Debugging)
localStorage.clear();
