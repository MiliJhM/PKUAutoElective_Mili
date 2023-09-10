#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: recognizerAPI.py
# modified: 2023-09-07

import os
import time
import base64
import requests
import json
import cv2

class Captcha(object):

    __slots__ = ['_code','_im_data','_im_segs']

    def __init__(self, code, im_data):
        self._code = code
        self._im_data = im_data

    @property
    def code(self):
        return self._code

    def __repr__(self):
        return '%s(%r)' % (
            self.__class__.__name__,
            self._code,
        )

    def save(self, folder):
        code = self._code
        data = self._im_data
        timestamp = int(time.time() * 1000)

        filepath = os.path.join(folder, "%s_%d.gif" % (code, timestamp))
        with open(filepath, 'wb') as fp:
            fp.write(data)



class CaptchaRecognizerAPI(object):

    def __init__(self, token):
        self.__custom_url = "http://api.jfbym.com/api/YmServer/customApi"
        self.__token = token
        self.__headers = {
        'Content-Type': 'application/json'
        }

    def common_verify(self, im_data, verify_type="10103"):
        payload = {
            "image": base64.b64encode(im_data).decode(),
            "token": self.__token,
            "type": verify_type
        }
        print(payload)
        resp = requests.post(self.__custom_url, headers=self.__headers, data=json.dumps(payload))
        print(resp.text)
        return resp.json()['data']['data']

    def recognize(self, im_data):
        code = self.common_verify(im_data) # 1-6位字母混合数字,可动态gif
        return Captcha(code, im_data)


if __name__ == '__main__':
    recognizer = CaptchaRecognizerAPI("")
    im_data = open("DrawServlet.jpg", "rb").read()
    print(recognizer.common_verify(im_data))