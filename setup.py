from setuptools import setup, find_packages
from typing import List

hyphen_E_Command = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function will return a list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if hyphen_E_Command in requirements:
            requirements.remove(hyphen_E_Command)
    return requirements
setup(
    name="GUARD",  # replace with your actual project name
    version="0.0.1",
    author="Sakthi Sharan",
    author_email="sakthisharanm@gmail.com",
    packages=find_packages(where="src"),  # assumes your code is under /src
    package_dir={"": "src"},
    install_requires=get_requirements("requirements.txt")
)