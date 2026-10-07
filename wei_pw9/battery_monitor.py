import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class BatteryMonitor(Node):
    def __init__(self):
        super().__init__('battery_monitor')
        self.subscription = self.create_subscription(
            Float32,
            'battery_voltage',
            self.listener_callback,
            10)
        self.subscription
        self.get_logger().info('Akkumulátor monitorozó elindult.')

    def listener_callback(self, msg):
        voltage = msg.data
        if voltage < 12.0:
            self.get_logger().warning(f'ALACSONY FESZÜLTSÉG! Jelenlegi érték: {voltage} V. Töltés javasolt!')
        else:
            self.get_logger().info(f'Feszültség rendben: {voltage} V')

def main(args=None):
    rclpy.init(args=args)
    node = BatteryMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()