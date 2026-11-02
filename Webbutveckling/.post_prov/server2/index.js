const express = require("express");

const app = express();
app.listen(4000);

app.use(express.static("public"));

app.get("/", function (req, res) {
    res.send(render("<h2>home</h2>"))
});

app.get("/about", function (req, res) {
    res.send(render("<p>abot</p>"))
});

app.get("/contact", function (req, res) {
    res.send(render("<p>cantokt</p>"))
});


function render(content) {
    /* ghemta tepempealte */
    let html = require("fs").readFileSync("template.html").toString();
    html = html.replace("%content%", content);
    return html;
}