import axios from 'axios';

let loadingIcon = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin: auto; margin-top: 50px; background: rgb(240, 248, 255); display: block; shape-rendering: auto;" width="200px" height="200px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
<circle cx="50" cy="50" fill="none" stroke="#e15b64" stroke-width="10" r="35" stroke-dasharray="164.93361431346415 56.97787143782138">
  <animateTransform attributeName="transform" type="rotate" repeatCount="indefinite" dur="1s" values="0 50 50;360 50 50" keyTimes="0;1"></animateTransform>
</circle>`

//let value = document.getElementById("accuracy-value");
let submitButton = document.getElementById("submitButton");
let textArea = document.getElementById("text");
let url = "http://localhost:5000";
let containerBody = document.querySelector(".container-body")

submitButton.addEventListener("click", () => {
    let text = textArea.value
    if (text.length == 0) return
    containerBody.innerHTML = loadingIcon;
    axios.post(url, {email: text}).then((res) => {
        containerBody.innerHTML = `Accuracy: ${res.data}%`;
    });
});