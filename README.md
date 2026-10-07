# Autonóm Járművek és Robotok Programozása - Kis Beadandó

Ez a package egy ROS 2 Humble alatt futó egyszerű szimuláció, amely egy jármű akkumulátorának feszültségét publikálja, illetve monitorozza azt.
A csomag két node-ból áll:
1. `battery_publisher`: Másodpercenként véletlenszerű feszültségadatokat (11.5V - 14.5V) publikál.
2. `battery_monitor`: Feliratkozik a feszültségadatokra, és `WARNING` szintű logolást végez, ha az érték 12.0V alá esik.

## Rendszerkövetelmények
- ROS 2 Humble
- Python 3

## Build és Futtatás

1. Workspace inicializálása és build:
bash
cd ~/ros2_ws
colcon build --packages-select wei_pw9
source install/setup.bash
2. Publisher futtatára (egyik terminál):
bash
ros2 run wei_pw9 battery_publisher
3. Monitor futtatása (második terminál):
bash
ros2 run wei_pw9 battery_monitor
## Node és Topic felépítés
mermaid
graph LR
A[battery_publisher]-->|/battery_voltage std_msgs/Float32|
B[battery_monitor]