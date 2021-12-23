# RobinhoodDataVis
- Export your Robinhood portfolio into a CSV file
- Visualize your returns on each holding

# How to use
- Clone this repo
- Create a virtual environment using ```python3 -m venv env``` in the folder you cloned the repo to
- Activate the environment 
- - Windows: ```env/Scripts/Activate.ps1```
- - Linux and Mac : ```source env/scripts/activate```
- Install modules using ```pip install -r requirements.txt```
- Create a file called ```config.py``` with the following contents:
``` 
    username = "<Username>"
    password = "<Password>"
```
- Run the ```main.py``` file

# Example Graph
![Figure](/graphs/Figure_1.png)