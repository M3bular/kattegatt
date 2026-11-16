function searchContent(s) {
    s = s.toLowerCase();
    const content = document.querySelectorAll(".content")
    for (div of content) {
        div.classList.remove("hidden");
        let heading = div.children[0].innerText.toLowerCase();
        let text = div.children[1].innerText.toLowerCase();
        if(heading.search(s)<0 && text.search(s)<0){
            div.classList.add("hidden");
        }
    }
}