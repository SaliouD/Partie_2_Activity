# -*-coding:utf-8 -*
from turtle import *
color('red', 'blue')
begin_fill()
while True:
	forward(200)
	right(170)
	if abs(pos()) < 1:
		break
end_fill()
done()