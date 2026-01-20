from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ." # This is used to remove -e . from the requirements.txt file
# -e. is used for installing a package in "editable" mode.

# Function to get the list of requirements
def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="ml_project",
    version="0.0.1",
    author="Subhrajit Ghose",
    author_email="subhrajeetghose5@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)