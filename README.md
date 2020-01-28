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


1個目

roscore


2個目

cd

mkdir -p catkin_ws/src

cd ~/catkin_ws/src

catkin_init_workspace 

cd ~/catkin_ws

catkin_make

source ~/.bashrc



cd ~/catkin_ws/src

catkin_create_pkg mypkg rospy

cd mypkg/

mkdir scripts

cd scripts/

git clone https://github.com/HayaoTamura/kadai.git

cd kadai

chmod u+x count.py

rosrun mypkg count.py


3個目

cd ~/catkin_ws/src/mypkg/scripts/kadai

chmod u+x twice.py

rosrun mypkg twice.py


4個目

cd ~/catkin_ws/src/mypkg/scripts/kadai

rostopic echo /twice

撮影


pを加えてなんか２つにする
何秒かに1回とか、毎回とか、文字を出すようにする
