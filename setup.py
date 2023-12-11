from setuptools import find_packages,setup
from typing import List

e_dot = '-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    this function takes requirements in form of list
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if e_dot in requirements:
            requirements.remove(e_dot)

    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Rashmith',
    author_email = 'rashdata007@gmai.com',
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")



)