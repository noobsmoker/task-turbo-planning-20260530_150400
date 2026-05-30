from setuptools import setup, find_packages

setup(
    name="task-turbo-planning-20260530_150400",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'task=task:main',
        ],
    },
)
