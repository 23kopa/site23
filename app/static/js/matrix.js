export function initMatrixEffect() {
    const c = document.getElementById("matrix");
    if (!c) return;

    const ctx = c.getContext("2d");
    c.height = window.innerHeight;
    c.width = window.innerWidth;

    const letters = "アァイィウエカキクケコサシスセソ0123456789";
    const fontSize = 18;
    const columns = c.width / fontSize;
    const drops = Array(Math.floor(columns)).fill(1);

    function draw() {
        ctx.fillStyle = "rgba(0, 0, 0, 0.1)";
        ctx.fillRect(0, 0, c.width, c.height);

        ctx.fillStyle = "rgba(0, 255, 0, 0.1)";
        ctx.font = `${fontSize}px monospace`;

        for (let i = 0; i < drops.length; i++) {
            const text = letters[Math.floor(Math.random() * letters.length)];
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
            if (drops[i] * fontSize > c.height && Math.random() > 0.995) drops[i] = 0;
            drops[i]++;
        }
        setTimeout(() => requestAnimationFrame(draw), 50);
    }

    draw();

    window.addEventListener("resize", () => {
        c.width = window.innerWidth;
        c.height = window.innerHeight;
    });
}

document.querySelectorAll('.btn-auth').forEach(btn => {
    btn.addEventListener('click', function (e) {
        const ripple = document.createElement('span');
        ripple.classList.add('ripple');
        ripple.style.left = `${e.offsetX}px`;
        ripple.style.top = `${e.offsetY}px`;
        this.appendChild(ripple);
        setTimeout(() => ripple.remove(), 600);
    });
});
