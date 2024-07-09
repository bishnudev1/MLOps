from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str = 'requirements.txt') -> List[str]:
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.read().splitlines()
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements




setup(
    name='student_score_prediction',
    version='0.0.1',
    author= "Bishnudev Khutia",
    author_email= "bishnudevkhutia20@gmail.com",
    packages=find_packages(),
    license='MIT',
    description='A package to predict student score based on study hours',
    install_requires= get_requirements()
)