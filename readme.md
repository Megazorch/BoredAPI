# Technical Challenge for Juniors
## Bored API Wrapper - by Ivakhiv Roman
### Running app via docker compose

*Supposed that Docker is already installed on your machine.*

1. Clone this repository to your local machine:
```shell
$ git clone https://github.com/Megazorch/BoredAPI.git
```
2. Create an `.env` file inside main directory and filled it as `.env.example`:
```env
DB_NAME=your_database_name
DB_USER=user_name
DB_PASS=password_to_your_database
DB_HOST=db (if running via docker-compose) | localhost (if running locally)
DB_PORT=5432
DB_NAME_TEST=name_of_database_for_tests
```
3. Choose `DB_HOST=db` in your `.env`:
4. To get a new **random** activity from Bored API just run:
```shell
$ docker compose run --rm bored_api new
```
5. Or add some options:
```shell
$ docker compose run --rm bored_api new --type music --price 0.0
```
6. To see more options just use `--help`:
```shell
$ docker compose run --rm bored_api new --help
```
7. If you wish to get the list of last five activities then run:
```shell
$ docker compose run --rm bored_api list
```
### Running app locally

*Supposed that Python is already installed on your machine.*

1. Clone this repository to your local machine:
```shell
$ git clone https://github.com/Megazorch/BoredAPI.git
```
2. Install dependencies:
```shell
$ pip install --no-cache-dir -r requirements.txt
```
Or if you are using `pipenv` run:
```shell
$ pipenv install
```
3. Create an `.env` file inside main directory and filled it as `.env.example`:
```env
DB_NAME=your_database_name
DB_USER=user_name
DB_PASS=password_to_your_database
DB_HOST=db (if running via docker-compose) | localhost (if running locally)
DB_PORT=5432
DB_NAME_TEST=name_of_database_for_tests
```
4. Choose `DB_HOST=localhost` in your `.env` and run command:
```shell
$ python main.py --help
```
5. You'll see that there are three actions you can perform:
- new
- list
- create_table

All three actions has `--help` option.

6. To get a new **random** activity from Bored API just run:
```shell
$ python main.py new
```
7. If you wish to narrow down your result than add options to your call:
```shell
$ python main.py new --type education --participants 1 --price_min 0.1 --price_max 1 --accessibility_min 0.1 --accessibility_max 0.5
```
8. To get the list of last five activities that you've already got from Bored API then run:
```shell
$ python main.py list
```

## For your information
Command `create_table` is used only for initialization of table call `activities`.

---
## Technical Challenge for Juniors
For this challenge, you are going to use the API of [bored API](https://www.boredapi.com/). This API gives us a random activity to do every time you call it, for example, if you make the following call:

```
GET https://www.boredapi.com/api/activity
```
You will get a response like this:

```json
{
    "activity": "Learn Express.js",
    "type": "education",
    "participants": 1,
    "price": 0.1,
    "link": "https://expressjs.com/",
    "key": "3943509",
    "accessibility": 0.1
}
```
For more details, check the [documentation](https://www.boredapi.com/documentation).

 We will use this API to create a simple program that will give us a random activity to do.

## Instructions
Clone this repository and create a new one on your own GitHub account. When you are done, please send us the link to your repository.

## Tasks

### API Calls
1. Create an API wrapper for bored API, This wrapper should have a method that returns a random activity, and should accept parameters to filter the activities by type, number of participants, price range, and accessibility range.

### Database
2. Write a class that will save the activities in a database, this class should have a method that will accept the activity as a parameter

3. Add another method that will return the latest activities saved in the database. The database can be any database you want (e.g. SQLite), but it should be a relational database.

### Command line program
3. Create a simple command line program that will use the API wrapper and the database class to get a random activity and save it in the database. The program should accept parameters to filter the activities by type, number of participants, price range, and accessibility range. The command should look like this:
    
    ```bash
    my_program new --type education --participants 1 --price_min 0.1 --price_max 30 --accessibility_min 0.1 --accessibility_max 0.5
    ```
This command should get a random activity with the type education, 1 participant, a price of 0.1, and an accessibility of 0.1 and save it in the database.


4. Add another command to the program that will return the last activities saved in the database. The command should look like this:
    
    ```bash
    my_program list
    ```
This command should return the last 5 activities saved in the database.


## Extra points
 - Make sure that you include a dependencies file (requirements.txt, gemfile, package.json, etc.). But don't include any virtual environment or packages installed in your repository.
 - Add unit tests for your work.

