# KanBan Console App
KanBan is a console application that is used to manage to-do tasks using the KanBan way of organizing todo into 3 sections: todo, doing, done. The app also tracks the time taken on a particular task and displays each task in the doing and done section with the time-taken so far on the task.

# Installation
First setup a virtual environment to install the application's dependencies:
```sh
$ pip install virtualenv
$ virtualenv environment
$ source environment_name/bin/activate
$ cd environment
```
To get started with KanBan Console, clone this repository: 
```sh
$ git clone https://github.com/skipcheru/bc-11-kanban_console.git
$ cd bc-11-kanban_console
$ pip install -r requirements.txt
```

# Getting Started
KanBan Console was developed using Python version `3.5.2` in mind and therefore may not work properly on Python version below 3. The console application interactive mode is accessed by running the following command:
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
A user can view the application commands using the `help` command during interactive mode:
```sh
(KanBan Console) help

Documented commands (type help <topic>):
========================================
doing  done  help  list  quit  todo

```
For example typing `todo -h` makes use of the help `-h` option command to get more insight to an application command:
```sh
(KanBan Console) todo -h
Create a todo task. For example todo email Kipngotie at 2pm
        Usage: todo <name>...
```

### `todo` command
To add a todo task , use the following command followed by task name:
```sh
(KanBan Console) todo install ubuntu on desktop pc

Task added!

 Task Id   Task Name                     Section    Start Time    Finish Time
---------  ----------------------------  ---------  ------------  -------------
   53      install ubuntu on desktop pc  todo

```

### `doing` command
Type `doing -h` to see how command must be typed:
```sh
(KanBan Console) doing -h
 Start doing a task. For example: doing 52
        Usage: doing <task_id>
```
To start doing a task or move a task to doing section, enter the command doing with task id:
```sh
(KanBan Console) doing 54

Great! You have started doing the Following Task

 Task Id   Task Name                Section    Start Time        Finish Time
---------  -----------------------  ---------  ----------------  -------------
   54      consult fellows on bugs  doing      2016-11-10 20:11

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
