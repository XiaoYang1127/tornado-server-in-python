#!/usr/bin/env/python
# _*_coding:utf-8_*_

import time
import os
import sys
import traceback

import httpserver.http_server
import tests.start


script_path = "script"
if script_path not in sys.path:
    sys.path.append(script_path)


def base_init():
    httpserver.http_server.init_http_server()


def main():
    try:
        base_init()
    except Exception:
        traceback.print_exc()

    process()


def process():
    while True:
        time.sleep(0.2)


def test():
    tests.start.do_unittest()


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("pthon main.py main|test")
        exit(0)

    if argv[1] == "main":
        main()
    elif argv[1] == "test":
        test()
    else:
        print("pthon main.py main|test")
