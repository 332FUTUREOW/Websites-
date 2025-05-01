document.querySelector("button").addEventListener("click", function() {
  alert("Button clicked!");
});
const greeting = document.createElement('h2');
const hour = new Date().getHours();

if (hour < 12) {
    greeting.textContent = "Good Morning!";
} else if (hour < 18) {
    greeting.textContent = "Good Afternoon!";
} else {
    greeting.textContent = "Good Evening!";
}

document.body.prepend(greeting);
