import sqlite3
import random

create_table_sql = """
    CREATE TABLE tasklist (
    hash int NOT NULL,
    name text,
    description text,
    deadline text
    );
    """

insert_task_sql = """
    INSERT INTO 
    tasklist (
        name,
        hash,
        description,
        deadline
    )
    VALUES (? , ?, ?, ?);
    """

update_task_sql = """
    UPDATE 
        tasklist
    SET 
        name=coalesce(NULLIF(?,''),name),
        description=coalesce(NULLIF(?,''),description),
        deadline=coalesce(NULLIF(?,''),deadline)
    WHERE
        hash=?;
    """

remove_task_sql = """
    DELETE FROM
        tasklist
    WHERE
        hash=?;
    """

list_all_task_sql = """
    SELECT
        hash,
        name,
        description,
        deadline
    FROM
        tasklist;
    """

list_today_task_sql = """
    SELECT
        hash,
        name,
        description,
        deadline
    FROM
        tasklist
    WHERE
        DATE(deadline) like DATE('now');
    """

check_table_sql = """
    SELECT
        count(name)
    FROM
        sqlite_master
    WHERE
        type='table'
    AND
        name='tasklist';
"""


class SqliteDatabase(object):
    def __init__(self, path: str) -> None:
        self.path = path

    def __repr__(self) -> str:
        return f"SqliteDatabase({self.__dict__})"

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.task_list_initialize()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()

    def md(self, value: str) -> int:
        return abs(hash(value))

    def task_table_check(self) -> None:
        with self.connection as con:
            result = con.execute(check_table_sql)
            return result.fetchone()[0]

    def task_list_initialize(self) -> None:
        if self.task_table_check() == 0:
            try:
                with self.connection as con:
                    con.execute(create_table_sql)
            except sqlite3.DatabaseError as err:
                print(f"Table creation error has occured: {err}")

    def task_insert_new(self, name: str, description: str = "", deadline: str = ""):
        try:
            with self.connection as con:
                con.execute(
                    insert_task_sql,
                    (
                        name,
                        self.md(name + str(random.randrange(0, 9999))),
                        description,
                        str(deadline),
                    ),
                )
        except sqlite3.Error as err:
            print(f"Insert failed, error: {err}")

    def task_update_existing(
        self, hash: int, name: str = "", description: str = "", deadline: int = ""
    ):
        try:
            with self.connection as con:
                con.execute(update_task_sql, (name, description, str(deadline), hash))
        except sqlite3.Error as err:
            print(f"Update failed, error: {err} ")

    def task_remove_existing(self, hash: int):
        try:
            with self.connection as con:
                con.execute(remove_task_sql, (hash,))
        except sqlite3.Error as err:
            print(f"Remove failed, error: {err} ")

    def task_list_all(self):
        try:
            with self.connection as con:
                result = con.execute(list_all_task_sql)
        except sqlite3.Error as err:
            print(f"List all failed, error: {err} ")
        else:
            return tuple(row for row in result)

    def task_list_today(self):
        try:
            with self.connection as con:
                result = con.execute(list_today_task_sql)
        except sqlite3.Error as err:
            print(f"List today failed, error: {err} ")
        else:
            return tuple(row for row in result)
