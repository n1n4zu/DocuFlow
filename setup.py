from setuptools import setup, find_packages

setup(
    name='docuflow',
    version='1.0',
    packages=find_packages(),
    install_requires=['reportlab'],
     entry_points = {
         'console_scripts': [
             'docuflow = DocuFlow.docuflow:docuflow',
         ],
     },
    author='Kryspin Dziarek',
    license='MIT',
    description='Documentation generator for python projects',
    url='https://github.com/n1n4zu/DocuFlow'
)