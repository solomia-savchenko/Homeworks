let number = document.getElementById("number");
const btn = document.getElementById("btn");

function calculateSquare(number) {
    return number * number;
}

function calculateCube(number) {
    return number * number * number;
}

function calculateRemainderBy5(number) {
    return number % 5;
}

btn.addEventListener("click", function() {
    const value = Number(number.value);

    const resultOfSquare = calculateSquare(value);
    const resultOfCube = calculateCube(value);
    const resultOfRemainderBy5 = calculateRemainderBy5(value);

    console.log(`Square of number ${value} is ${resultOfSquare}. Cube: ${resultOfCube}. Remainder by 5: ${resultOfRemainderBy5}`);
});