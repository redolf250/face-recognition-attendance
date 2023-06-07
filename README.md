Face Recognition Attendance Tracking System with PySide2 GUI

This GitHub repository contains a comprehensive face recognition-based attendance tracking system with a user-friendly graphical user interface (GUI) built using PySide2. The system utilizes the powerful face-recognition Python library for face detection, OpenCV and NumPy for image processing, SQLite3 as the database management system, and Pandas for exporting attendance records.

Key Features:
1. Face Detection: The system leverages the face-recognition library to detect and locate faces in images or real-time video streams, ensuring accurate face detection even in varying lighting conditions or orientations.

2. Face Recognition: Using state-of-the-art deep learning models, the system can recognize individual faces with high precision, allowing for reliable identification of students, employees, or any registered individuals.

3. Attendance Management: The system efficiently manages attendance records by capturing relevant data such as timestamps, names, and unique identifiers. It employs SQLite3 as the database system to store and manage attendance data securely.

4. Graphical User Interface: The GUI developed with PySide2 offers a seamless and intuitive interface for users to interact with the attendance tracking system. It enables easy registration of individuals, monitoring of attendance status, and generating attendance reports.

5. Image Processing: The system utilizes OpenCV and NumPy libraries to perform image processing tasks such as image resizing, normalization, and pre-processing, ensuring optimal input for face detection and recognition algorithms.

6. Attendance Record Export: With the help of Pandas, the system enables exporting attendance records in various formats such as CSV, Excel, or PDF. This feature simplifies data analysis and integration with other systems.

7. Scalability and Customization: The repository provides a modular and extensible codebase that supports scalability and customization. Developers can easily modify or extend the system's functionalities to meet specific requirements.

8. Documentation and Usage Guide: The repository includes comprehensive documentation and a detailed usage guide, assisting developers and users in understanding the system architecture, installation process, GUI usage, and database management.

By combining the power of PySide2 for GUI, face-recognition library for face detection, SQLite3 for database management, and OpenCV/NumPy for image processing, this open-source repository offers a robust and flexible solution for attendance tracking. It empowers educational institutions, organizations, or events to streamline attendance management processes, improve efficiency, and enhance data accuracy.

Start using the Face Recognition Attendance Tracking System with PySide2 GUI today, and revolutionize attendance management in your environment. Collaborate, contribute, and adapt the system to your specific needs, driving innovation in attendance tracking technology.


To install the application packages before running the main driver.py file, please follow these steps:

1. Ensure that you have Python installed on your system. You can download and install Python from the official Python website (https://www.python.org) if needed. Prefered  version 3.6

2. Navigate to the repository's directory on your local machine using the command line or terminal.

3. Locate the "requirements.txt" file within the repository. This file contains a list of all the necessary packages and their versions required for the application.

4. Open the command line or terminal and navigate to the repository's directory.

5. Run the following command to install the application packages from the "requirements.txt" file:

   ```
   pip install -r requirements.txt
   ```

6. Wait for the command to finish executing. It will download and install all the required packages specified in the "requirements.txt" file.

7. Once the installation is complete, you can proceed to run the main driver.py file. Use the following command:

   ```
   python driver.py
   ```

8. The application will now start running, and you can interact with it as intended.

By following these steps and installing the required packages, you ensure that the application has all the necessary dependencies to function properly.
