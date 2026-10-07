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

"""Battery voltage publisher node for the wei_pw9 ROS package."""

import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class BatteryPublisher(Node):
    """Publish simulated battery voltage readings every second."""

    def __init__(self) -> None:
        """Initialize the battery publisher node."""
        super().__init__('battery_publisher')
        self.publisher_ = self.create_publisher(Float32, 'battery_voltage', 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('E91 Akkumulátor szimulátor elindult.')

    def timer_callback(self) -> None:
        """Publish a random battery voltage measurement."""
        msg = Float32()
        msg.data = round(random.uniform(11.5, 14.5), 2)
        self.publisher_.publish(msg)
        self.get_logger().info('Publikált feszültség: %.2f V', msg.data)


def main(args=None) -> None:
    """Run the battery publisher node."""
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