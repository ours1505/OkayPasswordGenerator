###这是一个获取Okay学习机开发者密码的脚本
import hashlib
import time
key = input("请输入您设备的序列号：")+ str(time.strftime("%Y",time.localtime()) )+str(int(time.strftime("%m", time.localtime()) ))+str(int(time.strftime("%d", time.localtime()) ))+"010@okay.cn"
m = hashlib.md5()
m.update(key.encode("utf8"))
print("您设备的开发者密码为：",m.hexdigest()[-6:] )
