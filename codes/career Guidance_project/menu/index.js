function go(loctaion){
    if(location=="councellors")
    {
        location="councellors";
    }
    else if(location="recommendation")
    {
        location="recommendation";
    }
    else
    {
        location="store";
    }
    loc="..\\"+loctaion+'/index.html'
    window.location.href =loc;
}
function orange()
{
    var quote=document.getElementById("quote");
    quote.style.color="orange";
}
function yellow()
{
    var quote=document.getElementById("quote");
    quote.style.color="yellow";
}
function blue()
{
    var quote=document.getElementById("quote");
    quote.style.color="blue";
}
function start()
{
    var quote=document.getElementById("quote");
    quote.style.color="orange";
    setInterval(orange,1000);
    setInterval(blue,3000);
    setInterval(yellow,5000);
    var text=document.getElementById("quote");
}