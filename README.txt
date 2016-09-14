To execute simple nose test

-nosetests

For verbosity

-nosetests --verbosity=3 

nosetest with coverage
nosetests --verbosity=3 -x . --with-coverage --with-xunit

May be required to issue command on ubuntu
- pip install coverage

generate nosetest xunit report
nosetests --verbosity=3 -x . --with-coverage --with-xunit

To generate human readable test report in html

on ubuntu sudo apt install xsltproc

-xsltproc nosetests.xslt nosetests.xml > tests.html


To execute specific tests

nosetests -a critical  --verbosity=3 -x . --with-coverage --with-xunit --cover-html 