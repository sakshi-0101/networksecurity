from setuptools import find_packages,setup
from typing import List



def get_requirements(file_path:str)->List[str]:

    '''this function will return the list of requirements'''
    
    
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt') as file:
            #read lines from the file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
            ##ignore empty lines and -e
                if requirement and requirement !="-e .":
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")
        
            
    return requirement_lst
print(get_requirements("requirements.txt"))
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Sakshi",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)