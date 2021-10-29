from setuptools import setup, find_packages


def long_description():
    with open('README.md') as f:
        desc = f.read()
    return desc


setup(
    name='nay',
    version='0.0.1',
    description='nay generates boilerplate projects',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/TheIcyColdPenguin/nay',
    author='TheIcyColdPenguin',
    license='MIT',
    packages=find_packages(include=['nay']),
    entry_points={
        'console_scripts': [
            'nay = nay.__main__:main',
        ],
    },
    python_requires='>=3.6',
    install_requires=['setuptools'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    project_urls={
        'GitHub': 'https://github.com/TheIcyColdPenguin/nay',
    },
)
