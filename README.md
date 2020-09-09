# where2apply-api
Backend API for where2apply

## Setting Up
To set up the API on your local machine, clone the repo and run the following commands: 

```
pip3 install -r requirements.txt
gunicorn server:app
```

## Usage
### Base URL
This api is deployed to Heroku and running on a free dyno. Use the following base URL to access the API:

```
https://where2apply-api.herokuapp.com
```

### API Endpoints
|Endpoint|Method|Request|Response|
|--------|------|-------|--------|
| `/` |`GET`|-|Initial Route that returns a welcome API string|
| `/api/v1/colleges/list`|`POST`|JSON Object containing the following K-V Pairs:<br><br> • **class_size**: `Number` - Preferred College Class Size <br> • **ur_pref**: `Number` - Urban-Rural Preference <br> • **sat_vr**: `Number` - SAT English Score <br> • **sat_mt**: `Number` - SAT Math Score <br> • **gpa**: `Number` - Highschool GPA <br> • **region_dic**: `Object` - Region Preferences <br> |Balanced Array/List of Colleges that best fit user's profile|

#### Example

The following POST Request:

```
curl --request POST \
  --url https://where2apply-api.herokuapp.com/api/v1/colleges/list \
  --header 'content-type: application/json' \
  --data '{
	"class_size": 1000,
	"ur_pref": 3,
	"sat_vr": 750,
	"sat_mt": 400,
	"gpa": 2.5,
	"region_dic": {
		"Far West": "Preferred",
		"New England": "Neutral",
		"Mid East": "Not_Preferred",
		"Southeast": "Neutral",
		"Plains": "Preferred",
		"Great Lakes": "Neutral",
		"Southwest": "Not_Preferred",
		"Rocky Mountains": "Neutral"
	}
}'
```

gets the following response data:

```
[
  "Oberlin College",
  "Dickinson College",
  "Lewis & Clark College",
  "Rollins College",
  "California Institute Of The Arts",
  "Hampshire College",
  "Nazareth College",
  "University Of Hartford",
  "Norwich University",
  "Roger Williams University",
  "Berklee College Of Music",
  "Endicott College",
  "Keuka College",
  "Johnson & Wales University-Providence",
  "Columbia College Chicago"
]
```

## Version Control
To make any changes to the API or script, submit a PR. After code review, it'll be merged to `master`. The `master` branch is linked to the Heroku Dashboard so any new deploys on Github automatically trigger a reploy on Heroku. 
