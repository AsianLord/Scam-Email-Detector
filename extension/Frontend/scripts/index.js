const axios = require("axios")

value = document.getElementById("accuracy-value")

value.innerHTML = "10";

axios.get('http://localhost:5000/').then((res) => {
    console.log(res);
});