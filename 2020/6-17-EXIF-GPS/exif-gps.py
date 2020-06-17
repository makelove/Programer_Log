# -*- coding: utf-8 -*-

from GPSPhoto import gpsphoto
#读取GPS信息
photo = gpsphoto.GPSPhoto('黄河源头.jpg')
photo.getGPSData()
'''
{'Latitude': 35.019564,
 'Longitude': 95.990063,
 'Altitude': 0,
 'UTC-Time': '18:58:14',
 'Date': '05/31/2020'}
'''

#写入GPS坐标
photo = gpsphoto.GPSPhoto('牛头碑.jpg')
info = gpsphoto.GPSInfo((34.908458,97.492676))
photo.modGPSData(info, 'new_photo.jpg')
#把new_photo.jpg转到iPad上查看地图