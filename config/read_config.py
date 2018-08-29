#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-08-06 17:25:43
# @Last Modified time: 2018-08-16 15:05:00
# @E-mail: 1370465454@qq.com
# @Description: 读取ini配置文件

import configparser
import codecs


class Read_Config:
    """专门读取配置文件的,.ini文件格式"""

    def __init__(self, filename):
        configpath = filename
        fd = open(configpath, 'r', encoding='gbk')
        data = fd.read()
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            files = codecs.open(configpath, "w")
            files.write(data)
            files.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def get_Value(self, env, name):
        """
        [projectConfig]
        project_path=D:\Pyproject\Test_Login
        :param env:[projectConfig]
        "param name:project_path"
        :return:D:\Pyproject\Test_Login
        """
        return self.cf.get(env, name)
