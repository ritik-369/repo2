
function result(){
    // body
    var score=0;
    var max;
    if(document.getElementById("rf1")>document.getElementById("rf2"))
    {
        max=document.getElementById("rf1").value;
    }
    else
    {
        max=document.getElementById("rf2").value;
    }

    document.getElementById("greater").style.opacity=1;
    document.getElementById("greater").innerText=max;
}


function addrow(){
    console.log("clicked");
    cont=document.getElementById("container").innerHTML;
    console.log(cont);
    // elem=document.getElementsByClassName("about").innerHTML;
    document.getElementById("container").innerHTML=document.getElementById("container").innerHTML+document.getElementById("first").innerHTML;
}


function get_index(rating)
{
    // var length;
    length=rating.length;
    var v=rating[0].value;
    v=parseInt(v);
    var max=v,maxi=0;
    for(i=0;i<length;i++)
    {
       v=rating[i].value;
       v=parseInt(v);
       if(max<v)
       {
           max=v;
           maxi=i;
       }
       
    }
    return maxi;
}
function press()
{
    
    document.getElementById("submit").click();
    // document.body.style.backgroundColor="pink";
}
var arr=[0];
function values(obj)
{
    var length=obj.length;
    for(i=0;i<length;i++)
    {
        arr.push(obj[i].value)
    }
    arr.shift();
    return arr;
}
var global,global2;
function print(){
    localStorage.clear();
    fields=document.getElementsByClassName("field");
    global=values(fields);
    
    rating=document.getElementsByClassName("value");
    
    var max=get_index(rating);
    localStorage.clear();
    localStorage.setItem("field",(JSON.stringify(global)));
    localStorage.setItem("index",max);
    window.location.replace("./result.html")
}

