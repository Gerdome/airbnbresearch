# Implementing a mobile experiment with  360° representations

This is the project for implemting an experimental setup for a behavioral study to examine the influence of 360° representations on customers.


- *Space for some screenshots and/or screen recordings* - 


The project is structured into three parts and built accordingly with:

* [Otree](https://otree.readthedocs.io/en/latest/) - Mobile web framework (based on Django) used for implementing controlled behavioral experiments.
* [react360](https://facebook.github.io/react-360/docs/what-is.html) - VR cross platform framework used for creating 360° representations on the web.
* [Django](https://www.djangoproject.com/) - Framework for web development used for tracking behavior in backend.
	

## Getting Started

As of now (May 2019), the three different parts are pushed to three seperate Gitlab repositories: 
* **360** - This repository (Otree)
* [360-react](https://git.scc.kit.edu/yn2099/360-react) (react360)
* [360-behavior](https://git.scc.kit.edu/yn2099/360-behavior) (Django)

### Interplay between Otree, React360 and Django

**Otree** is used for implementing the experiment. It is building the mobile web frontend, participants will interact with when conducting the experiment.

**React360** renders the 360° representations on a seperate web url and is embedded into the experimental environment using **<iframe>**\.

In order to track the influence of our 360° representations and compare the behavior to the behavior in traditional settings, we need to track the participants interaction.

To do so, every event such as touch, swipe, looking at the pictures and exploring the virtual reality are tracked and saved using our own custom Rest APIs in **Django**.


### Setup

First, clone all individual repositories ([360](https://git.scc.kit.edu/yn2099/360),  [360-react](https://git.scc.kit.edu/yn2099/360-react), [360-behavior](https://git.scc.kit.edu/yn2099/360-behavior)).

It is recommended to create virtual environments for the **python** projects (Otree and django).

```
python -m venv 360env
```

A list of the required dependencies can be found in each repository.

```
pip install -r requirements.txt
```

In order to install the required dependencies for **react360**, cd to the package.json file inside the **360-react** repository and:

```
npm install
```

## Running on development server

We need three seperate development server for testing our experiment for the first time. 

### Otree

Inside the **360** repository, cd to the manage.py file and:

```
otree devserver 0.0.0.0:8000
```

### React360

Inside the **360-react** repository, cd to the client.js file and:

```
npm start
```

### Django

Inside the **360-behavior** repository, cd to the manage.py file and:

```
python manage.py runserver 0.0.0.0:8010
```


