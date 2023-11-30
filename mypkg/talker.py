import rclpy
from rclpy.node import Node
from person_msgs.msg import Int16

class Talker():
    def __init__(self):
        self.pub = node.create_publisher(Int16, "countup",10)
        self.n = 0

rclpy.init()
node = Node("talker")
talker = Talker()

def cd():
    msg = Int16()
    msg.data = talker.n
    talker.pub.publish(msg)
    tarker.n += 1

node.create_timer(0.5, cd)
rclpy.spin(node)
