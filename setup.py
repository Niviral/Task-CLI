from setuptools import setup, find_packages


def read_req():
    with open("requirements.txt") as req:
        content = req.read()
        requirements = content.split("\n")


setup(
    name="task",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_req(),
    entry_points="""
        [console_scripts]
        task=task.cli:cli
    """,
)
