const toggleBtn = document.getElementById("searchToggle");
const searchBox = document.getElementById("searchBox");

toggleBtn.addEventListener("click", () => {
  searchBox.classList.toggle("d-none");
});

