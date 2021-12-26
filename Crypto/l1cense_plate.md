* cipher.txt 파일을 열어볼게요.

![alt Li1](https://github.com/simnple/Christmas_ctf/blob/main/Crypto/imgs/Li1.png)<br>
```Xsirhgnzh{o1XvmHV_k1ZGv_ZAN9590}```
* 먼가 형식은.. 앞쪽은 무조건 Christmas{ 일꺼같은데..

![alt Li2](https://github.com/simnple/Christmas_ctf/blob/main/Crypto/imgs/Li2.png)
* URL: https://www.dcode.fr/cipher-identifier
* 위 사이트를 활용하여 분석해보면.
* Atbash Cipher 라는 암호화 방식이 가장 유력하다고 나오네요.

![alt Li3](https://github.com/simnple/Christmas_ctf/blob/main/Crypto/imgs/Li3.png)
* URL: https://www.dcode.fr/atbash-cipher
* 그래서 대입을 해보니 플래그가 나왔어요!
```
Flag: Christmas{l1CenSE_p1ATe_AZM9590}
```