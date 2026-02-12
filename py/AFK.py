"""
挂机脚本,发送挂机时间到vrchat聊天框中
前置库:pip install python-osc
运行环境:Windows 11 Python 3.12
2026-02-12 written by 小龙小龙
"""
from pythonosc.udp_client import SimpleUDPClient as Client
import time
import os
import datetime

client = Client('127.0.0.1',9000) #vrchat默认端口
def send(message):
    client.send_message("/chatbox/input", [message,True])

StartTime:str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #开始时间
AFKTime:int = 0 #挂机时间

if __name__ == "__main__":
    while True:
        AFKTime += 3
        hour,minute,second = AFKTime // 3600,(AFKTime % 3600) // 60,AFKTime % 60
        message = f"正在挂机...\n挂机起始时间: {StartTime}\n挂机时间: {hour:02d}小时{minute:02d}分钟{second:02d}秒"
        print(message)#在控制台打印消息
        send(message)#发送消息到osc服务器
        time.sleep(3)#等待3秒
        os.system("cls")#清屏
        


    
