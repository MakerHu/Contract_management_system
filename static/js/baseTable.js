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
    onSearchBtn(url_g, pageNum=obj.innerText);
}

function onPrePageClick() {
    if (current_page_g > 1) {
        current_page_g--;
        // reload_function_view('/right/', titlename_g, pageNum = current_page_g)
        onSearchBtn(url_g, pageNum=current_page_g);
    }
}

function onNextPageClick() {
    current_page_g++;
    // reload_function_view('/right/', titlename_g, pageNum = current_page_g)
    onSearchBtn(url_g, pageNum=current_page_g);

}

//
function data_edit_page_ajax(url,data){
    // let data = new FormData();
    // data.append("keyword", keyword);

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

//授权按钮
function onAuthorizationClick(keyword) {
    // let node = obj.parentNode.parentNode;
    // let keyword = node.children[0].innerHTML
    // alert(keyword);
    let data = new FormData();
    data.append("keyword", keyword);
    data_edit_page_ajax('/data_authorize/',data);
}

//定稿按钮
function onFinalizeClick(keyword) {
    // let node = obj.parentNode.parentNode;
    // let keyword = node.children[0].innerHTML
    let data = new FormData();
    data.append("keyword", keyword);
    data_edit_page_ajax('/contract_finalize/',data);
    //alert(keyword);
}

//会签按钮
function onCountersignClick(keyword,contersigner) {
    let data = new FormData();
    data.append("keyword", keyword);
    data.append("contersigner", contersigner);
    data_edit_page_ajax('/contract_countersign/',data);
}

//审批按钮
function onApprovalClick(keyword,approver) {
    // let node = obj.parentNode.parentNode;
    // let keyword = node.children[0].innerHTML;
    //alert(keyword);
    let data = new FormData();
    data.append("keyword", keyword);
    data.append("approver", approver);
    data_edit_page_ajax('/data_contract_approval/',data);
}

//签订按钮
function onSignClick(keyword,signer) {
    // let node = obj.parentNode.parentNode;
    // let keyword = node.children[0].innerHTML;
     // alert(keyword);
    let data = new FormData();
    data.append("keyword", keyword);
    data.append("signer", signer);
    data_edit_page_ajax('/data_contract_sign/',data);

}

//分配按钮
//待分配合同按钮
function onDistribute(keyword) {
    // let node = obj.parentNode.parentNode;
    // let keyword = node.children[0].innerHTML;
    let data = new FormData();
    data.append("keyword", keyword);
    data_edit_page_ajax('/data_allocation/',data);
}

//已分配合同详情按钮
function onContractDistributeDetail(keyword){
    let data = new FormData();
    data.append("keyword", keyword);
    data_edit_page_ajax('/data_allocation/',data);
}

//客户详情按钮
function onCostomerDetail(keyword){
    let data = new FormData();
    data.append("keyword", keyword);
    data_edit_page_ajax('/data_customermsg/',data);
}

//合同详情按钮
function onContractDetail(keyword){
    let data = new FormData();
    data.append("keyword", keyword);
    data_edit_page_ajax('/contractDetail/',data);
}