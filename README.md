# Tomorrow Challenge Report

### Orestis Zekai, Software Engineer, Athens, August 2021


## Introduction

This report consists the deliverable for the Tomorrow Full Stack Engineer challenge, received on Monday, August
9 in the context of the interview series for the position Back-end Software Engineer (Python). It’s purpose it to
provide the answers for the questions posed in the challenge and also explain and justify the reasoning between
certain choices that were made during the implementation.

## Data Modeling

In order to support the requirements for our application, we have created the following tables:

- Surveys
    This table is used to store the available surveys and some information. The columns are:
    ◦ Survey ID
    ◦ Survey name
- Questions
    This table is used to store information about the questions available. The concept is that a question can be
    used in many surveys. The columns are:
    ◦ Question ID
    ◦ Question Type (single, multiple, free)
    ◦ Question Text
- Answers
    In this table we store all the possible answers for a question. The columns are:
    ◦ Answer ID
    ◦ Question ID (FK to Questions.Question ID)
    ◦ Answer Text
- Survey Questions
    In this table we store pairs of surveys and question. If we search by survey, we get all the questions in this
    survey. The columns are:
    ◦ ID
    ◦ Survey ID (FK to Surveys.Survey ID)
    ◦ Question ID (FK to Questions.Question ID)
- Drivers
    This is a table where we store information for drivers. Every rating/survey response needs to be related to
    a driver. The columns are:
    ◦ ID
    ◦ Driver ID
- Users
    This tables holds information about the users. We have added an extra column called **survey_id**. Based
    on this field, our application can decide whether to send this user a survey to complete, or just a simple
    rating. Every time that a user submits a survey, this value s set to NULL so that the user will not see the
    same survey twice. The columns are:
    ◦ User ID
    ◦ Username
    ◦ Passwd
    ◦ Survey ID (FK to Surveys.Survey ID)
- Ratings
    This table is used to store the ratings the users give to drivers. The columns are:
    ◦ Rating ID
    ◦ User ID (FK to Users.User ID)
    ◦ Driver ID (FK to Driver.Driver ID)
    ◦ Rating (1-5)
    ◦ Rated at
- User Answers
    This table is used to store the answers to the surveys. The columns are:
    ◦ User Answer ID


```
◦ User ID (FK to Users.User ID)
◦ Driver ID (FK to Driver.Driver ID)
◦ Survey ID (FK to Surveys.Survey ID)
◦ Question ID (FK to Questions.Question ID)
◦ Answer Text
◦ Answered at
```
By using these tables, we fully support the requirements of our application.


## Implementation

The frameworks chosen for the implementation are the following:

- **Storage:** MySQL
- **Server:** Python (FastAPI framework)
- **Client:** React

The application is hosted on a virtual machine at okeanos. There are 3 containers running containing the
corresponding applications.

- **Storage**

```
A simple MySQL image is used to run our database. We have provided a start up script that initializes the
database with dummy data.
```
- **Server**

```
Since this position is related to Python, the server is implemented using the FastAPI framework. For the
development of this server, we followed the Domain Driven Design (DDD) approach. In this approach,
the domain and application use cases are completely separated from the infrastructure being used. In that
way, we can change the underlying infrastructure frameworks (i.e. from FastAPI to Flask) without
impacting the application use cases.
```
```
The following endpoints have been implemented:
```
- **Client**

```
A minimal client was developed using the React framework.
```

## Demo Flow

In order to demonstrate our application, we propose the adhere to the following flow:

**1. Login**
    Initially, the user sees a login page. By entering the correct credentials, he can login.

```
We have 5 users. Users 1 and 4 are going to be directed to a survey and the rest to a rating.
```
```
User ID Username Password
1 username1 passwd
2 username2 passwd
3 username3 passwd
4 username4 passwd
5 username5 passwd
```
**2. Ride**
    At this part, the user is logged in. We skip the select destination, search for driver etc. and we assign a
    random driver to him. The if he clicks on the _Ride_ button he performs his ride.


**3. Feedback**
    At this point, the user has completed his ride. Now, depending on whether he was selected to participate
    in a survey, we have the following cases:

```
I. Rating
If the user get directed to the Rating page, this means he was not selected for a survey. In this case,
the user selects the rating and the is “logged out” and gets redirected in the log in page.
```
```
II. Survey
If the user is selected for a survey, he gets redirected to the Survey page. Here, we load the survey the
user needs to fill in and we render it on the screen. Once the user fills the survey (can also be
submitted unfilled, no required fields), the survey responses are stored in the database, and the user
record gets updated so that the user will not see the same survey again. Last, the user is redirected to
the log in page.
```
```
Note: If the user sees the survey and completes it, he will not see it again. We will need to reset the
database manually.
```
In order to play around with the demo, you can navigate to [http://83.212.115.12:3000/.](http://83.212.115.12:3000/.) You can also view the
back-end interactive docs here.


## Bonus Objective

The object has 2 parts:

- Collecting data and training a ML model
- Serving prediction requests

The first part can be achieved by utilizing a NoSQL database (we could also use a relational one, but for machine
learning applications non-relational are more popular). This database will store all the information mentioned in
the description:

- Pick-up time
- Drop-off time
- Pick-up location (GPS lat, log)
- Drop-off location (GPS lat, log)
- Fare amount
- Toll

Besides this information, we will also store an extra identifier that will correspond to a specific city(can be
retrieved from the location). For simplicity, we will not consider cross-city fares.

This information will be retrieved by the **driver**. We can have buckets that contain groups of locations of close
proximity. Using this data, we will train out model and store it. A separate model will be used for each city. On
regular time intervals, the models will be **calibrated**. This means that based on new inputs, even after the users
start using the predictions feature, the model would further train. All the models would be stored on a database as
well (could be a separate one or the same as the training data).

Finally, all drivers would send data for further model training and users will make prediction requests. A high
level diagram would be the following:



