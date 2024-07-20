document.getElementById("subscribe").addEventListener("submit",function(event){
    event.preventDefault();
    var email = document.getElementById("email").value;
    var user_name = document.getElementById("name").value;
    var lc_user = document.getElementById("username").value;
    console.log(email)
    console.log(user_name)
    console.log(lc_user)

    const data = {email,user_name,lc_user}
    fetch("/submit",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
            },
        body:JSON.stringify(data)
    })
    .then(res=>res.json())
    .then(data=>{
        console.log(data)
        alert("YOU HAVE BEEN SUBSCRIBED! WAIT FOR US IS IN YOUR INBOX!")
    })
    
    .catch((error)=>{
        console.log(error)
    })











})