function checkIfPassOk() {
    let value = this.document.getElementById("password").value;
    let res = value && value.length>=8  && value.length<=20;
    if (!res) {
        alert("The input is need to be match! length need to be between  8-20");
    }
    return res;
}

function  checkAll() {
    let res = true;
    res = res && checkIfPassOk() ;
//    res = res && ..
    if (res){
       alert("The form has been sent !");
    }

}

