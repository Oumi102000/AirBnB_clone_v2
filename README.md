# AirBnB clone - The console
AirBnB clone project is a creation of a full web application that simulate the well known __AirBnB__ application.

## Description
This initial version of the AirBnB-clone app simply implements the back-end console that allows you to create, show, update and delete items.

## command line interpreter (Console)
Console is a commande line interpreter, also known as "command-line interface" (CLI). It allows users to execute precise commands:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object.

### How to start it
In order to gain access to our console, you must first clone the following repository:

`https://github.com/hajarzaitouni/AirBnB_clone.git`

### How to use it
After cloning the repository, you will have access to all of our console's features.

The AirBnB interpreter command (console) can be run either in interactive or non-interactive mode;

* The shell work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) help quit
quit command to exit the HBNB console
(hbnb) 
(hbnb) quit
$
```

* In the non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$
```

### console commands
As stated above, using our __AirBnB console__  you will have access to the following commands:

* __create__
	* `Usage: create <class_name>`
	* Example:
	```
	$ ./console.py
	(hbnb) create
	** class name missing **
	(hbnb) create BaseModel
	39e416ad-bb6e-4638-a326-428380805934
	(hbnb) 
	```

* __show__
	* `usage: show <class_name> <id>`
	* Example:
	```
	$ ./console.py 
	(hbnb) show BaseModel 39e416ad-bb6e-4638-a326-428380805934
	(hbnb) [BaseModel] (39e416ad-bb6e-4638-a326-428380805934) {'id': '39e416ad-bb6e-4638-a326-428380805934', 'created_at': datetime.datetime(2023, 9, 17, 16, 52, 53, 779675), 'updated_at': datetime.datetime(2023, 9, 17, 16, 52, 53, 779675)} 
	```

* __all__
	* `usage: all or all <class_name> or <class_name>.all()`
	* Example:
	```
	$ ./console.py
	(hbnb) create User
	be6de9db-f5e0-4224-accd-5b5e3013f916
	(hbnb) all
	["[BaseModel] (39e416ad-bb6e-4638-a326-428380805934) {'id': '39e416ad-bb6e-4638-a326-428380805934', 'created_at': datetime.datetime(2023, 9, 17, 16, 52, 53, 779675), 'updated_at': datetime.datetime(2023, 9, 17, 16, 52, 53, 779675)}", "[User] (be6de9db-f5e0-4224-accd-5b5e3013f916) {'id': 'be6de9db-f5e0-4224-accd-5b5e3013f916', 'created_at': datetime.datetime(2023, 9, 17, 17, 3, 48, 849389), 'updated_at': datetime.datetime(2023, 9, 17, 17, 3, 48, 849389)}"]
	(hbnb) all BaseModel
	["[BaseModel] (39e416ad-bb6e-4638-a326-428380805934) {'id': '39e416ad-bb6e-4638-a326-428380805934', 'created_at': datetime.datetime(2023, 9, 17, 16, 52, 53, 779675), 'updated_at': datetime.datetime(2023, 9, 17, 16, 52, 53, 779675)}"]
	(hbnb) User.all()
	["[User] (be6de9db-f5e0-4224-accd-5b5e3013f916) {'id': 'be6de9db-f5e0-4224-accd-5b5e3013f916', 'created_at': datetime.datetime(2023, 9, 17, 17, 3, 48, 849389), 'updated_at': datetime.datetime(2023, 9, 17, 17, 3, 48, 849389)}"]
	(hbnb) 
	```

* __update__
	* `usage: update <class_name> <id> <attribute_name> <value_name>`
	* Example:
	```
	$ ./console.py
	(hbnb) update User 1da69305-67b4-477f-b5ce-352927323dfd first_name "Betty"
	(hbnb) show User 1da69305-67b4-477f-b5ce-352927323dfd
	[User] (1da69305-67b4-477f-b5ce-352927323dfd) {'id': '1da69305-67b4-477f-b5ce-352927323dfd', 'created_at': datetime.datetime(2023, 9, 17, 17, 8, 7, 89532), 'updated_at': datetime.datetime(2023, 9, 17, 17, 14, 13, 529231), 'first_name': 'Betty'}
	(hbnb) 
	```

* __count__
	* `usage: count <class_name> or <class_name>.count()`
	* Example:
	```
	$ ./console.py
	(hbnb) count User
	1
	(hbnb) create User
	1da69305-67b4-477f-b5ce-352927323dfd
	(hbnb) count User
	2
	(hbnb) 
	```

* __destroy__
	* `usage: destroy <class_name> <id>`
	* Example:
	```
	$ cat file.json ; echo ""
	$ {"BaseModel.39e416ad-bb6e-4638-a326-428380805934": {"id": "39e416ad-bb6e-4638-a326-428380805934", "created_at": "2023-09-17T16:52:53.779675", "updated_at": "2023-09-17T16:52:53.779675", "__class__": "BaseModel"}, "User.be6de9db-f5e0-4224-accd-5b5e3013f916": {"id": "be6de9db-f5e0-4224-accd-5b5e3013f916", "created_at": "2023-09-17T17:03:48.849389", "updated_at": "2023-09-17T17:03:48.849389", "__class__": "User"}, "User.1da69305-67b4-477f-b5ce-352927323dfd": {"id": "1da69305-67b4-477f-b5ce-352927323dfd", "created_at": "2023-09-17T17:08:07.089532", "updated_at": "2023-09-17T17:14:13.529231", "first_name": "Betty", "__class__": "User"}} 
	$ ./console.py
	(hbnb) destroy User 1da69305-67b4-477f-b5ce-352927323dfd
	(hbnb) 
	$ cat file.json ; echo ""
	$ {"BaseModel.39e416ad-bb6e-4638-a326-428380805934": {"id": "39e416ad-bb6e-4638-a326-428380805934", "created_at": "2023-09-17T16:52:53.779675", "updated_at": "2023-09-17T16:52:53.779675", "__class__": "BaseModel"}, "User.be6de9db-f5e0-4224-accd-5b5e3013f916": {"id": "be6de9db-f5e0-4224-accd-5b5e3013f916", "created_at": "2023-09-17T17:03:48.849389", "updated_at": "2023-09-17T17:03:48.849389", "__class__": "User"}}
	$ ./console.py
	(hbnb) User.destroy("be6de9db-f5e0-4224-accd-5b5e3013f916")
	(hbnb) destroy BaseModel 39e416ad-bb6e-4638-a326-428380805934
	(hbnb) 
	$ cat file.json ; echo ""
	$ {}
	```
