from setuptools import setup, find_packages

setup(
    name='VZN',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'seaborn',
        'plotly'
    ],
    description='A module for data visualization.',
    author='Alan Fernandes',
    author_email='alanferns19@gmail.com',
    url='https://github.com/AlanFernandes8/Vizit',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)