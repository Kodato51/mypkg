# mypkg
![test](https://github.com/Kodato51/mypkg/actions/workflows/test.yml/badge.svg)

このパッケージは千葉工業大学先進工学部未来ロボティクス学科のロボットシステム学の講義で作成、使用したものです。

##使用方法
##talker.py
* /countupを通じて数字をカウントする。
'''
$ ros2 run mypkg talker
'''
* 実行結果
'''
(何も表示されない)
'''
##listener.py
* /countup からメッセージをもらい表示する。
* 実行方法
'''
$ ros2 run mypkg listener
'''
* 実行結果
'''
結果
'''

##talk_listn.launch.py
* talker.pyとlistener.pyを１つの端末で立ち上げるノード。
* 実行方法
'''
$ ros2 launch mypkg talk_listen.launch.py
'''
* 実行結果
'''
結果
'''

##必要なソフトウェア
* ROS2
* Python

##テスト環境
* ubuntu 22.04 on Windows

##ライセンス
*  このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されています

* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022/)

* © 2023 Ryuki Kodato
