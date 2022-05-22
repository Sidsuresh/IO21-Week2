function sendEmail(){
    var name = document.getElementById('from_name').value;
    var reply = document.getElementById('reply_to').value;
    var msg = document.getElementById('message').value;

    var tempPar = {
        from_name: name,
        message: msg,
        reply_to: reply,
    }

    alert("Sending");
    emailjs.send("service_z95sgnd","template_cktswrk", tempPar,"7XPp5Q1Kij49W77Ox").then(function(res){
        console.log(res.status);
    });

    alert("Success");
}