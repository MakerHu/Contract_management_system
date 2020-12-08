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

//起草合同界面中的提交按钮
function onAddContractCommit() {
    let data = new FormData();
    let contract_name = document.getElementById('contract_name').value;
    let cus_id = document.getElementById('customer').value;
    let start_time = document.getElementById('start_time').value;
    let end_time = document.getElementById('end_time').value;
    let contract_content = document.getElementById('contract_content').value;

    var dP = /^(?:(?!0000)[0-9]{4}-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-8])|(?:0[13-9]|1[0-2])-(?:29|30)|(?:0[13578]|1[02])-31)|(?:[0-9]{2}(?:0[48]|[2468][048]|[13579][26])|(?:0[48]|[2468][048]|[13579][26])00)-02-29)$/;
    if(dP.test(start_time)&&dP.test(end_time)){

    }
    else{
         alert('请输入合法的日期(格式：YYYY-MM-DD)！');
         return;
    }
    if(start_time>end_time){
        alert('开始时间不能迟于结束时间！');
        return;
    }
    if (contract_name != '' && cus_id != '' && start_time != ''
       && end_time != '' && contract_content != '') {
        if (contract_name.length>40) {
            alert('合同名不能超过40位！');
            return;
        }
        var data1 = new FormData();
        data1.append("cusid", cus_id);

        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.addEventListener("readystatechange", function () {
            if (this.readyState === 4) {
            var json = JSON.parse(this.responseText);
            console.log(this.responseText);
            if (json.exists_customer == 'success') {
                data.append("conname", contract_name);
                data.append("begintime", start_time);
                data.append("endtime", end_time);
                data.append("content", contract_content);
                data.append("cusid", cus_id);
                onCommitData('/ajax_addContract/', '/draftcontract/', data);
            } else {
                alert('没有该客户！');
                return;
            }
        }
    });
        xhr.open("POST", "/ajax_check_cusid/");
        xhr.send(data1);

    }else{
        alert('星号处不可为空！');
    }

}

function CheckCusidAjax() {
    let cus_id = document.getElementById('customer').value;

    var data = new FormData();
    data.append("cusid", cus_id);
    console.log(data);

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            var json = JSON.parse(this.responseText);
            console.log(this.responseText);
            if (json.exists_customer == 'success') {
                document.getElementById("hide3").style.display = "block";
            } else {
                document.getElementById("hide3").style.display = "none";
            }
        }
    });
    xhr.open("POST", "/ajax_check_cusid/");
    xhr.send(data);
}