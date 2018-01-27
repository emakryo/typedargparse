from setuptools import setup, find_packages

setup(
    name="typedargparse",
    version="0.0.0",
    description="Simple argparse wrapper with typing",
    # packages=find_packages(exclude=['tests']),
    py_modules=["typedargparse"],
    python_requires='>=3.5'
)
