
## Pages
Stream
	Filter
Add Event
	Info
	Loc
View Event
	rating
	Comment
Chat
User Management


## Naming Convension:
API: '^[a-z][_\w]+'
Table / Entity / Relation: '^[A-Z]\w+'
Attribute: '^[a-z]\w+'


## APIs
# Event Stream
**Filter: time, local, type**
[
	{
		Basic Info: 
	}
]
SELECT name:, desc:, rating:, host:, FROM Events WHERE time, local, type
Event list

# Event detail
**A new event should be updated to both Event and User**
Event's basic info, filter info

# Rating / comment
**A new comment and a rating should be updated to both Event and User**
Event's rating list
Event's comment list

# Friend List
User's friend list

# User management
User's basic info
User's event list (rating / comment)


## Data Model
Event-[N-N:Relation]-User-[N:N]-User
Participation: eid, uid, comment, rating, host / participate
Friendship: uid, uid

# Event snapshot
# Event
{
	eid,
	Basic Info: { name:, desc:, rating:, host:, }
	Filter Info: { type:, time:, location:, }
	[
		{ Participant (ref), Rating, Comments}
	]
}

# User
{
	uid,

}



