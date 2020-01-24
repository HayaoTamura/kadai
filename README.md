# kadai

 n = message.gata*3 : 3倍に設定
 
サブスクライバの作成
sub = rospy.Subscriber('count_up', Int32, cb)　: rospy.Subscriberを作る。型はInt32である。cb : コールバック関数
　
パブリッシャの作成
rospy.init_node('count')　: ノード名がcount
pub = rospy.Publisher('count_up', Int32, queue_size=1)　: パブリッシャがcount_up

rospy.Rate(10)　: 秒ごとの送信回数


