from setuptools import setup
from typing import List


## Declaring variable for setup funtion
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Neha Vishwakarma" 
DESCRIPTION = "This is My Full end to end project."
PACKAGES =["housing"]
REQUIREMENT_FILE_NAME ="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description : This fuction is going to return list of requirement
    mention in requirements.txt file

    return :Thios fuction is going to return the list of name of libraries 
    mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
    name= PROJECT_NAME,
    version=VERSION,
    author= AUTHOR,
    description= DESCRIPTION,
    packages=PACKAGES,
    install_requires = get_requirements_list()
)
"""
if __name__ =="__main__":
    print(get_requirements_list())
"""