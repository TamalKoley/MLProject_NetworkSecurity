from setuptools import find_packages,setup;
from typing import List;

HYPEN_E_DOT='-e .'
def get_requirements(filename:str)->List[str]:
    """
        This function will retrun all the packages written in requirement file
    """
    try:
        requirement_arr=[];
        with open(filename,'r') as req_file:
            req=req_file.readlines()
        for lines in req:
            line=lines.strip()
            requirement_arr.append(line.replace('\n',''))
        if HYPEN_E_DOT in requirement_arr:
            requirement_arr.remove(HYPEN_E_DOT)
        return requirement_arr;
    except Exception as e:
        print(f'Error occured in setup : {e}')

    

setup(
    name='Network Security Project',
    version='1.0.0',
    author='Tamal Koley',
    author_email='tamalkoley121@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)