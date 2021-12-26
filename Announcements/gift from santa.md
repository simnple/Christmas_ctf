![alt Gift1](/imgs/Gift1.png)
101.zip 안에는 수많은 폴더들이 있습니다.
그 안에는 폴더 혹은 flag.txt 라는 폴더가 있더라구요.
그래서 flag.txt 라는 파일을 열어보았는데,

![alt Gift2](/imgs/Gift2.png)
거기 안에 내용은 "Christmas{fake_flag}" 로 도배가 된걸로 보였습니다.
여기서 하나 확신이 든것은 이 수 많은 flag.txt중 하나는 진짜 플래그가 포함이 되었을꺼라 생각을 했어요.

근데 이 수많은 폴더, 파일중에 하나를 찾을려는건 불가능에 가까워서, 파이썬 코드를 작성하게 되었어요.

[ gift from santa.py ]

하지만 이 파이썬 코드를 실행시킬려면 조건이 필요해요.
1. 모든 폴더 안에 flag.txt가 있어야 한다.
2. 폴더 이름이 숫자여야 한다.

위에 코드를 실행시키려고 폴더 안에 폴더들을 빼내면서 수많은 작업을 거쳤습니다..

이동시킨 후, 파이썬 파일을 동작시키면

![alt Gift3](/imgs/Gift3.png)
이렇게 101번 폴더에 플래그가 있다 뜨네요.
101/flag.txt 파일을 보면

```
Flag: Christmas{Congratulations_You_got_a_flag_}
```