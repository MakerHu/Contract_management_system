function onAllocationCommit(conid) {


    let data_countersign = new Array();
    let data_approve = new Array();
    let data_sign = new Array();
    let data = new FormData();

    let obj_countersign = document.getElementById("countersign_have")
    let obj_approve = document.getElementById("approve_have")
    let obj_sign = document.getElementById("sign_have")

    let count_countersign = obj_countersign.options.length
    let count_approve = obj_approve.options.length
    let count_sign = obj_sign.options.length

    for(let i= 0;i<count_countersign;i++){
        let text = obj_countersign.options[i].value;
        data_countersign.push(text);
    }
    let data1 = JSON.stringify(data_countersign);
    data.append("data_countersign", data1);

    for(let i= 0;i<count_approve;i++){
        let text = obj_approve.options[i].value;
        data_approve.push(text);
    }
    let data2 = JSON.stringify(data_approve);
    data.append("data_approve", data2);

    for(let i= 0;i<count_sign;i++){
        let text = obj_sign.options[i].value;
        data_sign.push(text);
    }
    let data3 = JSON.stringify(data_sign);
    data.append("data_sign", data3);

    data.append('conid', conid);

    onCommitData('/ajax_updateAllocation/',url_g, data);
}





//会签人
function onDeleteCountersignWillOption(txt){
    console.log(txt);
    var obj = document.getElementById("countersign_will")
    var count = obj.options.length
    console.log(count);
    for(var i= 0;i<count;i++){
        var text = obj.options[i].value;
        if(txt==text){
            obj.options.remove(i);
            console.log("text");
            console.log(text);
            console.log(i);
            var selectobj = document.getElementById('countersign_have');
            selectobj.options.add(new Option(txt,txt));
        }
    }
}

function onDeleteCountersignHaveOption(txt){
    var obj = document.getElementById('countersign_have')
    var count = obj.options.length
    // console.log(count);
    for(var i= 0;i<count;i++){
        var text = obj.options[i].value;
        if(text==txt){
            obj.options.remove(i);
            var selectobj = document.getElementById('countersign_will');
            selectobj.options.add(new Option(txt,txt));
        }
    }
}

//审批人
function onDeleteApproveWillOption(txt){
    console.log(txt);
    var obj = document.getElementById("approve_will")
    var count = obj.options.length
    console.log(count);
    for(var i= 0;i<count;i++){
        var text = obj.options[i].value;
        if(txt==text){
            obj.options.remove(i);
            console.log("text");
            console.log(text);
            console.log(i);
            var selectobj = document.getElementById('approve_have');
            selectobj.options.add(new Option(txt,txt));
        }
    }
}

function onDeleteApproveHaveOption(txt){
    var obj = document.getElementById('approve_have')
    var count = obj.options.length
    // console.log(count);
    for(var i= 0;i<count;i++){
        var text = obj.options[i].value;
        if(text==txt){
            obj.options.remove(i);
            var selectobj = document.getElementById('approve_will');
            selectobj.options.add(new Option(txt,txt));
        }
    }
}

//签订人
function onDeleteSignWillOption(txt){
    console.log(txt);
    var obj = document.getElementById("sign_will")
    var count = obj.options.length
    console.log(count);
    for(var i= 0;i<count;i++){
        var text = obj.options[i].value;
        if(txt==text){
            obj.options.remove(i);
            console.log("text");
            console.log(text);
            console.log(i);
            var selectobj = document.getElementById('sign_have');
            selectobj.options.add(new Option(txt,txt));
        }
    }
}

function onDeleteSignHaveOption(txt){
    var obj = document.getElementById('sign_have')
    var count = obj.options.length
    // console.log(count);
    for(var i= 0;i<count;i++){
        var text = obj.options[i].value;
        if(text==txt){
            obj.options.remove(i);
            var selectobj = document.getElementById('sign_will');
            selectobj.options.add(new Option(txt,txt));
        }
    }
}

function delRepeatUsername(){
    let left_obj_countersign = document.getElementById("countersign_will")
    let left_obj_approve = document.getElementById("approve_will")
    let left_obj_sign = document.getElementById("sign_will")
        alert('1111');
    let left_count_countersign = obj_countersign.options.length
    let left_count_approve = obj_approve.options.length
    let left_count_sign = obj_sign.options.length

    let right_obj_countersign = document.getElementById("countersign_have")
    let right_obj_approve = document.getElementById("approve_have")
    let right_obj_sign = document.getElementById("sign_have")

    let right_count_countersign = obj_countersign.options.length
    let right_count_approve = obj_approve.options.length
    let right_count_sign = obj_sign.options.length

    for(var i= 0;i<left_count_countersign;i++){
        for(var j= 0;i<right_count_countersign;i++){
            var left_text = left_obj_countersign.options[i].value;
            var right_text = right_obj_countersign.options[j].value;
            if(left_text==right_text){
                left_obj_countersign.options.remove(i);
            }
        }
    }

    for(var i= 0;i<left_count_approve;i++){
        for(var j= 0;i<right_count_approve;i++){
            var left_text = left_obj_approve.options[i].value;
            var right_text = right_obj_approve.options[j].value;
            if(left_text==right_text){
                left_obj_approve.options.remove(i);
            }
        }
    }

    for(var i= 0;i<left_count_sign;i++){
        for(var j= 0;i<right_count_sign;i++){
            var left_text = left_obj_sign.options[i].value;
            var right_text = right_obj_sign.options[j].value;
            if(left_text==right_text){
                left_obj_sign.options.remove(i);
            }
        }
    }
}


