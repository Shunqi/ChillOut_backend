
# Pages

+ Stream
	- Filter
+ Add Event
	- Info
	- Loc
+ View Event
	- rating
	- Comment
+ Chat
+ User Management


# Naming Convension:

	API: '^[a-z][_\w]+'
	Table / Entity / Relation: '^[A-Z]\w+'
	Attribute: '^[a-z]\w+'
	List Object: 's{1}$'


# APIs

## GET Event Stream

**Filter: time, local, type**

	[
		{
			Basic Info: 
		}
	]

	SELECT name:, desc:, rating:, host:, FROM Events WHERE time, local, type


## GET Event detail

Event's basic info, filter info


## POST Add Event

**A new event should be updated to both Event and User**

	INSERT INTO Event (All column) VALUES (*)
	INSERT INTO User (events) VALUES (ref, event basic info)


## GET Rating / comment

Event's rating list
Event's comment list

## POST Add Rating / comment

**A new comment and a rating should be updated to both Event and User**

	INSERT INTO Event (ratings) VALUES (*)
	INSERT INTO User (ratings) VALUES (*)


## GET Friend List

User's friend list


## GET User Info

User's basic info
User's event list (rating / comment)


# Data Model

+ Event-[N-N:Relation]-User-[N:N]-User
+ Participation: eid, uid, comment, rating, host / participate
+ Friendship: uid, uid


## Event

	{
		"eid": 0,
		"basic_info": { 
			"eventname": "Poker night", 
			"desc": "Heinz College SA", 
			"rating": 0, 
			"host": "Shunqi", 
		},
		"filter_info": {
			"type": "", 
	        "time": "", 
	        "location": "", 
		},
		"ratings": [ 
			{"uid": 1, "username":"", "rating":0, "time":""} 
		],
		"comments": [ 
			{"uid": 1, "username":"", "comment": "", "time":""} 
		],
	}


## User

	{
		"uid": 1,
		"basic_info": {
			"username": "shunqi",
		},
		"filter_info": {
			"gender": "m",
		},
		"ratings": [
			{"eid": 0, "eventname":"", "rating":0, "time":""} 
		],
		"comments": [
			{"eid": 0, "eventname":"", "comment":0, "time":""} 
		],
	}



