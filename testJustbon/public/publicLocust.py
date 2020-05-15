# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# Time:2019/6/21 16:14
import os,re,time
from public.publicExcel import PublicExcel

class PublicLocust:
    def __init__(self):
        devices = "5376f2f6"
        self.devices = devices
        self.excel = PublicExcel("../report/locust.xls")

    def get_cpu(self):
        """
        cpu
        :return:
        """
        cmd = 'adb -s '+self.devices+' shell "dumpsys cpuinfo |grep -w com.hxdsw.brc"'
        try:
            lines = os.popen(cmd).readlines()[0]
            if "com.hxdsw.brc" in lines:
                result_cpu = lines.lstrip().split("%")
                return result_cpu[0]
            else:
                return "0"
        except:
            return "0"

    def get_memory(self):
        """
        内存
        :return:
        """
        cmd ="adb -s "+self.devices+" shell dumpsys meminfo com.hxdsw.brc"
        lines = os.popen(cmd).readlines()
        for line in lines:
            if re.findall("TOTAL",line):
                result = re.findall("(\d+) ",line.lstrip())

                return result[0]

    def get_fps(self):
        """
        fps
        :return:
        """
        cmd = "adb -s "+self.devices+" shell dumpsys gfxinfo cmd.hxdsw.brc"
        lines = os.popen(cmd).readlines()

    def get_battery(self):
        """
        电量
        :return:
        """
        cmd = "adb -s "+self.devices+" shell dumpsys battery"
        lines = os.popen(cmd).readlines()
        for line in lines:
            if re.findall("level",line):
                return re.findall("(\d+)",line)[0]

    def get_flow(self):
        """
        流量
        :return:
        """


    def run(self):
        for i in range(50):
            time.sleep(6)
            self.excel.write_excel(1,i+1,0,time.strftime("%H:%M:%S",time.localtime()))
            self.excel.write_excel(1,i+1,5,self.get_cpu())
            self.excel.write_excel(1,i+1,3,self.get_memory())


if __name__ == '__main__':
    loccust = PublicLocust()
    print (loccust.get_cpu())
    # print (loccust.get_memory())
    # print (loccust.get_battery())
    # print(loccust.run())