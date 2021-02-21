Application for basic task managment using CLI.<br/>
<br/>
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
  
```
  
---  
### Feedback


+ \+ Error messages
+ \+ typing
+ \+ App works
+ \+ It's installable
+ \+ Using black
+ \+ Descriptive README
- \- Using click (I don't see this as negative hence Click was left as CLI framework)
- \- ~~Lack of success message when adding task~~ (Added in : #74bc90e)
- \- ~~Command "task list" returns empty table without any info, it's quite
    confusing that it's returning 
    something(empty table), not an error, but no tasks even after user added some.
    I think that some flag should be default when no params to command are given.~~ (Option `--all` set as default when no option specifed #74bc90e)
- \- ~~Some of the names are considered reserved, list is builtin function so 
  don't overwrite it~~ (No reserved names overwiten)
- \- ~~Importing using * is considered bad practice~~ (All imports changed to absolute #74bc90e)
- \- ~~Use only absolute imports~~ (All imports changed to absolute #74bc90e)
- \- ~~Avoid using one letter variable names~~ (No single letter variables #74bc90e)
- \- ~~It would be more elegant to not mix string formatting methods, I would suggest to use only f strings~~ (All formating performed with fstring #74bc90e)
- \- ~~It's better to use docstrings than comments above function and remember that comment need to contain 
    some additional information, don't add comments that are obvious therefore redundant~~ (Removed all redundant docstrings and comments #74bc90e)
- \- ~~You could reverse logic in db_check function so else won't be necessary~~ (db_check logic resolved on context manager level since #f7c7fb5)
- \- ~~Lack of .gitignore file~~ (.gitignore added #26b7b93)
- \- ~~Commits should have descriptive message which is not repeated~~ (descriptive commit message from #26b7b93 forward)
- \- ~~Lack of tests~~ (test for manager added #c68c825)

