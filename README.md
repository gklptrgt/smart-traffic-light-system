# Smart Traffic Light System
This is my Graduation Project for the University.

![graduation_project](https://github.com/user-attachments/assets/ccbbe95f-5dd7-42b4-89d5-d95f0bff99de)


The purpose of this project is to design and implement a Smart Traffic Light System that
addresses the limitations of traditional traffic light systems and introduces innovative
functionalities to optimize traffic management, improve road safety, and enhance overall
transportation efficiency. By combining advanced technologies, energy efficiency measures,
fail-safe systems, and intelligent sensors, the project aims to revolutionize the way traffic is
regulated at intersections.

# Development Process
## Previous Attempts: Using OSM Map Network
In the initial stages of this project, an attempt was made to utilize the OpenStreetMap (OSM)
network for simulation software. OSM provided accurate and detailed data on road networks,
including traffic flow and road layouts. However, due to the massive size of the network, it posed
significant challenges in terms of computational power required to run realistic simulations. Despite
the accurate data provided by OSM, it was deemed impractical to utilize the network for the project's
simulation requirements.

![shortest path on kyreni road network](https://github.com/user-attachments/assets/2ede4d08-b056-47ba-8e7c-b7d315733b87)

Figure 1: Example of the OpenStreetMap (OSM) network showing road layouts and traffic flow
information with shortest path (red line) using Dijkstra’s algorithm.

![evidence2](https://github.com/user-attachments/assets/2722d7a8-88eb-4968-ba7a-5797c74cd213)

Figure 2: Example of the any line in the OpenStreetMap (OSM) network showing accurate data that
represents how many meters of each section, means it gives exact meters of each line and
intersection.

## 3D Modelling a Road Intersection
To overcome the limitations posed by the OSM map network, the decision was made to create a 3D
model of a real-life road intersection. By leveraging 3D modelling techniques, it became possible to
accurately represent the physical characteristics and geometry of the intersection. This approach
allowed for more control over the simulation environment and provided flexibility in incorporating
various traffic scenarios.

![image](https://github.com/user-attachments/assets/2d89e644-dc20-4818-816f-66919a68c632)

Figure 3: 3D model of a road intersection, created to simulate traffic scenarios and test the Smart
Traffic Light System.

## Simulation Using Ursina Engine
The Ursina engine, a Python-based game engine, was chosen as the framework for developing the
simulation software. The engine provides powerful tools for creating interactive 3D environments
and enables the integration of custom functionalities. By utilizing the Ursina engine, the simulation
software can accurately represent the road intersection, simulate vehicle movements, and visualize
the behaviour of the Smart Traffic Light System in real-time.

The simulation software developed using the Ursina engine incorporates various features, including
dynamic signal control algorithms, intelligent sensors, and data analysis capabilities. It allows for the
testing and evaluation of the Smart Traffic Light System's performance under different traffic
scenarios, providing valuable insights into its effectiveness and potential benefits.

By utilizing 3D modelling and simulation techniques, this project aims to bridge the gap between
theoretical concepts and real-world implementation, enabling a realistic and interactive environment
for testing and refining the Smart Traffic Light System.

![tezgah_gmap](https://github.com/user-attachments/assets/46bd26e0-e9fe-407b-b540-223621e22636)

Figure 4: The 3D modelled road is a real-life place on Kyrenia, Cyprus and this Is the image from the
Google Maps.

The subsequent chapters will delve into the details of the 3D modelling process, the implementation
of the simulation software using the Ursina engine, and the evaluation of the Smart Traffic Light
System's performance in various traffic scenarios.

Within the 3D model of the road intersection, comprehensive efforts were made to replicate real-life
traffic conditions. This involved modelling the cars and traffic lights to create a realistic traffic flow
simulation. The traffic light system was designed to ensure that cars would stop at red lights and
continue moving on green lights, adhering to standard traffic regulations.

The simulation encompasses a total of 16 possible paths that cars can follow within the road
intersection. Each path represents a distinct route that vehicles can take, accounting for different
turning movements and lane configurations.

![image](https://github.com/user-attachments/assets/c0ca281d-d950-4211-81f5-20c1dc5059f8)

Figure 5: Illustration of the 16 possible paths within the road intersection, representing various
turning movements and lane configurations.

Due to the unavailability of IR-sensors to capture real-time data, a randomized approach was
adopted for simulating car movements. Cars are spawned at random paths and random times,
emulating the unpredictability of real traffic flow. Although this approach may not capture the
precise dynamics of actual vehicles, it provides a simulated representation of traffic patterns and
interactions.

To enhance the realism of the simulation, acceleration and velocity properties were incorporated for
the cars. By considering these factors, the simulation accounts for the varying speeds and smooth
transitions observed in real-world traffic scenarios.

To ensure accuracy in the simulation, the duration of each traffic light's green, yellow, and red phases
was measured in real-life conditions. This data was then applied to the simulation, allowing for a
direct comparison between the simulated traffic light timings and the observed timings at the actual
road intersection. This analysis helps evaluate the performance of the Smart Traffic Light System
under different scenarios and determine the most effective signal control strategies.

Additionally, at the bottom of the simulation screen, an "Average Vehicles per Minute" metric is
displayed. This statistical data provides insights into the overall traffic volume and allows for
comparative analysis between different simulation runs. By monitoring this metric, patterns and
trends can be observed, contributing to a better understanding of the system's efficiency and
effectiveness.

# METHODOLOGY
This section outlines the methodology adopted for the development and evaluation of the Smart Traffic Light System. It describes the overall approach taken to design, implement, and assess the system's performance in a simulated environment. The methodology encompasses the steps involved in creating the 3D model of the road intersection, integrating the simulation software, and conducting performance evaluations.
The first step in the methodology involved the design and construction of a detailed 3D model of the road intersection. Utilizing computer-aided design (CAD) tools and techniques, the physical characteristics, road layouts, and traffic infrastructure of the real-life intersection were accurately replicated by using Blender 3D software. 
This process considered lane configurations, traffic signal locations, pedestrian crossings, and other relevant elements to ensure a realistic representation.

![image](https://github.com/user-attachments/assets/2a08884e-76db-47b0-9457-e5e1f8e2d7a7)

Figure 6: Blender 3D software, the replication of the real metric road.
Once the 3D model was complete, the simulation software was integrated into the virtual environment. The simulation software, developed using the Ursina engine, incorporated custom functionalities to emulate real-world traffic scenarios. 
This included the implementation of traffic light control algorithms, vehicle spawning mechanisms, traffic behaviour models, and data analysis capabilities. The integration process ensured that the simulation software interacted seamlessly with the 3D model, enabling the simulation of traffic flow and the evaluation of the Smart Traffic Light System.

![image](https://github.com/user-attachments/assets/1adcdd8e-aa1d-401e-b44c-305a90a74eb9)

Figure 7: Implementation of the Traffic Light system for the simulation. Image shows red light is on and cars stop at the red light.

To evaluate the performance of the Smart Traffic Light System, extensive simulations were conducted using the integrated software. Various traffic scenarios, including different traffic volumes, pedestrian movements, and signal control strategies, were tested to assess the system's effectiveness under different conditions. Simulations were executed multiple times to gather data on traffic flow, waiting times, congestion levels, and other relevant metrics.

Data analysis techniques were then applied to interpret the simulation results and extract meaningful insights. Statistical analysis, visualization tools, and comparative studies were employed to identify patterns, trends, and correlations in the collected data. This analysis helped in understanding the impact of different factors on the system's performance, identifying areas for improvement, and optimizing the signal control strategies for better traffic management.

The methodology also included a validation and verification phase to ensure the accuracy and reliability of the simulation results. The simulated traffic flow, waiting times, and other parameters were compared against observed data from the real-life road intersection to validate the simulation's realism and fidelity. Verification techniques were employed to verify the correctness and consistency of the implemented algorithms and models within the simulation software.

Throughout the methodology, an iterative approach was adopted, allowing for continuous development and refinement of the Smart Traffic Light System. The insights gained from data analysis, validation, and verification were used to improve the system's performance, fine -tune the signal control algorithms, and enhance the simulation environment. Feedback from experts, stakeholders, and users was also considered to ensure that the system met the intended objectives and addressed the identified challenges effectively.
By following this comprehensive methodology, the development, implementation, and evaluation of the Smart Traffic Light System were carried out systematically, ensuring a robust and reliable solution for efficient traffic management. The subsequent chapters will provide detailed insights into the specific steps, findings, and recommendations derived from the methodology, further contributing to the understanding and effectiveness of the Smart Traffic Light System.

# Additional Resources
![image](https://github.com/user-attachments/assets/c41eeaae-96e8-427b-8ce0-528398b67552)

If you like to edit the paths of the cars just uncomment this section from the main.py and comment the spawner function which spawns’ cars for the simulation.

![image](https://github.com/user-attachments/assets/03455726-3652-4f03-b367-7bb4f80d4634)

On the path editor you can click where ever you want to edit the path and then from top right section you can save the paths to the local data holder to use them in the simulation.

# Conclusion
This chapter provided a comprehensive evaluation of the Smart Traffic Light System based on performance metrics, simulation scenarios, and comparative studies. The findings demonstrated the system's effectiveness in preventing crashes, reducing waiting times, optimizing traffic flow, and enhancing energy efficiency. The chapter concluded with insights and recommendations derived from the evaluation results, contributing to the understanding and further development of the Smart Traffic Light System.
The subsequent chapters will delve into specific aspects related to the Smart Traffic Light System, such as the system's design and implementation, advantages, and future directions for research and development.

| Test        | Run 1       | Average of 10 runs | Average waiting time per car |
|-------------|-------------|--------------------|------------------------------|
| Normal      | 14          | 54                 | 45 seconds                   |
| Algorithm 1 | 26          | 74                 | 23 seconds                   |
| Results     | +9 (+%52.9) | +20 (+%37.03)      | -22 seconds (-%48.8)         |

As results show Algorithm 1 performs way better than real life traffic lights. There are 9 more cars passing on first run, 20 more cars on average of 10 tests and 22 seconds less waiting time on red light which decreases air pollution.


