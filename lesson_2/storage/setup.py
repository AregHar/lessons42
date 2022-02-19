from setuptools import find_packages, setup

setup(
    name="object-storage",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    version="0.1.0",
    python_requires=">=3.8",
    description="Object storage toolkit",
    install_requires=[
        'PyYAML~=6.0.0'
    ],
    author="Data42",
)
