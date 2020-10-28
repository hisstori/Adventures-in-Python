# Adventures-in-Python

Adventures in Python is an short adventure game where you must escape the forest. 
The user will be able to name their hero and fight several enemies including a boss at the end.
During the course of the adventure the user will either lose all health or prevail victorious.

![](https://i.imgur.com/QwPKzGS.png)

### Prerequisites

You will need the following technologies to finish installing and playing the game.
```
Python
Peewee
Pip
PostgreSQL
```

### Installing

You will need to clone this repository in to your local computer to create the project folder.
Once you have done this execute the following... 
```
cd Adventures-in-Python 
```
```
psql
```
```
\i lib/settings.sql
```

Next open your enviroment with the following and follow the remaining commands to build the database.
```
pipenv shell
```
```
python main.py
```
```
python seed.py
```

To run the game enter the following...
```
python game.py
```

## Built With

* [Python]() - The programming language used.
* [PeeWee]() - ORM used in conjunction with database.
* [PostgreSQL]() - Used to create store tables of data.


## Authors

* **Ryan Brown** - *Full Project* - [GitHub](https://github.com/Hisstori)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Zakk
* Zack
* Josh
