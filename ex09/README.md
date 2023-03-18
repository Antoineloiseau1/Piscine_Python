# ft_package

First build package:
$> python3 -m build

if anything goes wrong try:

$> python3 -m pip install --upgrade pip

or

$> python3 -m pip install --upgrade build


Then install using pip:

$> pip install ./dist/ft_package-0.0.1.tar.gz

or

$> pip install ./dist/ft_package-0.0.1-py3-none-any.whl

Verify using "pip list" if the package is installed

To see informations:
$> pip show -v ft_package 

run tester.py script to enjoy this beautiful package
