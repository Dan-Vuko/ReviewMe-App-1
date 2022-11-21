# Programming Task
## _ReviewMe_

ReviewMe uses a pool of culinary experts to rate restaurants based on the quality of their food, drink, and atmosphere. It is possible that a critic will be unable to assess one of these three elements, in which case the aspect will be marked as "N/A"(Not Assessed). Otherwise, they provide a score between 1 and 5, with 1 being the worst and 5 being the finest.
\
ReviewMe wants the computer to gather the restaurant name and ratings from no more than ten critics, and then calculate the average, maximum, and minimum score for each of the three criteria.

## Features

- Allows user to input name of restaurant, the amount of critics & the rating for food, wine & atmosphere.
- Calculates the average score for food, wine and atmosphere.
- Identifies the lowest and highest score given for food, wine and atmosphere.

## Tech

ReviewMe uses a number of open source projects to work properly:

- [Python](https://www.python.org/) - Python is a high-level, interpreted, general-purpose programming language. 
- [Linux Bash](https://www.linux.org/) - Bash is a Unix shell and command language written by Brian Fox for the GNU Project as a free software replacement for the Bourne shell.

## Installation

ReviewMe requires [Python](https://www.python.org/) v3.10.5 to run.

Extract the pt1.tgz file using linux bash, or by any other means neccesary. This should result in readme.md and reviews.py being extracted to the directory.

```sh
tar -zxf pt1.tgz
```

Check Python version & Installation

```sh
Check version
python --version

For windows - Download latest version from the official website: 
https://www.python.org/downloads/

For Centos - use yum:
sudo yum install python3

For Ubuntu - use apt-get:
sudo apt install python3
```

## License

UNE
