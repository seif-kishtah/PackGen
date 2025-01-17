PackGen - Packet Generator Simulation
PackGen is a simple GUI application built using Qt that simulates a packet generator. It allows users to enter packet details, save them in a "Saved Packets" table, or send them to a "Sent Packets" table. This application is designed to demonstrate basic Qt GUI development and packet simulation.
Table of Contents

Features
Repository Structure
Prerequisites
How to Launch the App
On macOS/Linux
On Windows
How to Use the App

Features

Packet Details Input: Enter packet details such as source, destination, protocol, and payload.
Save Packets: Save entered packets to the "Saved Packets" table for later use.
Send Packets: Send packets to the "Sent Packets" table to simulate transmission.
Simple and Intuitive UI: Built using Qt's powerful GUI framework for a clean and user-friendly experience.

PackGen/
├── CMakeLists.txt              # Root CMake configuration file
├── README.md                   # Project documentation (this file)
├── src/                        # Source code directory
│   ├── main.cpp                # Main application file
│   ├── mainwindow.cpp          # Implementation of the main window
│   ├── mainwindow.h            # Header file for the main window
│   └── mainwindow.ui           # UI file for the main window (created using Qt Designer)
├── resources/                  # Resource files (e.g., icons, images)
│   ├── siemens.qrc             # Resource file for the app
│   └── images/                 # Optional: Folder for images
│       └── icon.png            # Example icon file
└── .gitignore                  # Specifies files to ignore in Git

Prerequisites

Before running the app, ensure you have the following installed:

Qt Framework: Download and install Qt from qt.io.
CMake: Required for building the project. Download from cmake.org.
Git: For cloning the repository. Download from git-scm.com.

How to Launch the App

On Windows

Clone the repository:
git clone https://github.com/your-username/PackGen.git
cd PackGen

Build the application:
mkdir build
cd build
cmake -G "MinGW Makefiles" ..  # Use "Visual Studio 17 2022" for Visual Studio
cmake --build .

Run the application:
Navigate to the build directory and locate the generated executable (PackGen.exe).
Double-click the executable or run it from the command line

How to Use the App

Enter Packet Details:
Fill in the packet details (e.g., source, destination, protocol, payload) in the input fields.
Save Packet:
Click the "Save" button to save the packet to the "Saved Packets" table.
Send Packet:
Click the "Send" button to send the packet to the "Sent Packets" table.
View Packets:
The "Saved Packets" table displays all saved packets.
The "Sent Packets" table displays all sent packets.
