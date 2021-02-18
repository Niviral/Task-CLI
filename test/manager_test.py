import pytest
import os
from datetime import datetime, timedelta

from task import manager


@pytest.fixture
def setup_database():
    test_object = manager.SqliteDatabase("pytest.db")
    with test_object as db:
        db.task_insert_new(
            name="Today task",
            description="Test of description",
            deadline=datetime.today(),
        )
        db.task_insert_new(
            name="Tommorow Task", deadline=str(datetime.today() + timedelta(days=1))
        )
    yield test_object
    os.remove("pytest.db")


def test_md(setup_database):
    assert type(setup_database.md("test")) is int
    assert setup_database.md("test") > 0


def test_task_table_check(setup_database):
    with setup_database as db:
        assert db.task_table_check() == 1


def test_task_list_initialize(setup_database):
    with setup_database as db:
        db.connection.execute("DROP TABLE tasklist;")
        assert db.task_table_check() == 0
        db.task_list_initialize()
        assert db.task_table_check() == 1


def test_task_insert_new(setup_database):
    with setup_database as db:
        db.task_insert_new(name="Test task")
        assert db.connection.total_changes == 1


def test_task_update_existing(setup_database):
    with setup_database as db:
        before_update = db.task_list_all()[0]
        db.task_update_existing(hash=before_update[0], name="Updated Task")
        assert db.connection.total_changes == 1
        after_update = db.task_list_all()[0]
        assert before_update[0] == after_update[0]
        assert before_update[1] != after_update[1]
        assert before_update[2] == after_update[2]
        assert before_update[3] == after_update[3]


def test_task_remove_existing(setup_database):
    with setup_database as db:
        to_remove = db.task_list_all()
        db.task_remove_existing(to_remove[0][0])
        assert db.connection.total_changes == 1
        assert len(db.task_list_all()) == 1


def test_task_list_all(setup_database):
    with setup_database as db:
        assert len(db.task_list_all()) == 2


def test_task_list_today(setup_database):
    with setup_database as db:
        assert len(db.task_list_today()) == 1
