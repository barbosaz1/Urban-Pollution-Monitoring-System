Urban Pollution Monitoring System
This repository contains a Python-based project for monitoring and analyzing urban pollution levels. Designed as part of the Algorithms and Programming 2024/25 coursework, the system processes environmental data, generates alerts, and performs various simulations to aid pollution control efforts.

📋 Project Overview
The Urban Pollution Monitoring System is a tool to analyze pollution data collected from sensors placed in various urban regions. It processes this data to:

Display pollution levels in a tabular format.
Generate pollution alert maps (PAM) to classify areas by severity.
Adjust pollution data for simulation and analysis.
Perform calculations to support environmental decision-making, such as identifying optimal sites for air purifiers.
⚙️ Features
Load and Display Pollution Data:

Reads pollution data from a file and organizes it in a tabular format with values aligned to the right.
Pollution Alert Map (PAM):

Categorizes pollution levels into four alert levels:
Moderate (M)
High (H)
Extreme (E)
Severe (S)
Adjust Pollution Levels:

Simulates the impact of pollution changes by increasing or decreasing all values in the grid.
Alert Level Analysis:

Calculates the percentage of areas falling under each alert level.
Severe Pollution Mitigation:

Determines the pollution increase required for all areas to reach the Severe level.
Wind-Driven Pollution Spread Simulation:

Models the effect of wind on pollution levels, spreading severe pollution from North to South.
Optimal Pollution Reduction Site:

Identifies the 3x3 grid area with the highest pollution concentration for targeted reduction.
Safe Column Identification:

Locates the Easternmost column with no Severe pollution, even after simulated wind-driven spread.
🛠️ Tech Stack
Programming Language: Python
Concepts Used:
Matrix manipulation
String handling
Conditional logic and simulations
File handling for input and output operations
🚀 Getting Started
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/urban-pollution-monitoring.git
Run the program:
bash
Copy code
python pollution_monitoring.py
📝 Input File Format
The input file should follow this structure:

Header with the city name, date, and time (e.g., Lisboa; 2024/08/23; 13:30).
Dimensions of the pollution grid (e.g., 3 5 for 3 rows and 5 columns).
Pollution data grid, with each value representing pollution levels (e.g., 25 12 65 -33 11).
🎯 Use Cases
This project is useful for:

Environmental monitoring organizations (like the Portuguese Environment Agency) for analyzing urban air quality.
Educational purposes to demonstrate the application of algorithms in real-world problems.
👥 Contributors
Designed and developed by [Your Name/Team] as part of the academic course Algorithms and Programming 2024/25.
