from setuptools import setup, find_packages

setup(
    name='AssistantBot.py',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'assistant_bot = AssistantBot:main',
        ],
    },
)
