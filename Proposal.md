# Nathan's Spring Intensive Deliverable Proposal

## Copy this file, fill it out, and push it up to your project's repo.

Dates 3/16-3/25

**My Name:**
Nathan Pillai

**Project Name:**
Toxic Comments

**Is your project New or Old?**
New

**Is your project Solo or Team?**
Solo


## Code Structure and Design

The design of the application will be a one page web app. There will be a user input box for copy pasting text and a submit button. Once the toxicity score is calculated, then it will appear on the same page.

The code structure will be a simple backend api that handling the machine learning processing and a front end for displaying results.


## Model Evaluation Metrics

### Plain Lstm
* 'test_f1': .8968
* 'test_precision': .8904
* 'test_recall': .9038

### LSTM w/ Attn
* 'test_f1': .9024,
* 'test_precision': .9058,
* 'test_recall':.8995

### LSTM w/ CNN
* 'test_f1': .9060,
* 'test_precision': .9073,
* 'test_recall':.9051



## Description

**Write a paragraph summary of the current status of your project, what you hope to achieve during the intensive, how and why**
Copy and paste a comment, email, or any piece of text and see how it scores in terms of its toxicity. Scale of toxicity is a percentage from 0 - 100. Hopefully people can use this application to get an objective view of their comments on others.


## Objective 1:
Create at least 2 different classification models for comparison.

**Why do you want to meet this objective? How will it improve your project?**
In order to return a level of toxicity, I need to create a machine learning model that accepts text and outputs a probability level of toxicity.

**How will you demonstrate completion of your objective?**
Once text is submitted, the text will be evaluated on the backend by the classification model and a toxicity score will be returned. All model training and validating will be done in Google Colab Notebooks, but the models themselves will be utilized in the backend of a web application.

## Objective 2:
Model evaluation for classification models

**Why do you want to meet this objective? How will it improve your project?**
Model evaluation is an important part of building a machine learning project to understand how different model architectures compare and whether the model you end up using reaches the level of performance desired in the metrics you need.

**How will you demonstrate completion of your objective?**
In the README.md of this project I will be adding the 10 fold cross validation scores of what models were utilized. Metrics will include: recall, precision, and f1-score.

## Objective 3:
Deploy Web Application
**Why do you want to meet this objective? How will it improve your project?**
I want everyday users to be able to interact with my toxic classification models. To do this I will add an input box for text that the user may submit. Once submitted, the text will be evaluated by the model and a toxicity score will be displayed on the screen for the user to see.

**How will you demonstrate completion of your objective?**
UI components in the web app for text input and score display.

## Evaluation

**You must meet the following criteria in order to pass the intensive:**

- Students must get proposal approved before starting the project to pass
- SOLO
   - Must score an average above a 3 on the [rubric]
- TEAM
   - Must score an average above 3 on the [rubric]
   - Each individual completes 2 of the 3 objectives from their proposal
- Pitch your product


[rubric]:https://docs.google.com/document/d/1IOQDmohLBEBT-hyr-2vgw1mbZUNsq3fHxVfH0oRmVt0/edit



## Approval Checklist
- [X] If I have a team project, I wrote this proposal to represent my work and only my work
- [X] I have completed all the necessary parts of this proposal
- [X] I linked my proposal in the Spring Intensive Tracker

### Sign off

**Student Name:**                
> Nathan Pillai / March 16, 2020
**Make School Advisor Name**
> Milad
