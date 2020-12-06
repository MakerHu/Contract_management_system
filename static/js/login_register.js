function CheckLoginUsernameInput() {
    document.getElementById("hide1").style.display = "none";
    document.getElementById("hide2").style.display = "none";
}

function CheckLoginPasswordInput() {
    document.getElementById("hide2").style.display = "none";
}

function onlogin() {
    var username = document.getElementById("login-username").value;
    var password = document.getElementById("login-password").value;

    console.log(username);
    console.log(password);

    if (username == '' || password == '') {
        // alert("用户名或密码不能为空！");
    } else {
        var data = new FormData();
        data.append("username", username);
        data.append("password", password);
        console.log(data);

        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

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
                if (json.exists_username == 'success' && json.right_password == 'success') {
                    window.location.href = "/index/";
                }
            }
        });
        xhr.open("POST", "/ajax_login/");
        xhr.send(data);
    }
}

function CheckRegisterUsernameInput() {
    document.getElementById("hide3").style.display = "none";
}

function CheckUsernameAjax() {
    var username = document.getElementById("register-username").value;

    var data = new FormData();
    data.append("username", username);
    console.log(data);

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            var json = JSON.parse(this.responseText);
            console.log(this.responseText);
            if (json.same_username == 'success') {
                document.getElementById("hide3").style.display = "block";
            } else {
                document.getElementById("hide3").style.display = "none";
            }
        }
    });
    xhr.open("POST", "/ajax_confirm_username/");
    xhr.send(data);
}

function CheckSame() {
    var password1 = document.getElementById("register-password").value;
    var password2 = document.getElementById("confirm_password").value;
    if (password1 == password2) {
        document.getElementById("hide5").style.display = "none";
        // document.getElementById("onsubmit").style.disabled=false;
    } else {
        document.getElementById("hide5").style.display = "block";
        // document.getElementById("onsubmit").style.disabled=true;
    }
    if (password2 == '') {
        document.getElementById("hide5").style.display = "none";
    }
}

function onregister() {
    var username = document.getElementById("register-username").value;
    var password = document.getElementById("register-password").value;
    var confirm_password = document.getElementById("confirm_password").value;

    if (username == '' || password == '' || confirm_password == '') {
        // alert("用户名或密码不能为空！");
    } else {
        if (password == confirm_password) {
            var data = new FormData();
            data.append("username", username);
            data.append("password", password);
            data.append("confirm_password", confirm_password);
            console.log(data);

            var xhr = new XMLHttpRequest();
            xhr.withCredentials = true;

            xhr.addEventListener("readystatechange", function () {
                if (this.readyState === 4) {
                    var json = JSON.parse(this.responseText);
                    console.log(this.responseText);
                    if (json.role_execption == 'true') {
                        alert("系统异常，注册失败，请重新操作！");
                    } else {
                        if (json.same_username == 'success') {
                            document.getElementById("hide3").style.display = "block";
                        } else {
                            document.getElementById("hide3").style.display = "none";
                            alert("注册成功！");
                            window.location.href = "/login/";
                        }
                    }
                }
            });
            xhr.open("POST", "/ajax_register/");
            xhr.send(data);
        } else {
            document.getElementById("hide5").style.display = "block";
        }
    }
}

function OnLogout() {
    window.location.href = "/logout/";
}

