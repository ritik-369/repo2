function submit()
{
    var div=document.createElement("div");
    div.innerText=document.getElementById("message").value;
    div.classList.add("right","message");
    document.getElementById("container").appendChild(div);
}

function wait(id)
{
    
}