'''
   This setup.py is an essential part of packagein and distribution of Python projects.
   It contains metadata about the project, such as its name, version, author, and dependencies. 
   The setup.py file is used by tools like setuptools to build and install the package, making it easier for others to use and contribute to the project.
 '''

from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    '''
    This function reads the requirements.txt file and returns a list of dependencies.
    
    '''
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
           #read the lines from the file
           lines=file.readlines()
           #process each lines
           for line in lines:
              requirement=line.strip()
              if requirement  and requirement!='-e .':
                 requirement_lst.append(requirement)
    except FileNotFoundError:
        print(f"Error: The file requirements.txt was not found.")
    return requirement_lst

print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Aditya Koranne",
    author_email="aditya.u.koranne@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)