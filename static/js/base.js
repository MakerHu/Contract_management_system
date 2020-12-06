function list() {
    var body = document.getElementsByTagName("body")[0];
    var aside = document.getElementsByTagName("aside")[0];
    var listtext_2 = document.getElementsByClassName("listtext_2");
    var stretch = document.getElementsByClassName("stretch");
    if (aside.clientWidth <= 40) {
        body.className = "";
    } else if (aside.clientWidth > 40) {
        state =1;
        state_1 =1;
        state_2 =1;
        state_3 =1;
        state_4 =1;
        state_5 =1;
        for (var i = 0; i < stretch.length; i++) {
            stretch[i].innerHTML="&#9654;";
        }
        for (var i = 0; i < listtext_2.length; i++) {
            listtext_2[i].style.display="none";
        }
        console.log("side");
        body.className = "minibody";
    }
}

//点击首页按钮
// function onhome() {
//     window.location.href = "/index/";
// }

//刷新功能界面
let titlename_g = "";
let url_g="";
function reload_function_view(url, titlename ,pageNum=1) {
    url_g=url;
    let data = new FormData();
    data.append("pageNum", pageNum);

    titlename_g = titlename
    let xmlhttp;
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

    xmlhttp.open("POST", url);
    xmlhttp.send(data);
}

//打开合同起草栏
var state = 1;
function onOpenContractDraft() {
    if (state) {
        state = 0;
        document.getElementById("contract_draft").innerHTML="&#9660;";
        document.getElementById("draft_contract").style.display = "block";
        document.getElementById("pending_contract").style.display = "block";
        document.getElementById("finalized_contract").style.display = "block";
        document.getElementById("process_query").style.display = "block";
    } else {
        state = 1;
        document.getElementById("contract_draft").innerHTML="&#9654;";
        document.getElementById("draft_contract").style.display = "none";
        document.getElementById("pending_contract").style.display = "none";
        document.getElementById("finalized_contract").style.display = "none";
        document.getElementById("process_query").style.display = "none";
    }
}

//打开合同会签栏
var state_1 = 1;
function onOpenContractCountersign() {
    if (state_1) {
        state_1 = 0;
        document.getElementById("contract_countersign").innerHTML="&#9660;";
        document.getElementById("countersigning_contract").style.display = "block";
        document.getElementById("countersigned_contract").style.display = "block";
    } else {
        state_1 = 1;
        document.getElementById("contract_countersign").innerHTML="&#9654;";
        document.getElementById("countersigning_contract").style.display = "none";
        document.getElementById("countersigned_contract").style.display = "none";
    }
}

//打开合同审批栏
var state_2 = 1;
function onOpenContractApproval() {
    if (state_2) {
        state_2 = 0;
        document.getElementById("contract_approval").innerHTML="&#9660;";
        document.getElementById("contract_approving").style.display = "block";
        document.getElementById("contract_approved").style.display = "block";
    } else {
        state_2 = 1;
        document.getElementById("contract_approval").innerHTML="&#9654;";
        document.getElementById("contract_approving").style.display = "none";
        document.getElementById("contract_approved").style.display = "none";
    }
}

//打开合同签订栏
var state_3 = 1;
function onOpenContractSign() {
    if (state_3) {
        state_3 = 0;
        document.getElementById("contract_sign").innerHTML="&#9660;";
        document.getElementById("contract_signing").style.display = "block";
        document.getElementById("contract_signed").style.display = "block";
    } else {
        state_3 = 1;
        document.getElementById("contract_sign").innerHTML="&#9654;";
        document.getElementById("contract_signing").style.display = "none";
        document.getElementById("contract_signed").style.display = "none";
    }
}


//打开客户管理栏
var state_4 = 1;
function onOpenCustomerManage() {
    if (state_4) {
        state_4 = 0;
        document.getElementById("customer_manage").innerHTML="&#9660;";
        document.getElementById("customer_info").style.display = "block";
        document.getElementById("add_customer").style.display = "block";
    } else {
        state_4 = 1;
        document.getElementById("customer_manage").innerHTML="&#9654;";
        document.getElementById("customer_info").style.display = "none";
        document.getElementById("add_customer").style.display = "none";
    }
}

//打开权限管理栏
var state_5 = 1;
function onOpenRightManage() {
    if (state_5) {
        state_5 = 0;
        document.getElementById("right_manage").innerHTML="&#9660;";
        document.getElementById("newuser_authorize").style.display = "block";
        document.getElementById("manage_right").style.display = "block";
    } else {
        state_5 = 1;
        document.getElementById("right_manage").innerHTML="&#9654;";
        document.getElementById("newuser_authorize").style.display = "none";
        document.getElementById("manage_right").style.display = "none";
    }
}

//打开合同分配栏
var state_6 = 1;
function onOpenContractDistribute() {
    if (state_6) {
        state_6 = 0;
        document.getElementById("contract_distribute").innerHTML="&#9660;";
        document.getElementById("contract_distributing").style.display = "block";
        document.getElementById("contract_distributed").style.display = "block";
    } else {
        state_6 = 1;
        document.getElementById("contract_distribute").innerHTML="&#9654;";
        document.getElementById("contract_distributing").style.display = "none";
        document.getElementById("contract_distributed").style.display = "none";
    }
}

