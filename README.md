# Implementing a mobile experiment with  360° representations

This is the project for implementing an experimental setup for a behavioral study to examine the influence of 360° representations on customers.

## Example

###Regular Airbnb Clone

<img src="https://git.scc.kit.edu/yn2099/360/raw/master/Examples/Airbnb_clone_1" width="200">
> <img src="https://git.scc.kit.edu/yn2099/360/raw/master/Examples/Airbnb_clone_2" width="200">


###Virtual Reality Airbnb Clone

<img src="https://git.scc.kit.edu/yn2099/360/raw/master/Examples/Airbnb_clone_1" width="200">


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

**React360** renders the 360° representations on a seperate web url and is embedded into the experimental environment using **iFrame**\.

In order to track the influence of our 360° representations and compare the behavior to the behavior in traditional settings, we need to track the participants interaction.

To do so, every event such as touch, swipe, looking at the pictures and exploring the virtual reality are tracked and saved using our own custom Rest APIs in **Django**.


### Initial Setup

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

This will render your 360° image under http://hosturl:8081/index.html.

### Django

Inside the **360-behavior** repository, cd to the manage.py file and:

```
python manage.py runserver 0.0.0.0:8010
```
## Quick Otree Guide
When first running the server, the admin interface is accessible via: http://localhost:8000/demo, or via your corresponding url (e.g. http://0.0.0.0:8000/demo).
See [Otree Admin Documentation](https://otree.readthedocs.io/en/latest/admin.html?highlight=admin) for further information.

As you can see, the Air BnB Research App is already set up.

After opening the App, you will see that for each participant a corresponding URL has been automatically created. 

#### Change Configurations
In order to change for instance the number of participants:
Inside the **360** repository, open the settings.py file and change the configurations accordingly:

```
SESSION_CONFIGS = [
    {
        'name': 'airbnbresearch',
        'display_name': "AirBnB Research",
        'num_demo_participants': 3,
        'app_sequence': ['vr_screen'],
    },
]
```

The App Sequence references to the already created **vr_screen** folder.

### Customize Pages
Inside the **vr_screen** folder, open the pages.py file. Here you can add new pages or adjust the order of your sequence.

```
class MyPage(Page):
    form_model = 'player'
    form_fields = ['name', 'age','gender']

class Results(Page):
    pass

class VrPage(Page):
    pass

class RegularPage(Page):
    pass

class VRQuestionnaire(Page):
    pass

class RegularQuestionnaire(Page):
    pass

page_sequence = [
    MyPage,
    RegularPage,
    RegularQuestionnaire,
    VrPage,
    VRQuestionnaire,
    Results
]
```

Each Page is linked to an **html** template with the matching name inside the **vr_screen/templates/vr_screen** folder.

**RegularPage.html** tries to clone the Air BnB Layout with basic **html bootstrap** containers.
**VrPage.html**  adds the virtual reality representation by embedding our **react-360** world via **iFrame**.

By changing the **templates**, you can adjust the look and feel of your experiment.

As you can see, **forms** (used for questionnaires as well) can be passed within the Page classes and are rendered automatically.

## 360° Representation
The rendered representation ('npm start' inside the 360-react folder) is accessible under: http://hosturl:8081/index.html.

This page is embedded via **iFrame** in our Otree **html templates**:

```
<iframe 
  class = "frame"
  src="http://ec2-18-197-31-208.eu-central-1.compute.amazonaws.com:8081/index.html" 
  id = 'frame'
  onload='javascript:(function(o){o.style.height=o.contentWindow.document.body.scrollHeight+"px";}(this));' 
  style="height:350px;width:100%;border:none;overflow:hidden;" 
  allow="gyroscope; accelerometer"
  ></iframe> 
  ```

**Gyroscope** is allowed, so that participants can navigate inside the virtual AirBnB Environment by tilting their mobile device.

The **onload** parameter allows additionally to scroll within the iFrame.

### Embed VR fullscreen in experimental environment.

While conducting the experiment, Otree assigns new URLs to certain sessions and creates individual URLs for every participant. 
Hence, it is not possible to open a third party URL (in this case our react-360 URL in fullscreen) and then go back to the experimental URL.

In order to still be able to open the 360° environment in fullscreen mode, we dynamically adjust the size of our iFrame using clickable containers.
This way, the participant is still inside our experimental environment while exploring the 360° images.

** In Html Body**
```
<div class = "fullscreen" id = "fullscreen" align = "center">
FullScreen
</div>
```
** In Html Script**
```
document.getElementById("fullscreen").addEventListener("click", changeFrame);

 function changeFrame () {
     frame = document.getElementById("frame")
     frame.style.position = 'fixed';
     frame.style.top = '0px';
     frame.style.left = '0px';
     frame.style.bottom = '0px';
     frame.style.right = '0px';
     frame.style.width = '100%';
     frame.style.height = '100%';
	
     document.getElementById("back").style.visibility = 'visible';
}
```


### Change Images
Inside the **360-react** repository, save your 360° images in the **static_assets/** folder.

Then open the client.js file and change the loading of the initial environment.
```
 r360.compositor.setBackground(r360.getAssetURL('your_360_image.jpg'));
```

## Behavior Data 

### Built-in Otree data
Otree has a built-in data tracker, that allows to examine the behavior (such as time spent on each page) of the participants.

In the admin interface, click on "Data" (0.0.0.0:8000/export/) to download the data as CSV or Excel.

However, it only provides visibility of the participants behavior to a certain degree. In order to examine the influence of 360° representations on our participants, we need to track more behavior such as:
- time spent while exploring the 360° representation
- which parts of the 360° representation were explored (and how long)
- time spent while looking at correnponding regular images

### Implement Tracker
To do so, we built our own **RESTful API** using the [**Django Rest Framework**](https://www.django-rest-framework.org/), that gets addressed whenever a certain behavior of the participant shall be tracked.

#### Setup Django Backend
First, we set up our django project called **bnbResearchBackend** and our django app **backend** within that project. (See [**Django Documentation**](https://docs.djangoproject.com/en/2.2/) for further information)

In the resulting **360-behavior** repository, we set up two different URLs within our **backend/urls.py** file that serve as our APIs:

- One that gets addressed within our Otree html templates for tracking certain clicks/scrolls/touches (hosturl:8010/api/event/create/).
- And one that gets addresses within our react-360 index file for tracking the locations the participants look at (hosturl:8010/api/react/create/).

Both APIs have a **ListView** Interface for displaying the tracked data and a **CreateView** interface for tracking new behavior data.

```
urlpatterns = [
    path('react', ReactListView.as_view()),
    path('react/create/', ReactCreateView.as_view()),
    path('event', EventListView.as_view()),
    path('event/create', EventCreateView.as_view())
]
```

Both views connect through serializers with our models. (See [serializer documentation](https://www.django-rest-framework.org/api-guide/serializers/) for further information

Our models contain the essential fields that we use for storing information in our database.
They are created in the **backend/models.py** file

**Example model** for tracking camera ange in virtual reality:

```
class react360(models.Model):
    timestamp = models.CharField(max_length = 100, default = '20.05.2019')
    x_axis = models.IntegerField(default=0)
    y_axis = models.IntegerField(default=0)
```


#### API call within HTML template

```
function trackEvent() {
        $.post("http://hosturl:8010/api/event/create",
        {
          item: "Room Image",
          event: "Touch "
        });
    }
```
#### API call within react-360

```
	RCTDeviceEventEmitter.addListener('onReceivedInputEvent', e => {
					this.setState({
    aov: VrHeadModel.rotation()
  })

saveData() {
    const message = { 
      x_axis:  Number((this.state.aov[0]).toFixed(0)),
      y_axis: Number((this.state.aov[1]).toFixed(0))
      }  
      
    axios
      .post('http://hosturl:8010/api/react/create/', message)
      .then(response => {  
      })
      .catch(error => console.log(error));  
}
```
#### How to track other events

The behavior of the participants while browsing through the Air BnB App can be tracked by adding event listeners to certain containers in our html templates.


**Give containers Ids** (inside the body tags):

```
<div class="container" id="demo">
     <div class="media">
      <div class="media-left media-top">
        <img src="https://img.icons8.com/material-outlined/32/000000/exterior.png" class="media-object" style="width:20px">
      </div>
      <div class="media-body">
        <h5 class="media-heading"><b> Private room in house</b></h5>
        <b><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, s aliqua..</p></b>
       </div>
      </div>
     </div>
```
Add **Event Listener** to containers and **call API** function when event such as **click** occurs (inside the scripts tags):

```
document.getElementById("demo").addEventListener("click", trackEvent);
```

Other trackers can be created by adding IDs to the areas of interest and adding event listeners such as clicks, touches, scrolls to them.
In case other information than then ones provided through our backend models shall be tracked, the models can be adjusted or new ones can be added (also new url necessary)

### How to track other data with custom models
**Add models**

**Set up new URLs**

**Create new APIs**




