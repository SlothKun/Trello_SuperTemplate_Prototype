# TRELLO SUPERTEMPLATE PROTOTYPE

## Introduction 
SuperTemplate allows you to register and apply templates to all of your Trello's boards in your commandline on any platform.


## Installation
  python 3.9 was used in this project along with those libs (you'll need to install these) : 
  - requests
  - pprint
  - sys
  - sqlite3

  To install SuperTemplate you can type : 
 ```
  sudo git clone https://github.com/SlothKun/Trello_SuperTemplatePrototype.git
 ```
 
## Setup
 ```
  cd src/
  python main.py
 ```
 
When using the app for the first time, you'll be asked to create an user.\
Creating an user requires you to give your trello's USERNAME, your trello's APIKEY and your trello's APITOKEN\
(All of these are stored locally on the database located at '/src/config/Database.db' which you can modify anytime you want.)

/!\ IT IS IMPORTANT THAT YOU SPECIFY YOUR REAL TRELLO USERNAME (under 'profile & visibility' section, the one beginning with '@') /!\

To get the token please refer to : https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/.

If all the informations are correct, you'll be able to log in using the app.

## Create a template
Once you've selected the board on which you want to apply a template, the app will, if you haven't created a template yet, ask you to create one.\
The template creation doesn't have a lot of option for the moment, you'll only be able to include/exclude your lists from the template you want to create, you'll not be able to include/exclude specific card in specific list. If you include a list, it'll include all cards in that list in the template.\
Only lists (and lists' cards) included will be modified when you'll apply the template to your board.\
When you're done, continue and enter the template name and there's it, you've create your first template.

To apply, choose the template in the list when you select the board again.

### Data saved in template
Here's the design of the database, you can see all informated that is stored and used
![image](https://user-images.githubusercontent.com/25417942/108526053-00146500-72d1-11eb-98c7-ccff05790490.png)


## End note
The project is still a prototype which means a lot a things won't work perfectly. I'll probably give some updates but won't be actively update the project (i think)
If the project interest you & you want to improve it, you're welcome to give me feedbacks, or to improve it by yourself.
