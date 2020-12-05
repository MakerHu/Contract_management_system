function onDeleteWillOption(txt){
    console.log(txt);
    var obj = document.getElementById("will")
    var count = obj.options.length
    console.log(count);
    for(var i= 0;i<count;i++){
        var text = obj.options[i].value;
        if(txt==text){
            obj.options.remove(i);
            console.log("text");
            console.log(text);
            console.log(i);
            var selectobj = document.getElementById('have');
            selectobj.options.add(new Option(txt,txt));
        }
    }
}

function onDeleteHaveOption(txt){
    var obj = document.getElementById("have")
    var count = obj.options.length
    // console.log(count);
    for(var i= 0;i<=count;i++){
        var text = obj.options[i].value;
        if(text==txt){
            obj.options.remove(i);
            var selectobj = document.getElementById('will');
            selectobj.options.add(new Option(txt,txt));
        }
    }
}
