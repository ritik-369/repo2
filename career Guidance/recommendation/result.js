// var k=localStorage.getItem("max");

var scopes={
    "cse":"cse is super very good option",
    "neuro":"neuro is also a good option",
    "physician":"physician is also a good option"
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
document.getElementById("field1").innerText=scopes[fieldval];
document.getElementById("field2").innerText=scopes[fieldval2];
// localStorage.clear();
