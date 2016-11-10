# KanBan Console App
KanBan is a console application that is used to manage to-do tasks using the KanBan way of organizing todo into 3 sections: todo, doing, done. The app also tracks the time taken on a particular task and displays each task in the doing and done section with the time-taken so far on the task.
This application uses the [AfricasTalking SMS Gateway](https://africastalking.com/) to send one-way text messages to an intended recipient.


# Installation
First setup a virtual environment to install the application's dependencies:
```sh
$ pip install virtualenv
$ virtualenv environment_name
$ source environment_name/bin/activate
$ cd environment_name
```
To get started with KanBan Console, clone this repository: 
```sh
$ git clone https://github.com/skipcheru/bc-11-kanban_console.git
$ cd bc-11-kanban_console
$ pip install -r requirements.txt
```

# Getting Started
KanBan Console was developed using Python version `3.5.2` in mind and therefore may not work properly on Python version `2`. The console application interactive mode is accessed by running the following command:
```sh
(venv) C:\Users\Ngotie\kanban>python kanban.py -i
Welcome to KanBan Console Application! Add, organize and view your tasks
        The Commands For Any Action Are Listed Below
        Create A todo Task: todo task_name
        Start Doing Task: doing task_id
        Mark Task Done :  done task_id
        View Task You Are Doing :  list doing
        View Task You Have Finished :  list done
        View All Your Tasks :  list all
        To Exit : quit
(KanBan Console)
```

# Functionality
### `help` command
A user can find the built-in functionality of the application can be found using the `help` command during interactive mode:
```sh
(Contacts) help
Documented commands (type help <topic>):
========================================
add  help  quit  search  text  view
```
Typing `add -h` makes use of the help `-h` option command to get more insight to an application command:
```sh
(Contacts) add -h
Add a person to contacts list.
        Usage:
          add -n <person_name> <other_name> -p <phone_number>
```


### `add` command
To add a contact name and phone number combination, use the following command:
```sh
(Contacts) add -n gilbert gathara -p 0707012536
Added Contact: Gilbert Gathara, Phone number: +254707012536

(Contacts) add -n gilbert kariuki -p 0771374163
Added Contact: Gilbert Kariuki, Phone number: +254771374163
```


### `search` command
Type `search -h` to find the structure of the command:
```sh
(Contacts) search -h
Search a person in contacts list.
        Usage:
        	search <person_name>
```
To search a phone number or a contact name, you may enter the whole search term or part of the search term:
```sh
(Contacts) search gilbert
Found the following results: {254707012536: 'Gilbert Gathara', 254771374163: 'Gilbert Kariuki'}

(Contacts) search gat
Found the following results: {254707012536: 'Gilbert Gathara'}

(Contacts) search 74
Found the following results: {254771374163: 'Gilbert Kariuki'}
```


### `text` command
To get more insight into the command, type in the following:
```sh
(Contacts) text -h
Message a person in contacts list.
        Usage:
        	text <person_name> -m <message>
```
Sending a one-way text message to one of the contacts can be achieved using:
```sh
(Contacts) text gilbert -m 'Hey, wassup, Gilu'
Message sent! 
To: +254707079079 
Sms Charges: KES 1.0000
```
The same is also possible using an entire person's name or part of the name:
```sh
(Contacts) text gat -m 'Hey, wassup, Gilu'
Message sent! 
To: +254707012536 
Sms Charges: KES 1.0000
```


### `view` command
The view command allows a user to see all messages sent, either to a specific contact or every message sent. To do this, use the following command:
```sh
(Contacts) view
Displaying all sent messages:
 [{254707012536: {'Gilbert Gathara': "'Hey, wassup, Gilu' "}}]

(Contacts) view gil
Displaying sent messages to contacts matching 'gil':
 [{254707012536: {'Gilbert Gathara': "'Hey, wassup, Gilu' "}}]
```

### `quit` command
To loop out of the interactive shell and exit the console application, a user can use the `quit` command as so:
```sh
(Contacts) quit
Thank you for using Contacts Manager. Bye!
```
Since you are still in a virtual environment, you can deactivate the environment by typing:
```sh
$ deactivate
```


# To Do

  * Synchronize the Sqlite database to Firebase
  * View the contacts list
  * Edit a contact name/phone number
  * Delete a contact in contacts list
