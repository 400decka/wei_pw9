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

"""Launch file for the Foxglove bridge example configuration."""

import launch
import launch_ros.actions


def generate_launch_description():
    """Return the launch description for the Foxglove bridge example."""
    node = launch_ros.actions.Node(
        package='foxglove_bridge',
        executable='foxglove_bridge',
        parameters=[
            {'port': 8765},
            {'address': '0.0.0.0'},
            {'tls': False},
            {'certfile': ''},
            {'keyfile': ''},
            {'max_qos_depth': 10},
            {'num_threads': 0},
            {'use_sim_time': False},
        ],
    )

    return launch.LaunchDescription([node])