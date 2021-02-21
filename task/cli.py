import click
from task import manager

task_db = manager.SqliteDatabase(path="task.db")


@click.group()
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
def add(
    name: str,
    description: str = "",
    deadline: str = "",
) -> None:
    with task_db as db:
        db.task_insert_new(name, description, deadline)
    click.echo("Task successfully added")


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
def update(task_hash, name: str, description: str = "", deadline: str = "") -> None:
    with task_db as db:
        db.task_update_existing(task_hash, name, description, deadline)
    click.echo("Task successfully updated")


@cli.command()
@click.argument("task_hash", type=str)
def remove(task_hash: str) -> None:
    with task_db as db:
        db.task_remove_existing(task_hash)
    click.echo("Task removed")


@cli.command()
@click.option(
    "--all",
    "list_option",
    flag_value="ALL",
    default=True,
    help="List of all saved tasks.",
)
@click.option(
    "--today",
    "list_option",
    flag_value="TODAY",
    help="List of tasks with deadline for today.",
)
def list(list_option: str) -> str:
    if list_option == "ALL":
        with task_db as db:
            result = db.task_list_all()
        if not result:
            click.echo(
                "Your list is empty! Great Job! Remember that you can always add new tasks."
            )
        else:
            click.echo(f"{'Hash':20} {'Name':20s} {'Description':40s} {'Deadline':20s}")
            for row in result:
                hash, name, description, deadline = row[0], row[1], row[2], row[3]
                click.echo(
                    f"{hash:20} {name:20s} {task_db.nonestr(description):40s} {task_db.nonestr(deadline):20s}"
                )
    else:
        with task_db as db:
            result = db.task_list_today()
        if not result:
            click.echo(
                "Your list is empty! Great Job! Remember that you can always add new tasks."
            )
        else:
            click.echo(f"{'Hash':20} {'Name':20s} {'Description':40s} {'Deadline':20s}")
            for row in result:
                hash, name, description, deadline = row[0], row[1], row[2], row[3]
                click.echo(
                    f"{hash:20} {name:20s} {task_db.nonestr(description):40s} {task_db.nonestr(deadline):20s}"
                )


if __name__ == "__main__":
    cli()
