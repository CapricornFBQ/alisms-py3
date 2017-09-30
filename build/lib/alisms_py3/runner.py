# -*- coding: utf-8 -*-
import http
import json
import sys

from aliyunsdkcore.acs_exception import error_code, error_msg
from aliyunsdkcore.acs_exception.exceptions import ClientException
from .request.v20170525 import SendSmsRequest
from alisms_py3.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid

"""
短信业务调用接口示例，版本号：v20170525

Created on 2017-09-30

"""

# reload(sys)
# sys.setdefaultencoding('utf8')

class SetUp():
    def __init__(self, ACCESS_KEY_ID, ACCESS_KEY_SECRET, ):
        REGION = "cn-hangzhou"
        # ACCESS_KEY_ID/ACCESS_KEY_SECRET 根据实际申请的账号信息进行替换
        ACCESS_KEY_ID = ACCESS_KEY_ID
        ACCESS_KEY_SECRET = ACCESS_KEY_SECRET
        self.acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)

    def send_sms(self, business_id, phone_numbers, sign_name, template_code, template_param=None):
        smsRequest = SendSmsRequest.SendSmsRequest()
        # 申请的短信模板编码,必填
        smsRequest.set_TemplateCode(template_code)

        # 短信模板变量参数
        if template_param is not None:
            smsRequest.set_TemplateParam(template_param)

        # 设置业务请求流水号，必填。
        smsRequest.set_OutId(business_id)

        # 短信签名
        smsRequest.set_SignName(sign_name);

        # 短信发送的号码列表，必填。
        smsRequest.set_PhoneNumbers(phone_numbers)

        # 调用短信发送接口，返回json
        smsRequest.set_accept_format('JSON')
        http_response = self.acs_client._make_http_response('dysmsapi.aliyuncs.com', smsRequest)
        try:
            status, headers, body = http_response.get_response_object()
        except IOError as e:
            raise ClientException(
                error_code.SDK_SERVER_UNREACHABLE,
                error_msg.get_msg('SDK_SERVER_UNREACHABLE') + ': ' + str(e))
        except AttributeError:
            raise ClientException(
                error_code.SDK_INVALID_REQUEST,
                error_msg.get_msg('SDK_INVALID_REQUEST'))

        return body
        # print(a.get_url())
        # print(a.get_response_object())

        # smsResponse = acs_client.do_action_with_exception(smsRequest)


        # return smsResponse

# __name__ = 'send'
if __name__ == '__main__':
    st = SetUp('xxxx','xxxxxxx')
    __business_id = uuid.uuid1()
    print (__business_id)
    params = "{\"code\":\"12345\",\"product\":\"云通信\"}"
    print (st.send_sms(__business_id, "15500000000", "阿里云短信测试专用", "SMS_95611111", params))
