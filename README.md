# Toy Robot Simulator

## Description

• The application is a simulation of a toy robot moving on a square tabletop, of
dimensions 5 units x 5 units.
• There are no other obstructions on the table surface.
• The robot is free to roam around the surface of the table, but must be prevented
from falling to destruction. Any movement that would result in the robot falling from
the table must be prevented, however further valid movement commands must still
be allowed.
The application should be able to read in any one of the following commands:
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
• PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH,
EAST or WEST.
• The origin (0,0) can be considered to be the SOUTH WEST most corner.
• The first valid command to the robot is a PLACE command, after that, any sequence
• of commands may be issued, in any order, including another PLACE command. The
• application should discard all commands in the sequence until a valid PLACE command
has been executed.
• MOVE will move the toy robot one unit forward in the direction it is currently facing.
• LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without
changing the position of the robot.
• REPORT will announce the X,Y and F of the robot. This can be in any form, but standard
output is sufficient.
• A robot that is not on the table should ignore the MOVE, LEFT, RIGHT and REPORT
commands.
• Input can be from a file, or from standard input, as the developer chooses.
• Provide test data to exercise the application.
Constraints:
• The toy robot must not fall off the table during movement. This also includes the
initial placement of the toy robot.
• Any move that would cause the robot to fall must be ignored.
Here is some example input and output:
a)
PLACE 0,0,NORTH
MOVE
REPORT
Output: 0,1,NORTH
b)
PLACE 0,0,NORTH
LEFT
REPORT
Output: 0,0,WEST
c)
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
Output: 3,3,NORTH

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)


## Setup

1. Clone the repository:
   ```sh
   https://github.com/rajprashant84/Mars_Rover.git
   cd Mars_Rover

### Set up a virtual environment:

- **On Unix or MacOS**:
  ```sh
  python3 -m venv venv
  source venv/bin/activate

- **On WindowsS**:
  ```sh
  python -m venv venv
  venv\Scripts\activate




### Install the required dependencies

pip install -r requirements.txt

### Run code
python main.py 

###  Running Tests

python -m unittest discover -s tests



### Key Sections

- **Description**: Overview of the project.
- **Project Structure**: Explains the directory layout.
- **Setup**: Instructions to set up the project.
- **Usage**: How to run the application with example commands.
- **Running Tests**: How to run tests.
- **Code Overview**: Brief description of key modules.
- **License**: Licensing information (you may adjust as needed).

This `README.md` file should provide a comprehensive guide for anyone who wants to understand, set up, and use your project.



