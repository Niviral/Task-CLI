import sqlite3
import os

DB_LOCATION = os.path.dirname(os.path.abspath(__file__)) + "/task_list.sqlite3"


def md(val: str) -> int:
    res = hash(val)
    return abs(res)


# DB connector
def db_connect():
    con = sqlite3.connect(os.getenv("ENV_DB_LOC", DB_LOCATION))
    return con


# Table creation.
def dbinit():
    con = db_connect()
    cur = con.cursor()
    tasklist_sql = """
    CREATE TABLE tasklist (
        hash int NOT NULL,
        name text,
        description text,
        deadline text
        )
    """
    cur.execute(tasklist_sql)
    con.close()


# Check if table exist
def db_check():
    if os.path.exists(os.getenv("ENV_DB_LOC", DB_LOCATION)) == True:
        print("DB existing, skipping creation")
    else:
        dbinit()
        print("table created")


def task_insert(name: str, description: str = "", deadline: int = ""):
    con = db_connect()
    cur = con.cursor()
    hash = md(name)
    insert_task_sql = """
    INSERT INTO 
        tasklist(
            name,
            hash,
            description,
            deadline
        )
        VALUES (? , ?, ?, ?)
    """
    try:
        cur.execute(insert_task_sql, (name, hash, description, deadline))
        con.commit()
        con.close()
    except:
        con.rollback()
        raise RuntimeError("Failed, rolling back")


def task_update(hash: int, name: str, description: str = "", deadline: int = ""):
    con = db_connect()
    cur = con.cursor()
    update_task_sql = """
    UPDATE 
        tasklist
    SET 
        name=coalesce(?,name),
        description=coalesce(?,description),
        deadline=coalesce(?,deadline)
    WHERE
        hash=?
    """
    try:
        cur.execute(update_task_sql, (name, description, deadline, hash))
        con.commit()
        con.close()
    except:
        con.rollback()
        raise RuntimeError("Failed, rolling back")


def task_remove(hash: int) -> None:
    con = db_connect()
    cur = con.cursor()
    remove_task_sql = """
    DELETE FROM
        tasklist
    WHERE
        hash=?
    """
    cur.execute(remove_task_sql, (hash,))
    con.commit()
    con.close()


def task_list_all():
    con = db_connect()
    cur = con.cursor()
    list_task_sql = """
    SELECT
        hash,
        name,
        description,
        deadline
    FROM
        tasklist
    """
    cur.execute(list_task_sql)
    result = cur.fetchall()
    return result


def task_list_today():
    con = db_connect()
    cur = con.cursor()
    list_task_sql = """
    SELECT
        hash,
        name,
        description,
        deadline
    FROM
        tasklist
    WHERE
        deadline LIKE date('now')||' %'
    """
    cur.execute(list_task_sql)
    result = cur.fetchall()
    return result
