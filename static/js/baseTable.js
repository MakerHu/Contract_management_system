let searchMsg_g = "";

function onSearchBtn(url, pageNum=1) {
    url_g=url;
    let searchMsg = document.getElementById("search_input").value;
    searchMsg_g = searchMsg;
    let data = new FormData();
    data.append("searchMsg", searchMsg);
    data.append("pageNum", pageNum);

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
            document.getElementById("function_view").innerHTML = xmltype.responseText;
        }
    }

    xmltype.open("POST", url);
    xmltype.send(data);
}

var current_page_g = 1;

function onPageClick(obj) {
    current_page_g = obj.innerText;
    // reload_function_view('/right/', titlename_g, pageNum = obj.innerText)
    onSearchBtn(url_g, pageNum=obj.innerText)
}

function onPrePageClick() {
    if (current_page_g > 1) {
        current_page_g--;
        // reload_function_view('/right/', titlename_g, pageNum = current_page_g)
        onSearchBtn(url_g, pageNum=current_page_g)
    }
}

function onNextPageClick() {
    current_page_g++;
    // reload_function_view('/right/', titlename_g, pageNum = current_page_g)
    onSearchBtn(url_g, pageNum=current_page_g)

}