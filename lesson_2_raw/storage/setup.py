from setuptools import setup,  find_packages

setup(
    name='object-storage',
    author='Data 42',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    version='0.1.0',
    description='Object storage',
)
