from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function returns a list of requirements 
    '''
    requirements=[]
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements


setup(
name='volcanic rock classifier',
version='1.0',
author='Bimo Anggoro',
author_email='bimoanggorop@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)