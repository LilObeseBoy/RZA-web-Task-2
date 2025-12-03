function hideError() {
    const box = document.getElementById("errorBox");
    if (!box) return;
    box.style.animation = "fadeout 0.5s forwards";
    setTimeout(() => box.remove(), 500);
}


window.addEventListener("load", () => {
    const box = document.getElementById("errorBox");
    if (box) {
        setTimeout(hideError, 5000);
    }
});