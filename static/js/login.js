var button = document.querySelector("#change-view-button");

button.addEventListener("click", function() {
  var mainPage = document.querySelector("#main-page");
  var subPage = document.querySelector("#sub-page");

  if (mainPage.style.display !== "none") {
    mainPage.style.display = "none";
    subPage.style.display = "block";
  }
  else{
    mainPage.style.display = "block";
    subPage.style.display = "none";
  }
});
