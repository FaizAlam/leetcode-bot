document.getElementById("subscribe").addEventListener("submit",function(event){
    event.preventDefault();
    var email = document.getElementById("email").value;
    var user_name = document.getElementById("name").value;
    var lc_user = document.getElementById("username").value;

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
        if (data?.status===400){
            alert("YOU HAVE ALREADY SUBSCRIBED!")
        }
        else if(data?.status===200){
        alert("YOU HAVE BEEN SUBSCRIBED! WAIT FOR US IS IN YOUR INBOX!")
        }
    })
    
    .catch((error)=>{
        alert("SOMETHING WENT WRONG! TRY AGAIN LATER")
    })











})