from graphviz import Digraph
# Create a new directed graph
dot = Digraph("IoT-based_AQI_System", format="png")
# Main title
dot.attr(label="IoT-based Air Quality Index Meter System Architecture", fontsize="16", fontcolor="black")
# Data Collection Layer (Hardware)
dot.attr('node', shape='box', style='filled', fillcolor='lightgreen')
dot.node("B", "Data Collection Layer (Hardware)")
dot.node("B1", "Sensor Nodes: ESP32/ESP8266, MQ-135, MQ-5, PM2.5, PM10")
dot.node("B2", "Power Management: Battery Pack, Power Adapter, Charger Setup")
dot.node("B3", "Hardware Enclosure: Weatherproof Housing, Breadboard, Connecting Wires")
dot.edge("B", "B1")
dot.edge("B", "B2")
dot.edge("B", "B3")
# Connectivity Layer
dot.attr('node', shape='box', style='filled', fillcolor='lightblue')
dot.node("C", "Connectivity Layer")
dot.node("C1", "Communication Protocols: MQTT, HTTP/HTTPS, Web API")
dot.node("C2", "Authentication: API Keys, Auth Mechanisms")
dot.edge("C", "C1")
dot.edge("C", "C2")
# Data Processing & Storage Layer
dot.attr('node', shape='box', style='filled', fillcolor='lightcoral')
dot.node("D", "Data Processing & Storage Layer")
dot.node("D1", "Cloud Services: AWS IoT, Firebase")
dot.node("D2", "IoT Platform: ThingSpeak, Adafruit IO")
dot.node("D3", "Database: SQL Database, Excel Export")
dot.edge("D", "D1")
dot.edge("D", "D2")
dot.edge("D", "D3")
# Visualization & User Interface Layer
dot.attr('node', shape='box', style='filled', fillcolor='khaki')
dot.node("E", "Visualization & User Interface Layer")
dot.node("E1", "Mobile Application: Android Studio, Blynk App")
dot.node("E2", "Web Dashboard: Grafana, Custom Web Interface")
dot.node("E3", "Data Analysis: MATLAB, Python")
dot.edge("E", "E1")
dot.edge("E", "E2")
dot.edge("E", "E3")
# Development & Maintenance Layer
dot.attr('node', shape='box', style='filled', fillcolor='gray')
dot.node("F", "Development & Maintenance")
dot.node("F1", "Tools Used: VS Code, Arduino IDE, PlatformIO, GitHub, Eclipse IDE")
dot.edge("F", "F1")
# Main connections
dot.edge("B", "C")
dot.edge("C", "D")
dot.edge("D", "E")
dot.edge("E", "F")
# Render and save the diagram
dot.render("IoT_AQI_System_Architecture", format="png", cleanup=True)
dot.view()  # Open the generated image