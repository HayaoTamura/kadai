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

ノードを立ち上げてrostopic echo /threeでトピックとしてデータを得る


