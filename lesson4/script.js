const canvas = document.getElementById("c");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let progress = 0;

function drawBranch(x, y, len, angle, depth) {
    if (depth === 0 || len < 2) return;

    const x2 = x + Math.cos(angle) * len;
    const y2 = y + Math.sin(angle) * len;

    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x2, y2);
    ctx.strokeStyle = `hsl(${depth * 25}, 80%, 60%)`;
    ctx.lineWidth = depth * 1.2;
    ctx.stroke();

    drawBranch(x2, y2, len * 0.75, angle - 0.55, depth -1);
    drawBranch(x2, y2, len * 0.75, angle + 0.55, depth -1);
};

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const maxDepth = 10;

    ctx.lineCap = "round";

    drawBranch(
        canvas.width / 2,
        canvas.height,
        canvas.height * 0.25,
        -Math.PI / 2,
        Math.floor(progress * maxDepth)
    )

    progress += 0.02;

    if (progress <= 1) {
        requestAnimationFrame(animate);
    }
};

function start() {
    progress = 0;
    animate();
};

window.addEventListener("DOMContentLoaded", start);
window.addEventListener("click", start)

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    start();
})