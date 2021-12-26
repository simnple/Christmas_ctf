* SECRET 이 무슨 파일인지 알기 위해, hxd로 열어보겠습니다.

![alt De1](https://github.com/simnple/Christmas_ctf/blob/main/MISC/imgs/De1.png)
* 이미지 파일이였네요.
* SECRET.png로 이름을 바꾼후 열어보겠습니다.

![alt De2](https://github.com/simnple/Christmas_ctf/blob/main/MISC/imgs/De2.png)
* 근데 나오는건 회색사진 하나..
* 한번 이미지 포렌식을 하러 가보겠습니다.
* URL: https://29a.ch/photo-forensics/#forensic-magnifier

![alt De3](https://github.com/simnple/Christmas_ctf/blob/main/MISC/imgs/De3.png)
* 파일 업로드 후, Principal Component Analysis 탭에 들어가보니
* QR코드가 나오네요

![alt De4](https://github.com/simnple/Christmas_ctf/blob/main/MISC/imgs/De4.png)
* URL: https://webqr.com/
```
Flag: Christmas{iT's_t1m3_t0_g1v3_0ut_Pr3s3nts}
```