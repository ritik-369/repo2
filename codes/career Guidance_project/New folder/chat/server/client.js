const socket =io("http://localhost:8000");

const form = document.getElementById("send-container");
const messageInput=document.getElementById("messageInp")
const messageContainer=document.querySelector(".container")

const append=(message,position)=>{
    const messageElement=document.createElement('div')
    message.classlist.add("message")
    message.classlist.add("position");
    messageContainer.append(messageElement);
}


const namee=prompt("Enter Your Name");
socket.emit("new user join",namee);


socket.on("user joined",namee=>{
append(`${namee} joined the chat`,`right`)
})