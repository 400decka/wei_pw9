# Copyright 2024
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Battery voltage monitor node for the wei_pw9 ROS package."""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class BatteryMonitor(Node):
    """Monitor the battery voltage topic and log low-voltage warnings."""

    def __init__(self) -> None:
        """Initialize the battery monitor node."""
        super().__init__('battery_monitor')
        self.subscription = self.create_subscription(
            Float32,
            'battery_voltage',
            self.listener_callback,
            10,
        )
        self.get_logger().info('Akkumulátor monitorozó elindult.')

    def listener_callback(self, msg: Float32) -> None:
        """Handle incoming battery voltage measurements."""
        voltage = msg.data
        if voltage < 12.0:
            self.get_logger().warning(
                'ALACSONY FESZÜLTSÉG! Jelenlegi érték: %.2f V. '
                'Töltés javasolt!',
                voltage,
            )
        else:
            self.get_logger().info('Feszültség rendben: %.2f V', voltage)


def main(args=None) -> None:
    """Run the battery monitor node."""
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