from setuptools import setup,find_packages

setup(
    name='hazelpy',
    version='0.1',
    long_description=__doc__,
    packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[]
)
