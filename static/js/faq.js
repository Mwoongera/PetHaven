function toggleAnswer(button) {
     const answer = button.previousElementSibling;
     if (answer.style.display === "none" || answer.style.display === "") {
         answer.style.display = "block";
         button.textContent = "Hide Answer";
     } else {
         answer.style.display = "none";
         button.textContent = "Show Answer";
     }
 }
 