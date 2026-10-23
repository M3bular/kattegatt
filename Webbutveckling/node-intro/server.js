const http = require("http");

http.createServer(handleServer).listen(345);


function handleServer(req, res) {

    if(req.url == "/") return res.end(render("HOME"));
    if(req.url == "/about") return res.end(render("ABOUT"));
    if(req.url == "/faq") return res.end(render("FAQ"));
    else return res.end("404");

}



function render(content){

    const fs = require("fs");
    let html = fs.readFileSync("template.html").toString();
    html = html.replace("%va%",content);
    return html;
}