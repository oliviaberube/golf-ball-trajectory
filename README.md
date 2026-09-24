
# Golf Ball Trajectory and Speed Analysis

Projet developed as part of the third-year Electrical Engineering course *ELE3000 - Projet Personnel en génie électrique* at Polytechnique Montréal

## Description

This project aims to use a high-speed video to detect a golf ball and calculate its 2D trajectory and speed.

Video processing is done in Python using OpenCV

## Features 

- [ ] Video import
- [ ] Golf ball detection
- [ ] Trajectory estimation
- [ ] Speed estimation
- [ ] GUI for results

## Video requirements 

- Minimum frame rate: 120 fps 
- Minimum resolution: 720 p
- Fixed camera, at ball height and perpendicular to the motion

## Technologies
- Python
- OpenCV
- NumPy

## Requirements
- Clone the repository:

```bash 
git clone https://github.com/oliviaberube/golf-ball-trajectory.git
```

- Install dependencies:

```bash 
pip install opencv-python numpy
```

## Usage

Run the main program:

```bash
python ProjetGolf.py
```

 
## Status
In progress
Current work: video acquisition, frame extraction