# ClimateFrame
ClimateFrame is a framework that allows you to frame data by defining specific actions that are executed when certain events occur within real time data.


Mission Statement:
------------------
Providing a framework that allows regional experts to communicate their knowledge with local communities.


What a Mission Statement is:
----------------------------
A concise summary of the aims of a project.


The Problem We are Trying to Solve:
-----------------------------------
Currently local experts have no framework that helps them and allows them to automatically issue warnings or inform communities based on current data 

* Bridging the gap between fragmented datasets and local communities
* Combining datasets and knowledge of local experts
* Providing a common interface for building a message system based on customized datasets


The Concrete Use Case is as Follows: 
------------------------------------
* A local expert wants to help vulnerable clients 
* The local expert uses our framework and selects the datasets he/she wants to use
* The local expert knows the vulnerable clients and this specifies messages that will be sent as text messages or ASCII art symbols to the vulnerable clients when certain events in the realtime data occur
* Since the expert knows the local clients he/she gets them to sign up to the service 


Markers of Success:
-------------------
* Local experts to feel involved and enthusiastic. 
* We want governments to see our tool as a chance.
* We want to be the go to place for content providers who are looking for a platform to share info
* We want to enable direct stakeholders to share information with communities.


Indirect Stakeholders:
----------------------
* meterologists
* media 
* news agencies
* data providers
* vulnerable communities


Direct Stakeholders:
--------------------
* key people who want to help communities with data
* meterologists
* media 
* news agencies
* governments


Challenges:
-----------
* Involving key people share that aim to help communities
* Monetizing or making this sustainable
* For key people to reach the communities
* Finding a common and easily usable interface
* Language barriers


Installation:
-------------
```
virtualenv venv
source venv/bin/activate
cd server
pip install -r requirements.txt
```


##  Install [mongoDB](http://mongodb.org/)

According to the mongoDB installation instructions for [linux](https://docs.mongodb.org/master/administration/install-on-linux/), [mac](https://docs.mongodb.org/master/tutorial/install-mongodb-on-os-x/) and [window](https://docs.mongodb.org/master/tutorial/install-mongodb-on-windows/).

### Linux (Ubuntu and Debian)
Import the public key:

```
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
```

Next, for debian:

```
$ echo 'deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
```

Or ubuntu:
```
$ echo echo "deb http://repo.mongodb.org/apt/ubuntu precise/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

```

Then finally for either system:
```
$ sudo apt-get update
$ sudo apt-get install mongodb-org 
```


Running:
--------
```
python server.py
```


TODO:
-----
#### Frontend:
* Rashiq

#### Backend:
* Everyone else
* Using Python Flask


Progress:
---------
### Backend
#### Make Pulse API available
##### Implement Pulse Forecast Endpoint
 * [x] Get forecast data
 * [ ] Create triggers
 * [ ] Create actions
 * [ ] Create recipes that consists of triggers and actions
 * [ ] Save recipes (To a json file or mongodb)
 * [ ] Run scheduled jobs on the recipes that runs every hour
