# milk-project-GUI

## Code purpose

This application is intended for testing cyclic voltammograms from the ivium instrument for determining the content of antibiotics in milk by electrochemical methods.

## Dependencies

To install dependencies run:
```bash
pip install -r requirements.txt
```

## Installation

Use git:
```bash
git clone git@github.com:ShockOfWave/milk-project-GUI.git
```

To make binary file use [pyinstaller](https://github.com/pyinstaller/pyinstaller).

## Usage

- Run app with python or use binary file
```bash
python -m MilkApp
```
<p align="center">
Start window

![Main window](images/start.png)

</p>

- Select file from ivium 

Application displays graph

<p align="center">
Graph example

![Graph example](images/graph.png)

</p>

- Make prediction

You will see small massage

<p align="center">
Prediction example

![Prediction example](images/pred.png)

</p>

- Check full information and save it

Open tab table

<p align="center">
Table example

![Table example](images/table.png)

# License
## MIT

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
