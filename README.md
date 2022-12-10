# LIBRARIFY

### Contents

- [Description](#Description)
- [Environment](#Environment)
- [Further Information](#Furtherinformation)
- [Requirements](#Requirements)
- [Repo Contents](#FileContents)
- [Installation](#Installation)
- [Usage](#Usage)
- [Technologies](#Technologies)

## Description :page_facing_up:
This project aims at making digital libraries more engaging, interactive and interesting by employing software engineering techniques to build a digital learning platform that helps users access learning materials easily, get book recommendations based on the user’s historical behavior  and also interact with other users.


## Environment :computer:
The console was developed in Ubuntu 14.04LTS using python3 (version 3.4.3).

### Further information :bookmark_tabs:
For further information on python version, and documentation visit [python.org](https://www.python.org/).

## Requirements :memo:
Knowledge in python3, how to use a command line interpreter, a computer with Ubuntu 14.04, python3.

## Repo Contents :clipboard:
This repository constains the following files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|[AUTHORS](./AUTHORS) | Contains info about authors of the project |
|[librarify_base.py](./models/librarify_base.py) | Defines LibrarifyBase class (parent class), and methods |
|[file_storage.py](./models/storage/file_storage.py) | Creates new instance of class, serializes and deserializes data |
|[librarify_console.py](./librarify_console.py) | creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object |


## Installation :hammer_and_wrench:
Clone the repository and run the console.py
```
$ git clone https://github.com/Sodiq179/LIBRARIFY.git
```

## Usage :wrench:

|   **Method**   |   **Description**   |
| -------------- | --------------------- |
|[create](./librarify_console.py) | Creates object of given class |
|[show](./librarify_console.py) | Prints the string representation of an instance based on the class name and id |
|[all](./librarify_console.py) | Prints all string representation of all instances based or not on the class name |
|[update](./librarify_console.py) | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
|[destroy](./librarify_console.py)| Deletes an instance based on the class name and id (save the change into the JSON file) |
|[count](./librarify_console.py)| Retrieve the number of instances of a class |
|[help](./librarify_console.py)| Prints information about specific command |
|[quit/ EOF](./librarify_console.py)| Exit the program |

###### Example

```
➜  LIBRARIFY git:(feature) ✗ ./librarify_console.py
(librarify) create LibrarifyBase
bb4f4b81-7757-460b-9263-743c9ea6fef6
(librarify) show LibrarifyBase bb4f4b81-7757-460b-9263-743c9ea6fef6
[LibrarifyBase] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2022, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'created_at': datetime.datetime(2022, 11, 13, 17, 7, 45, 492106)}
(librarify) all LibrarifyBase
["[LibrarifyBase] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2022, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'created_at': datetime.datetime(2022, 11, 13, 17, 7, 45, 492106)}"]
(librarify) update LibrarifyBase bb4f4b81-7757-460b-9263-743c9ea6fef6 name Sodiq
['LibrarifyBase', 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'name', 'Sodiq']
(librarify) all LibrarifyBase
["[LibrarifyBase] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2022, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'name': 'Sodiq', 'created_at': datetime.datetime(2022, 11, 13, 17, 7, 45, 492106)}"]
(librarify) destroy LibrarifyBase bb4f4b81-7757-460b-9263-743c9ea6fef6
(librarify) all LibrarifyBase
[]
(librarify) show LibrarifyBase
** instance id missing **
(librarify)

```

## Technologies :gear:
python3 (3.4.3)

### Acknowledgements :raised_hands:
To all the peers that contribuited with their knowledge

### Authors :fountain_pen:
* Sodiq Babawale
* Benedict Mwiti
