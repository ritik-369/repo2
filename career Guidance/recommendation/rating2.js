function add(num)
{
    num--;
    var initial=document.getElementById("container").innerHTML;
    for(i=0;i<num;i++)
    {
        document.getElementById("container").innerHTML+=initial;
    }
}
function no_of_options()
{
    return((document.getElementsByClassName("value_int").length)/(document.getElementsByClassName("Intrest").length));
}
function fill(value_set)
{
    var fields=document.getElementsByClassName("name");
    // console.log(fields);
    var length=fields.length;
    for(i=0;i<length;i++)
    {
        // console.log(value_set[i]);
        fields[i].innerText=value_set[i];
    }
    
}
function print(a)
{
    console.log(a);
}
function values()
{
    var obj={};
    var options_html=document.getElementsByClassName("value_int");
    var length=options_html.length;
    for(i=0;i<length;i++)
    {
        obj[options_html[i].value]=length-i;
    }
return obj;
}

function formula(matrix)
{
    var integer;
    var mul=1;
    var row=matrix.length;
    var columns=matrix[0].length;
    for(i=0;i<row;i++)
    {
        mul=1;
        for(j=1;j<=columns-2;j++)
        {
            // console.log(i," ",j," ",matrix[i][j]);
            integer=parseInt(matrix[i][j]);
            // integer=parseInt(matrix[i][j]);
            // mul*=integer;
            mul+=integer;
            // console.log("a",matrix[i][j]);
        }
        matrix[i][columns-1]=mul;
        // console.log(i," ",j," ",matrix[i][columns+1]);
    }
    return matrix;
}



function matrix()
{
    var fields=localStorage.values;
    fields=JSON.parse(fields);
    var row=(fields.length);
    var coloumn=(document.getElementsByClassName("count").length/document.getElementsByClassName("Intrest").length);
    var arr=new Array(row);
    for(i=0;i<row;i++)
    {
        arr[i]=new Array(coloumn+2);
    }

    for(i=0;i<row;i++)
    {
        arr[i][0]=fields[i];
    }

    var t=document.getElementsByClassName("select");
    var parameters=[1];
    for(i=0;i<row;i++)
    {
        parameters.push(t[i].name);
    }
    parameters.shift();
    // console.log(parameters);
    var obj_val=values();
    // console.log(obj_val);
    // var vals=document.getElementsByClassName(parameters[0]);
    // console.log(vals[0].value);
    for(i=0;i<parameters.length;i++)
    {
        var vals=document.getElementsByClassName(parameters[i]);
        // console.log(obj_val[vals[i].value]);
        // console.log(vals[i].value);
        for(j=0;j<row;j++)
        {
            // console.log(j," ",i," ",vals[j].value);
            var integer=parseInt(obj_val[vals[j].value]);
            arr[j][i+1]=integer;
            // console.log(j," ",i," ",arr[j][i]);
        }
    }
    return (arr);
    // return formula(arr);
}
var max_index;
function maximum(matrix)
{
    var row=matrix.length;
    var column=matrix[0].length;
    var max=parseInt(matrix[0][column-1]),mi=0;
    for(i=0;i<row;i++)
    {
        console.log(matrix[i][column-1]);
        var val=parseInt(matrix[i][column-1]);
        if(max<val)
        {
            max=val;
            mi=i;
        }
    }
    max_index=mi;
    return(matrix[mi]);
}
function maximum2(matrix,field)
{
    var row=matrix.length;
    var column=matrix[0].length;
    var max=parseInt(matrix[0][column-1]),mi=0;
    var i=1;
    while(matrix[0][0]==field)
    {
        if(matrix[i][0]!=field)
        {
            max=matrix[i][column-1];
            mi=i;
            console.log(mi);
            break;
        }
        i++;
        if(i==3)break;
    }
    j=i;
    for(i=j;i<row;i++)
    {
        console.log(matrix[i][column-1]);
        var val=parseInt(matrix[i][column-1]);
        if((max<val)&&matrix[i][0]!=field)
        {
            max=val;
            mi=i;
        }
    }
    return(matrix[mi]);
}
function start1()
{
    var value_set=localStorage.getItem("values");
    value_set=JSON.parse(value_set);
    var length=value_set.length;
    // console.log(length);
    // console.log(no_of_options());
    add(length);
    fill(value_set);
    // here
    // var values_obj=values();
    // var obj=JSON.stringify(values_obj);
    // localStorage.setItem("options_obj",obj);
    // var data=matrix();
    // print(data);
    // data=formula(data);
    // var max=(maximum(data));
    // console.log(max);
    // // // localStorage.clear();
    // localStorage.setItem("max",JSON.stringify(max));
    // //// window.location.replace("./result.html");
    // //// window.location.replace("./result.html");

    
}
function start2()
{
    var value_set=localStorage.getItem("values");
    value_set=JSON.parse(value_set);
    var length=value_set.length;
    // console.log(length);
    // console.log(no_of_options());
    // add(length);
    // fill(value_set);
    // here
    var values_obj=values();
    var obj=JSON.stringify(values_obj);
    localStorage.setItem("options_obj",obj);
    var data=matrix();
    data=formula(data);
    var max=(maximum(data));
    print('a',data);
    data.splice(max_index,1);
    var max2=(maximum(data));
    console.log(data);;
    console.log("a",max);
    console.log("b",max2);
    // // localStorage.clear();
    localStorage.setItem("max",JSON.stringify(max));
    localStorage.setItem("max2",JSON.stringify(max2));
    //// window.location.replace("./result.html");
    //// window.location.replace("./result.html");

    
}

function move(){
    start2();
    window.location.replace("./suggestion.html");
    console.log("click");
}


