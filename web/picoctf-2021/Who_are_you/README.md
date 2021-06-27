## Solution:
Needed the following headers to get the flag:

```
User-Agent: PicoBrowser
Accept-Language: sv
Referer: http://mercury.picoctf.net:38322
Date: 2018
DNT: 1
X-Forwarded-For: 2.16.155.10
```

```X-Forwarded-For``` was used to spoof the IP address range of the country i.e. Sweden here, and value in ```Accept-Language``` was used as a language preference i.e. swedish here.
                                                                                                                                                                                                                           
 
