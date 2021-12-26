* corruption.png 파일을 열어볼게요.
  
![alt Co1](https://github.com/simnple/Christmas_ctf/blob/main/FORENSIC/imgs/Co1.png)
* 어라? 분명 png 파일인데 이미지로 안열리네요
* 그래서 hxd로 파일을 불러와봤어요.

![alt Co2](https://github.com/simnple/Christmas_ctf/blob/main/FORENSIC/imgs/Co2.png)
* png 파일은 맞는것같아요.
* 두번째줄에 세로 가로 크기들이 쓰여있으니,
* 근데 파일 시그니처인 ``` 89 50 4E 47 0D 0A 1A 0A ``` 이 안보이네요.

![alt Co3](https://github.com/simnple/Christmas_ctf/blob/main/FORENSIC/imgs/Co3.PNG)
* 이렇게 바꿔주고 사진을 다시 열었더니

![alt Co4](https://github.com/simnple/Christmas_ctf/blob/main/FORENSIC/imgs/Co4.PNG)
* 그림판으로 그린듯한 플래그가 나오네요!!
```
Flag: Christmas{itisflag}
```