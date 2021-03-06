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

//审批合同中的选中单选框
function onSelected(conid, approver) {
    if (document.getElementById("pass").checked == true) {
        let data = new FormData();
        let content = document.getElementById('approval_comments').value
        let state = true
        data.append("conid", conid)
        data.append("content", content)
        data.append("state", state)
        data.append("approver", approver)
        onCommitData('/ajax_updateContractApprovalmsg/', url_g, data)
    } else {
        let data = new FormData();
        let content = document.getElementById('approval_comments').value
        let state = false
        data.append("conid", conid)
        data.append("content", content)
        data.append("state", state)
        data.append("approver", approver)
        onCommitData('/ajax_updateContractApprovalmsg/', url_g, data)
    }
}


//重置签订合同中的签订信息
function onClearText() {
    document.getElementById('approval_comments').value = '';
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

        if (code.length > 6) {
            alert('邮编不能超过六位！');
            return;
        }
        if (account.length > 20) {
            alert('银行账户不能超过20位！');
            return;
        }
        data.append("cusid", cusid);
        data.append("cusname", cusname);
        data.append("address", address);
        data.append("tel", tel);
        data.append("code", code);
        data.append("fax", fax);
        data.append("bank", bank);
        data.append("account", account);

        onCommitData('/ajax_updateCustomermsg/', '/customer_info/', data);
    } else {
        alert('星号处不可为空！');
    }

}

//审批合同界面中的提交按钮
function onApprovalcontractCommit(conid, approver) {
    let data = new FormData();
    let information = document.getElementById('approval_comments').value;
    let state;

    if (document.getElementById("pass").checked == true) {
        state = document.getElementById('pass').value;
    } else {
        state = document.getElementById('reject').value;
    }
    print(state)
    data.append("conid", conid);
    data.append("state", state);
    data.append("information", information);
    data.append("approver", approver);
    onCommitData('/ajax_updateContractApprovalmsg/', '/contract_approving/', data);
}


//签订合同界面中的提交按钮
function onSigncontractCommit(conid, signer) {
    let data = new FormData();
    let information = document.getElementById('approval_comments').value;
    data.append("conid", conid);
    data.append("information", information);
    data.append("signer", signer);
    onCommitData('/ajax_updateContractSignmsg/', '/contract_signing/', data)
}

//起草合同界面中的提交按钮
function onAddContractCommit() {
    let data = new FormData();
    let contract_name = document.getElementById('contract_name').value;
    let cus_id = document.getElementById('customer').value;
    let start_time = document.getElementById('start_time').value;
    let end_time = document.getElementById('end_time').value;
    let contract_content = document.getElementById('contract_content').value;

    let file_upload = document.getElementById('file_upload').files[0];
    let extIndex;
    let extName;


    if (contract_name != '' && cus_id != '' && start_time != ''
        && end_time != '' && contract_content != '') {
        if (contract_name.length > 40) {
            alert('合同名不能超过40位！');
            return;
        }
        if (start_time > end_time) {
            alert('开始时间不能迟于结束时间！');
            return;
        }

        data.append("conname", contract_name);
        data.append("begintime", start_time);
        data.append("endtime", end_time);
        data.append("content", contract_content);
        data.append("cusid", cus_id);

        //添加附件
        if (file_upload != undefined) {
            extIndex = file_upload.name.lastIndexOf('.')
            extName = file_upload.name.substring(extIndex).toLowerCase();
            data.append('file', file_upload);
            data.append('filename', file_upload.name);
            data.append('filetype', extName);
        }


        onCommitData('/ajax_addContract/', '/draftcontract/', data);

    } else {
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


//合同定稿界面中的提交按钮
function onFinalContractCommit(conid) {
    let data = new FormData();
    let content = document.getElementById('contract_content').value;
    data.append("conid", conid)
    data.append("content", content)
    onCommitData('/ajax_updateContractFinalMsg/', '/pending_contract/', data)
}

//合同会签页面中的提交按钮
function onContersignContractCommit(conid, contersigner) {
    let data = new FormData();
    let single_content = document.getElementById('countersign_comments').value;
    data.append("conid", conid)
    data.append("single_content", single_content)
    data.append("contersigner", contersigner)
    onCommitData('/ajax_updateContractCountersignMsg/', url_g, data)

}


// function ondownloadFile(conid) {
//     let data = new FormData();
//
//     data.append('conid',conid);
//     let xmltype;
//     if (window.XMLHttpRequest) {
//         //  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
//         xmltype = new XMLHttpRequest();
//     } else {
//         // IE6, IE5 浏览器执行代码
//         xmltype = new ActiveXObject("Microsoft.XMLHTTP");
//     }
//     xmltype.onreadystatechange = function () {
//         if (xmltype.readyState == 4 && xmltype.status == 200) {
//             // document.getElementById("function_view").innerHTML = xmltype.responseText;
//         }
//     }
//
//     xmltype.open("POST", '/downloadFile/');
//     xmltype.send(data);
// }