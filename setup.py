from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="sigmoid_check",
    version="0.1.1",
    packages=find_packages(),
    description="A package for checking the implementation of tasks in Sigmoid Courses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="SigmoidAI - Balamatiuc Eduard",
    author_email="balamatiuc2@gmail.com",
    keywords=["tasks", "check", "sigmoid", "sigmoidai", "sigmoid_check"],
    license="Apache License 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
)