# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 01:28:18 2019

@author: Byen23
"""

# 7th Program to be uploaded to github

"""Using Variables and Assign Statements"""

'''Write a script that will use distance in kilometers and time in hours to calculate and print out speed in kilometers per hour, miles per hour, and meters per second.'''

'''The formula for calculating speed is distance/time = speed.
	To convert kilometers to miles, divide the kilometers by 	     	1.6.
	To convert kilometers to meters, multiply the kilometers by 		1,000.
	To convert hours to seconds, multiply hours by 3,600.'''
	
distance_in_km = 150
time_in_hours = 2

distance_in_mi = distance_in_km / 1.6
distance_in_mtrs = distance_in_km * 1000

time_in_seconds = time_in_hours * 3600

speed_in_kph = distance_in_km / time_in_hours
speed_in_mph = distance_in_mi / time_in_hours
speed_in_mps = distance_in_mtrs / time_in_seconds

print("The speed in kilometers per hour is:", speed_in_kph)
print("The speed in miles per hour is:", speed_in_mph)
print("The speed in meters per second is:", speed_in_mps)


	
