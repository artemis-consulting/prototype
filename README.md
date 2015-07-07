Project Overview
================
Artemis Consulting kicked off our agile project named "FDA Drug Monitor" by assembling the project team and discussing the 18F opportunity/problem statement. 
To read more about the Problem and Vision Statements, go to [the supporting document](https://github.com/artemis-consulting/prototype/blob/master/SUPPORTING_DOC.md#section-pool2-vision).
To read more about the Project Scope and Key Features, go to [the supporting document](https://github.com/artemis-consulting/prototype/blob/master/SUPPORTING_DOC.md#section-pool2-overview).

Team and Stakeholders
=====================
* Project leader (Product Owner) – Rohit G.
* Scrum master – Jim T.
* Backend developer – Risa O.
* Front end – Stephanie S.
* UX – Hoa P.
* Web design – David N.
* DevOps – Jay M.

The team decided on nominating Rohit as the project leader based on his qualifications and the technical product manager (TPM) role he performs on the Congress.gov contract. Under normal circumstances, 18F would be considered key stakeholders. However, due to the nature of this RFP, Artemis management is fulfilling this function with Rohit performing the role of ‘Product Owner’. 

His responsibilities include:

* Ensuring the service will meet the needs of its prospective users
* Ensuring that key features are built
* Managing the features and defect backlogs on a daily basis
* Setting priorities and providing the definition of "done" 
[Pool 2, requirement A, B and Play 6 ]

The team members assembled for this project are experts in their respective disciplines. [Pool 2, requirement A and Play 7 ]

User-Centered Design 
====================
During the story planning meetings, the following prospective users where identified:
* Public users
* Doctors 
* Pharmacists 
* Attorneys 
* FDA SMEs/employees 
* Federal regulators and watchdog agencies
* State regulators

To read the full UCD approach, techniques, and results, go to [the supporting document](https://github.com/artemis-consulting/prototype/blob/master/SUPPORTING_DOC.md#section-pool2-ucd)

The team strongly felt that applying the UCD techniques in the sections previously mentioned satisfy Play [1] and [2].

Mobile-first Responsive Design
------------------------------
Our HTML experts created multiple functioning web prototypes throughout the course of the development phase. These were used for Accessibility testing and usability testing. 

Formal Accessibility Review
---------------------------
Our team conducted a fairly formal accessibility review with the initial web prototype. The results of this review are [here](https://github.com/artemis-consulting/prototype/blob/master/doc/testing/FDA%20Drug%20Monitor%20Formal%20Accessibility%20Review.pdf).

Usability Testing
-----------------
Agile usability testing was integrated into the design and prototyping process so that the team could identify and fix user experience problems before they become baked in and expensive to address. To read the full UX testing approach, techniques, and results, go to [the supporting document](https://github.com/artemis-consulting/prototype/blob/master/SUPPORTING_DOC.md#section-pool2-ux-testing)

Agile Delivery Approach
=======================
For the FDA prototype, we decided on 2-day sprints but chose to add a 4-day sprint to accommodate the unusual nature of this project and weekend work after the project deadline was extended.

To view our entire agile section and artifacts related to Play 4, click [here](https://github.com/artemis-consulting/prototype/blob/master/SUPPORTING_DOC.md#section-pool2-agile).
Results of usability testing can be viewed [here](https://github.com/artemis-consulting/prototype/blob/master/SUPPORTING_DOC.md#section-pool2-ucd). 
For automated testing, we used the open source Selenium tool. The scripts for these tests are checked in [here](https://github.com/artemis-consulting/prototype/blob/master/code/core/tests/test_behavior.py).

Scrum Ceremonies & Roadmap
==========================
To view Scrum ceremonies, product roadmap, and release strategy for our FDA project, click [here](https://github.com/artemis-consulting/prototype/blob/master/SUPPORTING_DOC.md#section-pool2-scrum)

Tools and Technology Stack
==========================
Click [here to see the details of the tools and full technology stack](https://github.com/artemis-consulting/prototype/blob/master/SUPPORTING_DOC.md#section-pool2-tools) used by the team for the FDA prototype.

Hosting environment
===================
During Sprint 0, the team worked on deploying the hosting environment for both test and production.  
Click [here](https://github.com/artemis-consulting/prototype/blob/master/SUPPORTING_DOC.md#section-pool2-hosting) to read more about the testing and production cloud setup [Pool 2 requirements D, Play 9]. 

Continuous Monitoring
=====================

For this prototype, we installed CloudWatch and Threat Stack, two security-related monitoring services that are built for AWS. [Pool 2 requirements F, Play 9 and Play 12]
Read more about our [continuous monitoring](https://github.com/artemis-consulting/prototype/blob/master/SUPPORTING_DOC.md#section-pool2-monitoring) here.
Read more about our [Nagios server monitoring](https://github.com/artemis-consulting/prototype/blob/master/SUPPORTING_DOC.md#section-pool2-nagios) here.

Configuration Management
========================

The team used Puppet for automated configuration management. Docker is used for container virtualization. A Docker container is available.
[Pool 2 requirements G]

Automated testing and deployments
---------------------------------
For this prototype, we built a suite of automated tests, which tested the app as well as ensured wide code coverage (>92%). [Pool 2 requirements F, Play 10].
To read more about the [testing frameworks and tools](https://github.com/artemis-consulting/prototype/blob/master/SUPPORTING_DOC.md#section-pool2-automated-testing) used for the FDA Pool2 prototype.

Running locally
---------------

### Prerequisites for Development Environment

Install the following for system level dependencies for Ubuntu
```shell
$ sudo apt-get install python python-dev apache2 libapache2-mod-wsgi git python_psycopg2 libpq-dev memcached
```

Clone this repository into desired $APP_DIR
```shell
$ git clone https://github.com/artemis-consulting/prototype-pool3 $APP_DIR
$ cd $APP_DIR/code
```
Create the database:
```shell
sudo su - postgres
createdb prototype
createuser -P proto_user
```
choose 'proto_pass' as password.  If choosing a different password, keep it handy to modify in the settings file later.
```shell
psql
```
Grant privileges to the user
```shell
# GRANT ALL PRIVILEGES ON DATABASE prototype TO proto_user;
```
Create a virtualenv
```shell
virtualenv aretmisprototype
source $APP_DIR/artemisprototype/bin/activate
```
Install the Python modules using pip. 
```shell
pip install -r code/requirements.txt
```

Run django commands
```shell
python manage.py migrate
python manage.py collectstatic
```

Make changes to the settings file if needed.
Change DATABASE settings if you changed the password for example
Change ALLOWED_HOSTS to appropriate domain name if you're not using localhost


### Running Locally
To test the install, use django's runserver command
```shell
python manage.py runserver
```
You can now open [http://localhost:8000](http://localhost:8000) in your browser.
Set up Apache using mod_wsgi
https://code.djangoproject.com/wiki/django_apache_and_mod_wsgi

Sample apache config for django running daemon mode with virtualenv:
```shell
<VirtualHost *:80>

 WSGIDaemonProcess prototype python-path=/apps/prototype/code:/apps/env/lib/python2.7/site-packages
 WSGIScriptAlias / /apps/prototype/code/opendata_fda/wsgi.py process-group=prototype

 Alias /static/ /apps/prototype/code/.static/
 
 <Directory /apps/prototype/code/opendata_fda>
 Require all granted
 </Directory>
 
 <Directory /apps/prototype/code/.static>
 Require all granted
 </Directory>
 
</VirtualHost>
```

Start Apache


You can now open [http://localhost:80](http://localhost:80) in your browser.

### Testing

#### Unit tests

To run the unit tests, use django's test framework with coverage
```shell
$ python manage.py test core --with-coverage --cover-html --cover-package=core
```
The unit tests will also kick off the selenium tests.
You can view the full details of coverage in a drill-down enabled report by opening:

 - Backend report: $APP_DIR/cover/index.html

### Docker image
If you use [Docker](https://www.docker.com/) for virtualization, a Docker container is [available] (https://github.com/artemis-consulting/prototype/)

