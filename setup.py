from setuptools import find_packages,setup
from typing import List

def get_requirements()->List:
    """
    Retrieve the list of requirements.
    Returns:
        List[str]: A list of strings representing the requirements.
    """
    
    requirement_list:List[str] = []
    
    return requirement_list

setup(name='BigMartSales',
      version='0.0.1',
      author='Swinal',
      author_email='swinalwaghmare2802@gmail.com',
      packages=find_packages(),
      install_requires = get_requirements()
)
