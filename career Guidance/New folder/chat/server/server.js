// const io=require("socket.io")(8000)
const io = require('socket.io')(8000, {cors:{origin:'*',}});
const user={}

io.on("connection",socket=>{
    socket.on("user-joined",namee=>{
        consoke.log("new user joined",namee)
        user[socket.id]=namee;
        socket.broadcast.emit("user joined")
    });
    socket.on("send",message=>{
        socket.broadcast.emit("receive",{message:message,name:user[socket.id]})
    });
})