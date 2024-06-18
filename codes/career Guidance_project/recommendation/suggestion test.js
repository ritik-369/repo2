// var k=localStorage.getItem("max");

var scopes={
    "cse":"cse is  very good option for you",
    "neuro":"neuro is  good option for you",
    "physician":"physician is also a good option for you"
}
function orange()
{
    var quote=document.getElementById("quote");
    quote.style.color="orange";
    quote.innerText="Success is not final; failure is not fatal: It is the courage to continue that counts.-- Winston S. Churchill";
}
function yellow()
{
    var quote=document.getElementById("quote");
    quote.style.color="yellow";
    quote.innerText="It is better to fail in originality than to succeed in imitation -- Herman Melville";
}
function blue()
{
    var quote=document.getElementById("quote");
    quote.style.color="pink";
    quote.innerText="The road to success and the road to failure are almost exactly the same. -- Colin R. Davis";
}
function start()
{
    var quote=document.getElementById("quote");
    quote.style.color="orange";
    setInterval(blue,10000);
    setInterval(orange,5000);
    setInterval(yellow,15000);
    var text=document.getElementById("quote");
}
var data=localStorage.getItem("max")
var data2=localStorage.getItem("max2")
data=JSON.parse(data);
data2=JSON.parse(data2);
// console.log(data);
var fieldval=data[0];
var fieldval2=data2[0];
// console.log(fieldval)
// console.log(scopes[fieldval])
var elem=document.createElement("b");
elem.innerText=fieldval
document.getElementById("page-1").innerText+="1. "+fieldval+" is very good option for you \n \n \n2."+fieldval2+" is also a good option for you as second option";
// document.getElementById("page-1").innerText+="1. "+fieldval+" is very good option for you \n \n \n2."+fieldval2+" is also a good option for you as second option";
// document.getElementById("page-1").innerText=scopes[fieldval];
document.getElementById("page-3").innerText=scopes[fieldval2];
// localStorage.clear();
