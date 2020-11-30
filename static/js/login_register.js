/*function CheckPassword(inputtext)
{
    // alert(inputtext);
    var passw = /^[A-Za-z]\w{7,15}$/;
    if(inputtext.value.match(passw))
    {
        document.getElementById("hide1").style.display="none";
        return true;
    }
    else
    {
        document.getElementById("hide1").style.display="block";
        return false;
    }
}*/

function onlogin() {
    var username = document.getElementById("login-username").value;
    var password = document.getElementById("login-password").value;
    console.log(username);
    console.log(password);

    var data = new FormData();
    data.append("username",username);
    data.append("password",password);
    console.log(data);

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            var json = JSON.parse(this.responseText);
            console.log(this.responseText);
            if (json.exists_username == 'fail') {
                document.getElementById("hide1").style.display = "block";
            } else {
                document.getElementById("hide1").style.display = "none";
            }
            if (json.right_password == 'fail') {
                document.getElementById("hide2").style.display = "block";
            } else {
                document.getElementById("hide2").style.display = "none";
            }
            if(json.exists_username == 'success'&&json.right_password == 'success'){
                    window.location.href="index/";
                }
        }
    });

    xhr.open("POST", "/ajax_login/");
    // xhr.setRequestHeader("Content-Type", "application/json");

    xhr.send(data);
}
