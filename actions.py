#from wallaby import *
import wallaby as w
import constants as c

def turn_left(speed, time):
    w.motor(c.rMotor, speed)
    w.msleep(time)
    w.ao()

def turn_right(speed, time):
     w.motor(c.lMotor, speed)
     w.msleep(time)
     w.ao()

def move(speed, time):
    w.motor(c.lMotor, 6+speed) #int?
    w.motor(c.rMotor, speed)
    w.msleep(time)
    w.ao()

def turn(lspeed, rspeed, time):
    w.motor(c.lMotor, lspeed)
    w.motor(c.rMotor, rspeed)
    w.msleep(time)
    w.ao()

def attack(time):
    w.set_servo_position(c.servo, c.attack_position)
    w.msleep(time)
    w.ao()

def drive_until_black():
    while w.analog(c.left_tophat)< c.on_black and w.analog(c.right_tophat) < c.on_black:
        move(30, 10)
    if w.analog(c.left_tophat) >= c.on_black:
        while w.analog(c.right_tophat)< c.on_black:
            turn_left(30, 10)
    else :
        while w.analog(c.left_tophat)< c.on_black:
            turn_right(30, 10)
    w.ao()

def follow_line(time):
    sec = w.seconds()
    while (w.seconds() - sec) < time : #help
        if w.analog(c.right_tophat) >= c.on_black:
            turn(30, 90, 10)

        else:
            turn(90, 30, 10)


