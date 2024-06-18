// var k=localStorage.getItem("max");

var scopes={
    "doctor":"very good option",
    "engineer":"super good option",
    "field1":"test field"
}

var field=localStorage.getItem("field")
var rating=localStorage.getItem("rating");
var index=localStorage.getItem("index");
field=JSON.parse(field);
rating=JSON.parse(rating);

var fieldval;
var fieldval=field[index];
console.log(field[index])
console.log(scopes[fieldval])
document.getElementById("container").innerText=scopes[fieldval];
