# 阿里云短信sdk在python3中的实现

用阿里云的官方sdk

```
sudo pip3 install aliyun-python-sdk-core-v3
```
适配了py3短信功能。
##使用方法。

```python
import uuid
from alisms_py3.runner import SetUp
st = SetUp('xxxx','xxxxxxx')
__business_id = uuid.uuid1()
print (__business_id)
params = "{\"code\":\"12345\",\"product\":\"云通信\"}"
print (st.send_sms(__business_id, "15500000000", "阿里云短信测试专用", "SMS_95611111", params))
```
