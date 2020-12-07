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
function onCommitData(url, return_url, data) {
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
            alert("操作成功！");
            reload_function_view(return_url, titlename_g, pageNum = 1);
        }
    }

    xmltype.open("POST", url);
    xmltype.send(data);
}

//返回上一个界面
function onReturnPrePage() {
    reload_function_view(url_g, titlename_g, pageNum = 1);
}

//重置签订合同中的签订信息
function onClearText() {
    document.getElementById('approval_comments').value= '';
}

//授权界面中的提交按钮
function onAuthorityCommit(username) {
    let data = new FormData();
    let form = document.querySelector('form');
    let new_rolename = form.querySelector("input[name='authority']:checked").value;
    data.append("new_rolename", new_rolename);
    data.append("username", username);
    onCommitData('/ajax_updateAuthority/', url_g, data)
}

//添加客户界面中的提交按钮
function onAddCustomerCommit(cusid) {
    let data = new FormData();
    let cusname = document.getElementById('cusname').value;
    let address = document.getElementById('address').value;
    let tel = document.getElementById('tel').value;

    if (cusname != '' && address != '' && tel != '') {
        let code = document.getElementById('code').value;
        let fax = document.getElementById('fax').value;
        let bank = document.getElementById('bank').value;
        let account = document.getElementById('account').value;

        if (code.length>6) {
            alert('邮编不能超过六位！');
            return;
        }
        if (account.length>20) {
            alert('银行账户不能超过20位！');
            return;
        }
        data.append("cusid",cusid);
        data.append("cusname", cusname);
        data.append("address", address);
        data.append("tel", tel);
        data.append("code", code);
        data.append("fax", fax);
        data.append("bank", bank);
        data.append("account", account);

        onCommitData('/ajax_updateCustomermsg/', '/customer_info/', data);
    }else{
        alert('星号处不可为空！');
    }

}

//签订合同界面中的提交按钮
function onSigncontractCommit(conid) {
    let data = new FormData();
    let information = document.getElementById('approval_comments').value;
    data.append("conid", conid)
    data.append("information", information)
    onCommitData('/ajax_updateContractSignmsg/','/contract_signing/', data)
}