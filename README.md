# KanBan Console App
KanBan is a console application that is used to manage to-do tasks using the KanBan way of organizing todo into 3 sections: todo, doing, done. The app also tracks the time taken on a particular task and displays each task in the doing and done section with the time-taken so far on the task.

# Installation
First setup a virtual environment to install the application's dependencies:
To get started with KanBan Console, clone this repository:
1. Go To KanBan Console GitHub Repository(https://github.com/skipcheru/bc-11-kanban_console) .
2. Clone the Repository.
3. Install the Requirements From the requirements.txt File.
4. Run The kanban.py file.
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

### `done` command
Type `doing -h` to see how command must be typed:
```sh
(KanBan Console) done -h
Finish a task. For example: done 52
        Usage: done <task_id>
```
To finish a task or move a task to done section, enter the command done with task id:
```sh
(KanBan Console) done 54

Great! You have finished the Following Task

 Task Id   Task Name                Section    Start Time        Finish Time
---------  -----------------------  ---------  ----------------  ---------------
   54      consult fellows on bugs  done       2016-11-10 20:11  2016-11-10 20:49
```

### `list` command
The list command allows a user to see all tasks currently doing, tasks completed and all the todo tasks. To do this, use the following command with either all, doing or done:
```sh

(KanBan Console) list doing

These Are The Tasks You are still doing with duration Taken

 Task Id   Task Name                  Section     Hours Taken    Minutes Taken
---------  -------------------------  ---------  -------------  ---------------
   52      test new table format      doing            3              8
   53      install ubuntu on desktop  doing            0              15

```
To view task in done section use `list done`. Example:
```
(KanBan Console) list done

These Are The Tasks You Have Completed With Time Taken

 Task Id   Task Name                Section     Hours Taken    Minutes Taken
---------  -----------------------  ---------  -------------  ---------------
   54      consult fellows on bugs  done             0              38
   
```
To view your to do list use `list all`. Example:

```
(KanBan Console) list all

These Are All Your todo Tasks in All The Sections.

 Task Id   Task Name                          Section    Start Time        Stop Time
---------  ---------------------------------  ---------  ----------------  ----------------
   52      test new table format              doing      2016-11-10 17:49
   53      install ubuntu on desktop          doing      2016-11-10 20:26
   54      consult fellows on bugs            done       2016-11-10 20:11  2016-11-10 20:49
   55      listen to sheepy mixes on youtube  todo

```

### `quit` command
To loop out of the interactive shell and exit the console application, a user can use the `quit` command as so:
```sh
(KanBan Console) quit
Bye Bye! See you soon!
```

# To Do

  * Synchronize the Sqlite database to Firebase

