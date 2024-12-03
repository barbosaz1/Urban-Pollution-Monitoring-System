# Urban Pollution Monitoring System

A Python-based project for monitoring and analyzing urban pollution levels. Designed as part of the **Algorithms and Programming 2024/25 coursework**, this system processes environmental data, generates alerts, and performs various simulations to aid pollution control efforts.

---

## 📋 Project Overview

The **Urban Pollution Monitoring System** analyzes pollution data collected from sensors placed in various urban regions. It processes this data to:
- Display pollution levels in a tabular format.
- Generate pollution alert maps (PAM) to classify areas by severity.
- Simulate pollution adjustments and environmental scenarios.
- Perform calculations to support pollution mitigation efforts, such as identifying optimal sites for air purifiers.

---

## ⚙️ Features

1. **Load and Display Pollution Data**  
   - Reads pollution data from a file and organizes it in a tabular format with values aligned to the right.

2. **Pollution Alert Map (PAM)**  
   - Categorizes pollution levels into four alert levels:  
     - `M`: Moderate  
     - `H`: High  
     - `E`: Extreme  
     - `S`: Severe  

3. **Adjust Pollution Levels**  
   - Simulates the impact of pollution changes by increasing or decreasing all values in the grid.

4. **Alert Level Analysis**  
   - Calculates the percentage of areas falling under each alert level.

5. **Severe Pollution Mitigation**  
   - Determines the pollution increase required for all areas to reach the `Severe` level.

6. **Wind-Driven Pollution Spread Simulation**  
   - Models the effect of wind on pollution levels, spreading severe pollution from North to South.

7. **Optimal Pollution Reduction Site**  
   - Identifies the 3x3 grid area with the highest pollution concentration for targeted reduction.

8. **Safe Column Identification**  
   - Locates the Easternmost column with no Severe pollution, even after simulated wind-driven spread.

---

## 🛠️ Tech Stack

- **Programming Language**: Python  
- **Key Concepts**:  
  - Matrix manipulation  
  - String handling  
  - Conditional logic and simulations  
  - File handling for input and output operations  

---

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/urban-pollution-monitoring.git
