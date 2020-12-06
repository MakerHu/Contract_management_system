function onCommitDraftContract(url) {
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

//用户填表的数据传输
// 其中url是后端要调用的函数的url
// return_url,是操作完成后返回的界面
// data要传输到后端的数据
function onCommitData(url,return_url, data) {
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
            // document.getElementById("function_view").innerHTML = xmltype.responseText;
            reload_function_view(return_url, titlename_g ,pageNum=1);
        }
    }

    xmltype.open("POST", url);
    xmltype.send(data);
}

//授权界面中的提交按钮
function onAuthorityCommit(username) {
    let data = new FormData();
    let form = document.querySelector('form');
    let new_rolename = form.querySelector("input[name='authority']:checked").value;
    data.append("new_rolename", new_rolename);
    data.append("username", username);
    onCommitData('/ajax_updateAuthority/',url_g, data)
}

function onAuthorityCancel() {
    reload_function_view(url_g, titlename_g ,pageNum=1);
}