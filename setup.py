import pathlib
from setuptools import setup, find_packages
from distutils.core import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='generate_gerrit_jenkins_project',
    url='https://github.com/tom-010/generate_gerrit_jenkins_project',
    version='0.0.1',
    author='Thomas Deniffel',
    author_email='tdeniffel@gmail.com',
    packages=['generate_gerrit_jenkins_project'], # find_packages(),
    license='Apache2',
    install_requires=[
        'python-jenkins'
    ],
    entry_points = {
        'console_scripts': ['generate_gerrit_jenkins_project = generate_gerrit_jenkins_project:main'] 
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    description='A tool to generate a project from a given template with a preconfigured Gerrit-project and Jenkins-pipelines.',
    long_description=README,
    long_description_content_type="text/markdown",
    python_requires='>=3',
    include_package_data=True,
)