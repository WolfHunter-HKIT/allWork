export default function randomInt(start, end) {
	if (start > end) {
		let temp = start;
		start = end;
		end = temp;
	}
	return Math.floor(Math.random() * (end - start) + start);
}
