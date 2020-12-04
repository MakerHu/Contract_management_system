function onSearchBtn(url) {
    let search_value = document.getElementById("search_input").value;

    let data = new FormData();
    data.append("search_value", search_value);

    let xmltype;
    if (window.XMLHttpRequest) {
        //  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmltype = new XMLHttpRequest();
    } else {
        // IE6, IE5 浏览器执行代码
        xmltype = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmltype.onreadystatechange = function () {
        if (xmltype.readyState == 4 && xmltype.status == 200) {
            let json = JSON.parse(this.responseText);
        }
    }

    xmltype.open("GET", url);
    xmltype.send();
}