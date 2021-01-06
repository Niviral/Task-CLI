import click
from .data_manager import *

db_check()


@click.group(invoke_without_command=True)
def cli() -> None:
    """Welcome to Task managment cli command"""


@cli.command(context_settings={"ignore_unknown_options": True})
@click.option(
    "--name",
    help="name of task",
    required=True,
)
@click.option("--description", help="description of task", required=False)
@click.option(
    "--deadline",
    help="task deadline",
    required=False,
    type=click.DateTime(["%d-%m-%Y", "%d-%m-%Y %H:%M"]),
)
def add(name: str, deadline: str = "", description: str = "") -> None:
    """Add new task."""
    task_insert(name, description, deadline)


@cli.command()
@click.option("--name", help="task name", required=False)
@click.option("--description", help="description of task", required=False)
@click.option(
    "--deadline",
    help="task deadline",
    required=False,
    type=click.DateTime(["%d-%m-%Y", "%d-%m-%Y %H:%M"]),
)
@click.argument("task_hash", type=str)
def update(task_hash, name: str, deadline: str = "", description: str = "") -> None:
    """Update a task"""
    task_update(task_hash, name, description, deadline)


@cli.command()
@click.argument("task_hash", type=str)
def remove(task_hash: str) -> None:
    """Remove a task"""
    task_remove(task_hash)
    click.echo("Task removed")


@cli.command()
@click.option("--all", "list_option", flag_value="ALL", help="List of all saved tasks.")
@click.option(
    "--today",
    "list_option",
    flag_value="TODAY",
    help="List of all task set with deadline for today.",
)
def list(list_option: str) -> str:
    """List of tasks"""

    def xstr(s):
        return "" if s is None else str(s)

    if list_option == "ALL":
        result = task_list_all()
        click.echo(
            "{:20s} {:20s} {:40s} {:20s}".format(
                "hash", "name", "description", "deadline"
            )
        )
        for row in result:
            hash, name, description, deadline = row[0], row[1], row[2], row[3]
            click.echo(
                f"{hash:20} {name:20s} {xstr(description):40s} {xstr(deadline):20s}"
            )
    else:
        result = task_list_today()
        click.echo(
            "{:20s} {:20s} {:40s} {:20s}".format(
                "hash", "name", "description", "deadline"
            )
        )
        for row in result:
            hash, name, description, deadline = row[0], row[1], row[2], row[3]
            click.echo(
                f"{hash:20} {name:20s} {xstr(description):40s} {xstr(deadline):20s}"
            )


if __name__ == "__main__":
    cli()
