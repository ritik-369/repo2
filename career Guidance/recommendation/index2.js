function print(a)
{
    console.log(a);
}
function others_data()
{
    var other_data=document.getElementsByClassName("other_data");
    var ids=document.getElementsByClassName("id");
    var values=document.getElementsByClassName("value");
    var length =other_data.length;
    for(i=0;i<length;i++)
    {
        other_data[i].setAttribute("id",ids[i].value);
        other_data[i].setAttribute("value",values[i].value);
        console.log(other_data[i].id,"===",other_data[i].value);
        
    }
    print(other_data);
    // return other_data;
}

var otrst=document.getElementById("first_otr");
var otrs=otrst;
console.log(otrs);
otrst.remove();
function add()
{
    // document.body.style.backgroundColor="pink";
    otrs.style.opacity=1;
    document.getElementById("container").innerHTML=document.getElementById("container").innerHTML+otrs.innerHTML;
}
var g_fields,g_values;
function make(fields,values)
{
    // value=value.toLowerCase()
    var length=fields.length;
    for(i=0;i<length;i++)
    {
        if(fields[i]=="")
        {
            fields.splice(i,1);
            values.splice(i,1);
        }
    }
    length=fields.length;
    for(i=0;i<length;i++)
    {
        if((fields[i]=="none")||(fields[i]=="None"))
        {
            fields.splice(i,1);
            values.splice(i,1);
        }
    }
    length=fields.length;
    for(i=0;i<length;i++)
    {
        if(values[i]=="")
        {
            fields.splice(i,1);
            values.splice(i,1);
        }
    }
    length=fields.length;
    for(i=0;i<length;i++)
    {
        if((values[i]=="none")||(values[i]=="None"))
        {
            fields.splice(i,1);
            values.splice(i,1);
        }
    }
    print("a");
    print(fields);
    print("b");
    print(values);
    g_fields=fields;
    g_values=values;
}
// function make(arr,value)
// {
//     var tarr=arr;
//     var length=arr.length;
//     for(i=0;i<length;i++)
//     {
//         if(arr[i]==value)
//         {
//             tarr.splice(i,1);
//         }
//     }
//     return tarr;
// }
// function submit()
// {

//     localStorage.clear();
//     fields=document.getElementsByClassName("specific");
//     values=document.getElementsByClassName("specific");
//     var length=values.length;
//     var fields=[1],values=[1];
//     for(i=0;i<length;i++)
//     {
//         field=document.getElementsByClassName("specific")[i].id;
//         value=document.getElementsByClassName("specific")[i].value;
//         fields.push(field);
//         values.push(value);
//     }
//     fields.shift();
//     values.shift();
//     // print(values);
//     values=JSON.stringify(values);
//     fields=JSON.stringify(fields);
//     localStorage.removeItem("fields");
//     localStorage.removeItem("values");
//     localStorage.setItem("fields",fields);
//     localStorage.setItem("values",values);
//     // window.location.replace("./rating.html");
// }
function submit()
{

    localStorage.clear();
    others_data();
    var data=document.getElementsByClassName("specific");
    // console.log(data[0].id,"====",data[0].value);
    var fields=[1],values=[1],length=data.length;
    for(i=0;i<length;i++)
    {
        field=data[i].id;
        value=data[i].value;
        fields.push(field);
        values.push(value);
    }
    fields.shift();
    values.shift();
    // print(fields);
    make(fields,values);
    make(fields,values);
    fields=g_fields;
    values=g_values;
    // values=make(fields,values,null);
    // fields=make(values,fields,"");
    // values=make(values,fields,null);
    // print(values);
    values=JSON.stringify(values);
    fields=JSON.stringify(fields);
    localStorage.removeItem("fields");
    localStorage.removeItem("values");
    localStorage.setItem("fields",fields);
    localStorage.setItem("values",values);
    document.body.style.backgroundColor="pink";
    window.location.replace("./rating2.html");
}

// var a=["none",2,3,4,"none"],b=[1,2,3,4,5];
// make(a,b,"");
// print(a);
// print(b);