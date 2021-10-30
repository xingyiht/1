# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
	x = []
	y = []
	x_range = [0, 10]
	axes = plt.gca()
	axes.set_xlim(x_range[0], x_range[1])
	axes.set_ylim(0, 10)  #定义绘制坐标轴
	line, = axes.plot(x, y, 'r-')#定义线，r-为红色
	data = 0.00		
while True:
		if data >= 10:
			x_range[0] += 1
			x_range[1] += 1
			axes.set_xlim(x_range[0], x_range[1])#动态x轴
			
			

		x.append(data)
		f=open('test.txt')
		s = f.readline()
		num=int(s)
		y.append(num)#读取流量
		axes.set_ylim(num-5,num+5 )#动态y轴
		line.set_xdata(x)
		line.set_ydata(y)#画线
		plt.pause(1)#停一秒
		data += 1#x+1
plt.pause(0)


#需要安装numpy和matplotlib模块
