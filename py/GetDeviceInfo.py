"""
获取设备信息并发送到vrchat聊天框中
前置库:pip install psutil py-cpuinfo GPUtil python-osc
运行环境:Windows 11 Python 3.12
2026-02-12 written by 小龙小龙
"""
from pythonosc.udp_client import SimpleUDPClient as Client
import time
import psutil
import cpuinfo
import GPUtil

client = Client('127.0.0.1',9000) #vrchat默认端口
def send(message):
    client.send_message("/chatbox/input", [message,True])

def get_device_info():
    device_info = {} #存储设备信息的字典

    cpu_name = cpuinfo.get_cpu_info().get("brand_raw","未识别型号") #获取CPU型号
    cpu_usage = psutil.cpu_percent(interval=1) #获取CPU使用率，interval参数表示测量的时间间隔，单位为秒
    device_info["cpu"] = {
        "cpu_name":cpu_name,
        "cpu_usage":cpu_usage
    } #将CPU信息存储到字典中

    gpus = GPUtil.getGPUs() #获取GPU信息
    if gpus:
        gpu = gpus[0] #假设只使用第一块GPU
        gpu_name = gpu.name #获取GPU型号
        gpu_usage = gpu.load * 100 #获取GPU使用率，load属性表示GPU的负载，范围为0到1
        VRAM_total = gpu.memoryTotal / 1024 #获取GPU的总显存，单位为GB
        VRAM_used = gpu.memoryUsed / 1024 #获取GPU的已用显存，单位为GB
        device_info["gpu"] = {
            "gpu_name":gpu_name,
            "gpu_usage":gpu_usage,
            "VRAM":{
                "total":VRAM_total,
                "used":VRAM_used
            }
        } #将GPU信息存储到字典中
    ram = psutil.virtual_memory() #获取内存信息
    ram_total = ram.total / (1024 ** 3) #将内存总量转换为GB
    ram_used = ram.used / (1024 ** 3) #将已用内存转换为GB
    ram_usage = ram.percent #获取内存使用率 
    device_info["ram"] = {
        "ram_total":ram_total,
        "ram_used":ram_used,
        "ram_usage":ram_usage
    } #将内存信息存储到字典中 
    return device_info

if __name__ == "__main__":
    while True:
        device_info = get_device_info() #获取设备信息
        message = f"CPU: {device_info['cpu']['cpu_name']}\nGPU: {device_info['gpu']['gpu_name']}\nCPU {device_info['cpu']['cpu_usage']:.2f}%|GPU {device_info['gpu']['gpu_usage']:.2f}%\nVRAM: {device_info['gpu']['VRAM']['used']:.2f}GB/{device_info['gpu']['VRAM']['total']:.2f}GB\nRAM: {device_info['ram']['ram_used']:.2f}GB/{device_info['ram']['ram_total']:.2f}GB"
        print(message) #在控制台打印设备信息
        send(message) #发送设备信息到vrchat聊天框
        time.sleep(3) #每3秒更新一次设备信息