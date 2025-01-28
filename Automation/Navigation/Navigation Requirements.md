# Autonomous Navigation System (ANS)
## Objectives
- Enable the rover to autonomously navigate the lunar surface.

- Detect and avoid environmental hazards.

- Optimize path planning for efficiency and safety.

- Integrate with the Digital Lunar Exploration Sites Unreal Simulation Tool (DUST) for virtual environment navigation.

## Functional Requirements
### P0: Mission-Critical
#### Path Planning and Optimization:

- Shall use the A algorithm* or equivalent for optimal pathfinding. (P0)

- Shall dynamically update the path based on real-time telemetry and environmental changes. (P0)

- Shall detect and avoid obstacles using Visual SLAM (Simultaneous Localization and Mapping). (P0)

- Shall provide real-time alerts for detected hazards (e.g., craters, boulders). (P0)

#### Map Integration:

- Shall display a 2D live map of the lunar surface, tracking the rover’s location and projected path. (P0)

- Shall display designated Points of Interest (POIs) and allow users to add new POIs. (P0)

- Shall track the rover’s speed, angle, and heading using Inertial Measurement Units (IMUs). (P0)

#### Interoperability:

- Shall integrate with the Telemetry Stream Server (TSS) to receive updated destinations and POIs. (P0)

- Shall share navigation data (e.g., waypoints, asset locations) with other systems. (P0)

### P1: High Priority
#### Autonomous Rover Control:

- Shall control the rover in the virtual DUST environment using a joystick and programmable hotkeys. (P1)

- Shall provide predictive analytics for rover resource usage (e.g., power, life support). (P1)

#### Hazard Avoidance:

- Shall recommend alternate routes when hazards are detected. (P1)

### P2: Medium Priority
#### Advanced Path Options:

- Should provide multiple route options (e.g., fastest, safest, most energy-efficient). (P2)

#### 3D Map Integration:

- May include a 3D map for enhanced spatial awareness. (P2)

### P3: Low Priority
#### AI-Powered Navigation Assistance:

- May integrate an AI-powered chatbot to assist with navigation and reduce cognitive load. (P3)

