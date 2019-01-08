## Python-KCP
+ Python binding for KCP, 
+ what is KCP? please visit: https://github.com/skywind3000/kcp, 
+ http://www.skywind.me/blog/archives/1048 

## Wiki
+ 感谢xingshuo的python-kcp，https://github.com/xingshuo/python-kcp ，本库在该库的基础上添加ikcp_peeksize和ikcp_setmtu、ikcp_waitsnd三个函数，并增加Python3版本的支持
+ 基于Cython实现KCP源码的Python2和Python3的封装

## 前置库
+ 1.Python2.x / Python3.x
+ 2.python-pip         #sudo apt-get install python-pip python-dev build-essential python3-dev
+ 3.Cython             #sudo pip install Cython
+ 4.python-setuptools  #sudo apt-get install python-setuptools

## 支持平台
+ Linux(Ubuntu)

## 安装库
+ sh setup.sh

## 运行测试程序
+ python test/testkcp.py