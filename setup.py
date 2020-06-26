from setuptools import setup, find_packages

setup(
    name="pytorch_neat",
    packages=find_packages(),
    install_requires=["neat-python", "numpy", "gym", "click", "torch"],
)
