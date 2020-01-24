# kadai2

 n = message.gata*3 :3倍に設定
 
Publisher :トピックにデータを送信する

Subscriber　:送信されたデータを受信する 

・サブスクライバの作成

sub = rospy.Subscriber('count_up', Int32, cb)　: rospy.Subscriberを作る。

型はInt32である。cb : コールバック関数
　
・パブリッシャの作成

rospy.init_node('count')　: ノード名がcount

pub = rospy.Publisher('count_up', Int32, queue_size=1)　: パブリッシャがcount_up

rospy.Rate(10)　: 秒ごとの送信回数



#kadai2-2

pigpio :Raspberry Piのデジタル入出力のGPIOを使いやすくするためのライブラリ。

pigpioではLow→HighやHigh→Lowなど、GPIOピンの状態が変化したときにコールバック関数を呼ぶことが出来る。

public : クラス外からアクセス可能。クラスを利用するために使用するメソッドを宣言。

private : クラス内でのみアクセス可能 。クラスの中でのみ利用するメソッドを宣言。

NodeHandle :rosparamを扱うことができる

pi = pigpio_start(NULL,NULL); :piの初期化

gpio_write(pi,26,1);　:ピン番号の選択。GPIO26の制御。1ではHighで電圧をかける。

ros::spin()は、イベントが発生するまでずっとループし続ける。
ros::spinOnce()には、ループ機能がない
