from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    this function is return list of requirements 
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from thr file
            lines=file.readlines()
            #PRocess each line
            for line in lines:
                requirements=line.strip()
                ## ignore empty file and -e .
                if requirements and requirements!= '-e .':
                    requirement_lst.append(requirements)

    except FileNotFoundError:
        print("requirements.txt file no tfound") 

    return requirement_lst  



setup(
    name="NetWorkSecurity",
    version="0.0.1",
    author="Ashutosh",
    author_email="sahuashutosh1408@gmial.com",
    packages=find_packages(),
    install_requires=get_requirements()

)
