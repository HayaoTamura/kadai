# 課題2

countした数値をpub.publishu()の括弧内の式に代入し、表示させるプログラム。

n = message.gata % 20  : 20で割った余りに設定

p = message.data % 15　: 15で割った余りに設定
 
Publisher :トピックにデータを送信する

Subscriber　:送信されたデータを受信する 

sub = rospy.Subscriber('count_up', Int32, cb)　: rospy.Subscriberを作る。

型はInt32である。cb : コールバック関数

pub = rospy.Publisher('count_up', Int32, queue_size=1)　: Publisherがcount_up

rospy.Rate(1)　: 秒ごとの送信回数

pub.publish((n+p)**2)　: カッコ内の式に代入し、表示する





