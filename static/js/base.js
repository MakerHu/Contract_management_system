function list() {
    var body = document.getElementsByTagName("body")[0]
    var aside = document.getElementsByTagName("aside")[0]
    if (aside.clientWidth <= 40) {
        body.className = ""
    } else if (aside.clientWidth > 40) {
        console.log("side")
        body.className = "minibody"
    }
}

//点击首页按钮
function onhome() {
    window.location.href = "/index/";
}

//刷新功能界面
function reload_function_view(url, titlename) {
    var xmlhttp;
    if (window.XMLHttpRequest) {
        //  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlhttp = new XMLHttpRequest();
    } else {
        // IE6, IE5 浏览器执行代码
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                document.getElementById("function_view").innerHTML=xmlhttp.responseText;
                document.title=titlename;
        }
    }

    xmlhttp.open("GET", url);
    xmlhttp.send();
}

//打开合同起草栏
var state = 1;

function onOpenContractDraft() {
    if (state) {
        state = 0;
        document.getElementById("draft_contract").style.display = "block";
        document.getElementById("pending_contract").style.display = "block";
        document.getElementById("finalized_contract").style.display = "block";
        document.getElementById("process_query").style.display = "block";
    } else {
        state = 1
        document.getElementById("draft_contract").style.display = "none";
        document.getElementById("pending_contract").style.display = "none";
        document.getElementById("finalized_contract").style.display = "none";
        document.getElementById("process_query").style.display = "none";
    }

}

