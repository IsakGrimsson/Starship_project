
# SWAPI Project

## Description

This project utilises the SWAPI (Star Wars API) to fetch and manipulate Star Wars-related data. This project pulls data on all available starships from the API, and replaces the 'pilots' key URLS with a list of ObjectIDs from the character collection. The starships are then inserted into their own collection.

Other requirements included:

- Work following the **Scrum Framework**
- Use Trello for **Kanban**
- Use an appropriate branching strategy
- Implement **OOP** principles
- Separate code into modules which have one job to do
- Organise modules into files appropriately
- **Test** your code with UnitTest and/or PyTest
- Include a detailed **README.md** describing the project and linking to Kanban board
- Include a **test report** in README document.

## Table of Contents



# Useful Links:

- [Trello Kanban Board](https://trello.com/b/0IGj6Zvj/starship-project)
- [SWAPI API](https://swapi.dev/)

## Features

- Data retrieval from SWAPI.
- Data transformation and field conversion.
- Starship integration with MongoDB for data storage.

## Getting Started

### Prerequisites

- Python 3, using your preferred installation method
- [A working MongoDB installation](https://www.mongodb.com/docs/manual/installation/)
- UnitTest, which is part of the Python Standard Library
- [pymongo](https://pymongo.readthedocs.io/en/stable/) - `pip install pymongo`

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/IsakGrimsson/Starship_project.git
   ```


### Usage
Once the requirements have been installed, navigate to the base folder of this project and run main.py as follows:
```py
python main.py
```
This will then retrieve and transform the data as specified.

# Testing Report:
![test suite image](/test_results_1.png)
![mongo test suite image](/mongo_test_report.png)

# Collaborators:

This project was completed collaboratively by Taslima Hossain, Killian Hughes, Isak Grimsson, Jack Cavanagh, Tommy Ainsworth and Sophie Wilkie
