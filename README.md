# tornado_server in python

## 1. 背景
* Tornado是一个用Python编写的异步HTTP服务器，同时也是一个web开发框架
* Tornado优秀的大并发处理能力得益于它的web server，从底层开始就自己实现了一整套基于epoll的单线程异步架构
* [tornado文档](./doc/tornado.md)
* [tornado高并发demo](./doc/code)

## 2. 特点
* 支持restful api风格
* 高并发异步框架


## 3. 安装
* 安装python3.7
* pip3 install -r requirements.txt


## 4. 运行
### windows
* 双击run_mine.exe

### linux
* ./run_mine


## 5. 用例测试
* 测试用例在script/tests下，如有增加，修改start.py里面的do_unittest函数即可
* 双击run_unittest.exe，进行自动化测试


## 6. 其他
* 如有疑问，可以邮箱联系yzs1127@163.com