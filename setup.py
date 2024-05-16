from setuptools import setup, find_packages

def read_version():
    with open("src/__init__.py") as f:
        for line in f:
            if line.startswith('__version__'):
                return line.strip().split('=')[1].strip().strip('"').strip("'")
            
setup(
    name='ai_nutrition_analyzer',
    version=read_version(),
    packages=find_packages(),
    install_requires=[
    ],
)