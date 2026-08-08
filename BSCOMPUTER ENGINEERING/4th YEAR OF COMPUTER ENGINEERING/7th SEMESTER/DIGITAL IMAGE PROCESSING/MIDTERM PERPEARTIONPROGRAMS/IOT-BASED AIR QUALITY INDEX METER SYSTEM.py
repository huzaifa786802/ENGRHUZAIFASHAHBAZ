from graphviz import Digraph

# Create a directed graph
dot = Digraph("IoT-based_AQI_Meter_System_Architecture", format="png")

# Set graph attributes
dot.attr(rankdir="TB", size="10")

# Define Layers
layers = {
    "Data Collection Layer (Hardware)": "green",
    "Connectivity Layer": "blue",
    "Data Processing & Storage Layer": "red",
    "Visualization & User Interface Layer": "yellow",
    "Development & Maintenance": "gray"
}

# Add nodes for layers
for layer, color in layers.items():
    dot.node(layer, layer, shape="box", style="filled", fillcolor=color)

# Define Components in each layer
components = {
    "Data Collection Layer (Hardware)": [
        "Sensor Nodes\n(ESP32/ESP8266, MQ Sensors, PM2.5, PM10)",
        "Power Management\n(Battery Pack, Charger, Adapter)",
        "Hardware Enclosure\n(Weatherproof Housing, Breadboard, Wires)"
    ],
    "Connectivity Layer": [
        "Communication Protocol\n(MQTT, HTTP, WebSockets, Wi-Fi)",
        "Authentication\n(API Keys, Auth Mechanisms)"
    ],
    "Data Processing & Storage Layer": [
        "Cloud Services\n(AWS IoT, Firebase)",
        "IoT Platform\n(ThingSpeak, Adafruit IO)",
        "Database\n(SQL/NoSQL, Excel, Export)"
    ],
    "Visualization & User Interface Layer": [
        "Mobile Application\n(Android Studio, Kotlin, Java)",
        "Web Dashboard\n(Grafana, Custom Web Interface)",
        "Data Analysis\n(Matplotlib, Python)"
    ],
    "Development & Maintenance": [
        "Development Tools\n(VS Code, Arduino IDE, PlatformIO, GitHub, Eclipse IDE)"
    ]
}

# Add nodes for components
for layer, comps in components.items():
    for comp in comps:
        dot.node(comp, comp, shape="box")
        dot.edge(layer, comp)  # Connect layers to their components

# Render and save the diagram
dot.render("IoT_AQI_Meter_Architecture", format="png", cleanup=False)
print("System Architecture Diagram has been generated successfully!")
