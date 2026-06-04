const bnt = document.getElementById("btn")
let number = document.getElementById("number")

function evenOrOdd (number) {
    if (number % 2 === 0) {
        return "Even";
    } else {
        return "Odd";
    }
}

btn.addEventListener("click" , function() {
    const value = Number(number.value);

    const result = evenOrOdd(value);
    console.log(`Number ${value} is ${result}`)
})