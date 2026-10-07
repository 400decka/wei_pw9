# Autonóm Járművek és Robotok Programozása - Kis Beadandó

Ez a csomag egy ROS 2 Humble alatt futó egyszerű szimuláció, amely egy jármű
akkumulátorának feszültségét publikálja és monitorozza.

A csomag két node-ból áll:

1. `battery_publisher`: Másodpercenként véletlenszerű feszültségadatokat
   (11.5 V - 14.5 V) publikál.
2. `battery_monitor`: Feliratkozik a feszültségadatokra, és `WARNING` szintű
   logolást végez, ha az érték 12.0 V alá esik.

## Rendszerkövetelmények

- ROS 2 Humble
- Python 3

## Build és Futtatás

1. Workspace inicializálása és build:

```bash
cd ~/ros2_ws
colcon build --packages-select wei_pw9
source install/setup.bash
```

2. Publisher futtatása (egyik terminál):

```bash
ros2 run wei_pw9 battery_publisher
```

3. Monitor futtatása (második terminál):

```bash
ros2 run wei_pw9 battery_monitor
```

## Node és Topic felépítés

```mermaid
graph LR
    A[battery_publisher] -->|/battery_voltage std_msgs/Float32| B[battery_monitor]
```