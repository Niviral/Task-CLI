Application for basic task managment using CLI.<br/>
,br/>
[![code style: black](https://img.shields.io/static/v1?label=code%20style&message=black&color=black&style=flat-square)](https://github.com/psf/black)&nbsp;


Setup
---

```
# Clone repository
git clone https://github.com/Niviral/Task-CLI.git
# Create VENV
python3 -m venv <location>
# Activate VENV
source <location>/bin/activate
# Move to folder containing setup.py
cd <path>
# Install CLI application
python3 -m pip install .
```

Storage
---

Task application as every CRUD application has been created with persistent storage under the hood in this case SQLite.<br/>
You can specify location of your SQLite file using enviroment variable `ENV_DB_LOC` containg path and filename<br/>
```
export ENV_DB_LOC='/home/DB.sqlite3'
```
If not defautl DB will be creted inside application `/task` folder.


Usage
---
```
task [OPTIONS] COMMAND

Commands:
  add       Add new task
  list      List of tasks
  remove    Remove a task
  update    Update a task
```

### ADD


```
task add [OPTIONS]


Options:
  --name TEXT                             name of task  [required]
  --description TEXT                      description of task
  --deadline [%d-%m-%Y|%d-%m-%Y %H:%M]    task deadline
  --help                                  Show this message and exit.
```

### List

```
Usage: task list [OPTIONS]

Options:
  --all                                   List of all saved tasks.
  --today                                 List of all task set with deadline for today.
  --help                                  Show this message and exit.
  ```
Example output:
```
hash                 name    description              deadline
2361641662108793839  task    this is description      2021-01-06 23:59:00
```
### Update

```
Usage: task update [OPTIONS] TASK_HASH

Options:
  --name TEXT                             task name
  --description TEXT                      description of task
  --deadline [%d-%m-%Y|%d-%m-%Y %H:%M]    task deadline
  --help                                  Show this message and exit.
```

### Remove

```
Usage: task remove [OPTIONS] TASK_HASH

Options:
  --help                                  Show this message and exit.
