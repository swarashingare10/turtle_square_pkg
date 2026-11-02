import time
import math
import rclpy
from geometry_msgs.msg import Twist

def stop(publisher):
	msg=Twist()
	publisher.publish(msg)
	time.sleep(0.5)

def move(publisher):

	msg=Twist()
	msg.linear.x=2.0
	msg.angular.z=0.0
	publisher.publish(msg)

	time.sleep(2.0)

	stop(publisher)

def turn(publisher):

	msg=Twist()
	msg.linear.x=0.0
	msg.angular.z= 2.0
	publisher.publish(msg)

	turn_time=(math.pi/2)/2.0
	time.sleep(turn_time)

	stop(publisher)

def square(publisher):
	while True:
		move(publisher)
		turn(publisher)

def main():
	rclpy.init()
	node=rclpy.create_node('square_mover')
	publisher=node.create_publisher(Twist, '/turtle1/cmd_vel', 10)

	time.sleep(1.0)

	try:
		square(publisher)
	except KeyboardInterrupt:
		print("stopped by the user")
		stop(publisher)
	node.destroy_node()
	rclpy.shutdown()

if __name__=='__main__':
	main()

