from setuptools import setup, find_packages

setup(
    name="dab_project",
    version="0.1.0",
    description="This contains the code in the ./sec directory of the project",
    author="Ankur Chaudhary",
    packages=find_packages(where="./src"),
    package_dir={"": "./src"},
    install_requires=["setuptools"],
)
