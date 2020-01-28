# 課題2

countした数値をpub.publishu()の括弧内の式に代入し、表示させるプログラム。

n = message.gata % 20  : 20で割った余りに設定
 
Publisher :トピックにデータを送信する

Subscriber　:送信されたデータを受信する 

・サブスクライバ

sub = rospy.Subscriber('count_up', Int32, cb)　: rospy.Subscriberを作る。

型はInt32である。cb : コールバック関数
　
・パブリッシャ

rospy.init_node('count')　: ノード名がcount

pub = rospy.Publisher('count_up', Int32, queue_size=1)　: パブリッシャがcount_up

rospy.Rate(1)　: 秒ごとの送信回数

pub.publish((n+p)**2)　: カッコ内の式に代入し、表示する

・手順

1

roscore


2

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


3

cd ~/catkin_ws/src/mypkg/scripts/kadai

chmod u+x three.py

rosrun mypkg three.py

4

cd ~/catkin_ws/src/mypkg/scripts/kadai

rostopic echo /twice



