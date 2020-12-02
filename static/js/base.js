function list() {
    var body = document.getElementsByTagName("body")[0]
    var aside = document.getElementsByTagName("aside")[0]
    if (aside.clientWidth <= 40) {
        body.className = ""
    } else if (aside.clientWidth > 40) {
        console.log("side")
        body.className = "minibody"
    }
}

function ondraft_contract() {

    window.location.href = "/draftcontract/";
}

function onhome() {

    window.location.href = "/index/";
}