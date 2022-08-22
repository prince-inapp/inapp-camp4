var params = {
    "email": "prince.j@inapp.com",
    "password": "wraf",
    "first_name": "fwafwe",
    "last_name": "ffwaew",
    "date_of_joining": "2022-08-02",
    "id": 6
  }


fetch("http://localhost:50/staff",{ 
    method: 'POST',Headers:{
    'ACCEPT': 'application/json,text/plain, */*',
    'Content-Type': 'application/json;charset=UTF-8'
    }
})
    .then(response => response.json())
    .then(data => console.log(data))
    .catch((error) => console.error(error));
    
