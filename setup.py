from setuptools import setup,find_packages
from typing import List


## Declaring variable for setup funtion
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.2"
AUTHOR = "Neha Vishwakarma" 
DESCRIPTION = "This is My Full end to end project."
## It will find where is __init__function and add them as a package
PACKAGES = find_packages()   # ['housing']
REQUIREMENT_FILE_NAME ="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description : This fuction is going to return list of requirement
    mention in requirements.txt file

    return :Thios fuction is going to return the list of name of libraries 
    mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
    name= PROJECT_NAME,
    version=VERSION,
    author= AUTHOR,
    description= DESCRIPTION,
    packages=PACKAGES,
    install_requires = get_requirements_list()
)
## housing is package and __init__ is module