# tornado_server in python

## 1. 背景

- Tornado 是一个用 Python 编写的异步 HTTP 服务器，同时也是一个 web 开发框架
- Tornado 优秀的大并发处理能力得益于它的 web server，从底层开始就自己实现了一整套基于 epoll 的单线程异步架构
- [tornado 文档](./doc/tornado.md)
- [tornado 高并发 demo](./doc/code)

## 2. 特点

- 支持 restful api 风格
- 高并发异步框架

## 3. 安装

- 安装 python3.7.5
- pip3 install -r requirements.txt

## 4. 运行

- cd script
- python main.py main

## 5. 用例测试

- cd script
- python main.py test

## 6. 其他

- 如有疑问，提交 issues，定期回复
