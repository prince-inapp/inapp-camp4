

function send_data(){

    params = {
        'email': document.getElementById("email").value,
        password : document.getElementById("password").value,
        'first_name': document.getElementById("firstName").value,
        'last_name': document.getElementById("lastName").value,
        'mobile_no': document.getElementById("mobileNo").value,
        'date_of_joining': document.getElementById("doj").value,

    }

    request = new XMLHttpRequest();
    request.open('POST', 'http://localhost:50/staff')
    request.setRequestHeader('Content-Type', 'application/json;charset=UTF-8')
    request.send(JSON.stringify(params));
    request.onload=()=>{
        console.log(JSON.parse(request.responseText));
    }
    document.getElementById("send_status").innerHTML = "Data sent";
}

function get_data(){
    request = new XMLHttpRequest();
    request.open('GET', 'http://localhost:50/staff')
    request.send();
    request.onload=()=>{
        
        if(request.status === 200){
            console.log(JSON.parse(request.response));
            document.getElementById("r1").innerHTML = request.response;
        }
        else {
            console.log("Error");
        }
    }
}
