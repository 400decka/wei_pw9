import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class BatteryPublisher(Node):
    def __init__(self):
        super().__init__('battery_publisher')
        self.publisher_ = self.create_publisher(Float32, 'battery_voltage', 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('E91 Akkumulátor szimulátor elindult.')

    def timer_callback(self):
        msg = Float32()
        msg.data = round(random.uniform(11.5, 14.5), 2)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publikált feszültség: {msg.data} V')

def main(args=None):
    rclpy.init(args=args)
    node = BatteryPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()