from setuptools import setup, find_packages

with open('README.MD', "r", encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"
AUTHOR_NAME = 'Himanshu'
AUTHOR_USER_NAME = 'Himanshu0208'
AUTHOR_EMAIL = 'himanshupandey1036@gmail.com'
REPO = 'PlantCare'
SRC_REPO = 'plant_care'

setup(
    name=SRC_REPO,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small project for checking the disease of a some plant",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO}",
    package_dir={"":"src"},
    packages=find_packages(where='src')
)
