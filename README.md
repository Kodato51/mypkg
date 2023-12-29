# mypkg
[![test](https://github.com/Kodato51/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Kodato51/mypkg/actions/workflows/test.yml)

このパッケージは千葉工業大学先進工学部未来ロボティクス学科のロボットシステム学の講義で作成、使用したものです。

# 使用方法
## talker.py
* /countupを通じて数字をカウントする。

* 実行方法
  - 以下のコマンドを端末１で実行
```
$ ros2 run mypkg talker
```
* 実行結果
```
(何も表示されない)
```
## listener.py
* /countup からメッセージをもらい表示する。

* 実行方法
  - 別の端末２で以下のコマンドを実行
```
$ ros2 run mypkg listener
```
* 実行結果
```
[INFO] [1703853650.521510168] [listener]: Listen: 11
[INFO] [1703853650.999005294] [listener]: Listen: 12
[INFO] [1703853651.497019100] [listener]: Listen: 13
[INFO] [1703853651.997191090] [listener]: Listen: 14
[INFO] [1703853652.497162622] [listener]: Listen: 15
[INFO] [1703853652.997085636] [listener]: Listen: 16
[INFO] [1703853653.497429703] [listener]: Listen: 17
[INFO] [1703853653.996932644] [listener]: Listen: 18
[INFO] [1703853654.497097220] [listener]: Listen: 19
[INFO] [1703853654.998425150] [listener]: Listen: 20
[INFO] [1703853655.497294684] [listener]: Listen: 21
[INFO] [1703853655.997441311] [listener]: Listen: 22
[INFO] [1703853656.497618644] [listener]: Listen: 23
[INFO] [1703853656.997646743] [listener]: Listen: 24
[INFO] [1703853657.497197859] [listener]: Listen: 25
[INFO] [1703853657.997170716] [listener]: Listen: 26
[INFO] [1703853658.497302285] [listener]: Listen: 27
[INFO] [1703853658.997277639] [listener]: Listen: 28
[INFO] [1703853659.497819370] [listener]: Listen: 29
[INFO] [1703853659.997084641] [listener]: Listen: 30
[INFO] [1703853660.497213248] [listener]: Listen: 31
```

## talk_listn.launch.py
* talker.pyとlistener.pyを１つの端末で立ち上げるノード。
* 実行方法
```
$ ros2 launch mypkg talk_listen.launch.py
```
* 実行結果
```
結果
```

## 必要なソフトウェア
* ROS2
* Python

## テスト環境
* ubuntu 22.04 on Windows

## ライセンス
*  このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されています

* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022/)

* © 2023 Ryuki Kodato
