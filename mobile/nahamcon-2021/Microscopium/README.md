## Task:
Determine the correct 4-digit pin (that is treated as salt) to get the flag.

## Bug:
* Key and flag (in encrypted form) is hardcoded in the code written in JS inside assets/index.android.bundle file.
* Algorithm used to generate cipher/plain text can also be read easily inside the same file.

## Solution:
* Run ``` apktool d microscopium.apk ``` to get the decompiled version of apk inside the folder name 'microscopium'.
* Run ``` grep -Ri "Insert the pin to get the flag" microscopium/ ``` to find the file where the relevant code and pin validation is present.
* Found the relevant string, cipher text, and the partial key used for encryption inside microscopium/assets/index.android.bundle file.
* This code is written in JS that can be make readable using [JS beautifier](https://beautifier.io/)
* Relevant code:
```
function b() 
{
                var t;
                (0, o.default)(this, b);
                for (var n = arguments.length, l = new Array(n), u = 0; u < n; u++) l[u] = arguments[u];
                return (t = v.call.apply(v, [this].concat(l))).state = {
                    output: 'Insert the pin to get the flag',
                    text: ''
                }, t.partKey = "pgJ2K9PMJFHqzMnqEgL", t.cipher64 = "AA9VAhkGBwNWDQcCBwMJB1ZWVlZRVAENW1RSAwAEAVsDVlIAV00=", t.onChangeText = function(n) {
                    t.setState({
                        text: n
                    })
                }, t.onPress = function() {
                    var n = p.Base64.toUint8Array(t.cipher64),
                        o = y.sha256.create();
                    o.update(t.partKey), o.update(t.state.text);
                    for (var l = o.hex(), u = "", c = 0; c < n.length; c++) u += String.fromCharCode(n[c] ^ l.charCodeAt(c));
                    t.setState({
                        output: u
                    })
                }, t
}
```
* Only salt is missing from the partial key, and that is what need to be bruteforced.
* Iterate over all values from 0 to 9999 and append it in the partial key as a salt then take sha256 of it to generate the final key.
* Final algo used for decryption ``` flag = cipher XOR sha256(partialKey + bruteforced_salt)  ``` 
* Given cipher text is of 38 bytes long and generated hash is only 32 bytes long.
* As per the code the hashed key is first converted to hex format thus making it 64 character long (still 32 bytes long).
* Each of these 64 characters are then considered as 1 byte before XORing with the cipher text (treated as 64 bytes long).
* Hence, only 19B (38 hex characters) of hashed value are used in this XOR operation.

