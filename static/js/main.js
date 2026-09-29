// Phase 0 foundation script — proves static JS is served.
document.addEventListener("DOMContentLoaded", function () {
    var el = document.getElementById("js-check");
    if (el) {
        el.textContent = "JavaScript loaded.";
    }
});
