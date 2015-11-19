# Christmas List Crowdsource - Backend

## Description
The overall project is basically a wish list generator.  
* A user can create a list
* The list owner can then share a link with friends and family
* Visitors will be able to pledge to buy an item or pledge to pay for part of it
* Once an item is fully pledged it becomes reserved 
* The owner will never see what is reserved and what is not (we want it to be a surprise)
* When a person pledges they will be prompted for a credit card which will be processed through stripe
* When a list deadline passes the list is set to inactive and all partially funded items are refunded (otherwise it is embezzlement)


As the backend your job in the group is to provide the front end with api endpoints they need.  On a simple level this should include the basic 5 verbs but will need to include other api end points as the need arises.  Your job will also be try try to keep your api clean and Restful.

## Details

### Normal Mode

#### Overview
* Create an API that is published on the internet
* API should have authentication
* Will be the source of all models for the group project
* Can take stripe tokens and handle them for charges
* Will run background jobs to keep the system clean and up to date

#### API
* Use token Authentication
* Use the endpoint from class that allows the api to be passed a username and password and return a token
* Make sure to lock down permissions on all dangerous endpoints so that only the owner can monkey with them
* Must install CORS to allow remote requests
* All views should have tests
* Integrate with Travis-CI

#### Money
* Use stripe with your group.  The front end should provide a token from stripe.
* Use the token to charge the card immediately
* If the item has been fully pledged then make sure the item is reserved
* See below for refunding partially pledged items

#### Background Tasks
* These should be django commands
* The list needs a deadline on it
* You should schedule a task that checks for active lists where the deadline has passed
	* [Heroku Scheduler](https://elements.heroku.com/addons/scheduler)
* The list should be made inactive
* Any partially paid for items need to have their pledge amounts refunded
* The refunded pledges should indicate they were refunded

#### Suggestions
* Get the api published as fast as possible
* Include token auth with the initial push but you can wait on permissions
* Use the admin to add data so the front end engineers can work

### Hard Mode

* For any links that are amazon based pull out the unique id from the URL and store it in the model
	* Hint: Regex would be good
	* Hint: It is the alpha numeric string after bp/
* Using the unique id and the amazon product api get the price and quantity of the product available. 
	* [Affiliate Program](https://affiliate-program.amazon.com)
	* [Product API](https://affiliate-program.amazon.com/gp/advertising/api/detail/main.html)
	* [Python Library](https://python-amazon-product-api.readthedocs.org/en/latest/index.html)
* Schedule a Background task to run and update the price and quantity of any active, non-reserved items
	* [Heroku Scheduler](https://elements.heroku.com/addons/scheduler)
