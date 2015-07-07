Supporting Document for Artemis Consulting's Pool 2 Submission
==============================================================
Section-pool2-Vision
----------------------
The "problem statement" describes the current business scenario that creates the need for this project. We decided on the following "problem statement": “We will produce a usable, mobile-friendly and accessible public website using OpenFDA's APIs for drugs, and win one of the BPAs in the process”.  We also created a concise "vision statement" to ensure that the solution meets the intended product owner’s and users’ goals. This shared "vision statement" also helped to keep our team focused: "To deliver a fast, responsive and intuitive API-driven website using the Drug Labels API, Adverse Events API and Enforcement Actions API that integrates information  for the public and other potential users in a holistic fashion, within the next 6 days".

Section-pool2-Overview
----------------------
Since the original RFP had a due date of 06/26/2015, the team had to place boundaries around the solution by deciding which features and system functions to focus on. Due to time constraints, the decision was made to de-scope the following items and revisit them at future sprints.
 * All ‘food’ elements from our system
 * Off-line browsing (e.g. keep the service in case the FDA APIs are down) 
 * Full-blown load testing
 * Content Delivery Network for static content

### Initial scope
Defining the project scope early on helped the team set stakeholders’ expectations while providing sufficient details and features for the team to focus on.
The team determined that instead of using a single API from OpenFDA, what would really serve the public is a website that consumes all the APIs that OpenFDA offers in one target area. Since the APIs are divided into "Drugs", "Devices" and "Food" with "Drugs" having the most APIs, we decided to build a website that consumed all 3 Drugs-related APIs, and offer the users of the site a chance to see the interconnections betwen drug labels, drug adverse reactions and drug recalls. The interconnection would be from each API's dataset to the other API's dataset using targeted queries. In the end based on user testing with our doctor and lawyer subject matter experts(SMEs), we also decided to add a completely new Drug Manufacturers section on the site, which further interconnected the 3 API datasets together but using derived data from each dataset.
The team also decided to support two navigation paradigms for the 4 data sets: Browse and Search. Users could look at a list of what's available for each data set, or could search for an item of interest in each data set. Once the user found an item, the user would still be able to navigate to the other connected data from each item.
The final list of key features we decided to support were:
* Browse drugs by label
* Search drugs by label
* Browse adverse reactions by frequency
* Search adverse reactions
* Browse drug enforcement actions by state
* Browse adverse reactions by gender
* Submit questions using a “Contact Us” form
* Ensure speed and high performance
* Responsive mobile-friendly design
* Section 508-compliant accessible design

Section-pool2-UCD
-----------------

In most of our current client projects, we use an integrated ‘User-Centered Design’ process  where we strongly encourage end-users to shape how the final system gets developed. For the FDA project, we decided on the following UCD techniques (mainly due to time constraints): user personas, user journeys, usability testing, interviews, expert reviews, and prototypes.

During the story planning meetings, the following prospective users where identified: Public users, doctors, pharmacists, attorneys, FDA SMEs/employees, Federal regulators, Federal Watchdog agencies, state regulators

Based on the analyzed interview results, the team ended up with the following personas:
* Novice – public users, concerned parents, students, people in the drug and food industry 
* Professional – doctors, pharmacists, mainly medical professionals
* Specialist – Attorney, policy makers, and maybe bloggers 
* Experts – FDA employees, state regulators, federal watchdogs

The team strongly felt that applying the UCD techniques in the sections previously mentioned satisfy Play [1] and [2].

When teams have accurate user data at their disposal, the task of designing simple, intuitive, easy-to-use but powerful, interface becomes much more straight-forward. The key design objective was to make the service user friendly instead of frustrating or confusing. Due to time constraints, the team decided against creating a (more traditional) style guide from scratch but opted to use the Bootswatch Paper theme as the design style guide and pattern library for the website. By using this flexible style guide for design and incorporating accessibility best practices, the team is confident that they have satisfied Play [3], ensuring all prospective users can navigate the service intuitively and can obtain the information they want from the service, in a easy and consistent way. 

Section-pool2-UX-usability-testing 
---------------------------------
### Usability Testing

Agile usability testing was integrated with the design and development process so that we could identify and fix user experience problems before they become baked in and expensive to address. In addition to being fast and inexpensive, agile style user testing is highly flexible; it can be conducted without a dedicated lab, on-site and remotely, in both moderated and un-moderated formats. Due to the quick response time required for this prototype, we were not able to use Artemis' standard usability testing tool called Chalkmark.  To view the results the usability testing conducted on 06/12/15, see below.

Section-pool2-UX-testing
------------------------

Here is an overview of the results from Agile UX testing conducted on 06/12/15.
* The subheads/instructions to be too large (The header should not dominate the page and should be a smaller than the “branding” text in the nav bar. They should appear as informational/instructions).
* The gray paragraph text on a gray background can be hard to read (basic design and 508 issue, perhaps lighten the background color).
* The navigation is little redundant and a bit confusing (the buttons below the search box are repeats of the main nav. They should be combined in a dropdown in the search box. Apply the materials theme to the basic sample below).
* It’s not initially clear what or why I am searching “drugs” (Replace initial text with something like the following:
  Search for current drug related information
  Begin your request for FDA drug related information by entering a search term and choosing a category from the dropdown menu).
* I would like more information about the purpose and use of the web app (Add some text to the home page, something like the following:
   Welcome to the FDA Drug Monitor
  We know you take your health seriously. Having the latest Drug related information and tools at your fingertips is a critical part of you overall health and well-being. The information provided by the FDA Drug Monitor is the latest and most relevant in our database. Use it along with your physicians’ advice to make informed decisions about the drugs you take.
  Please note that the information provided here is for reference only and is not intended as medical advice or diagnosis. Always consult with your physician before making drug related decisions.).
* I would like to know more about this app (Add a basic footer to all pages that perhaps include: About | Last Updated).

### Drug Names Page
* I find the subheads/instructions to be too large (The header should not dominate the page and should be a smaller than the “branding” text in the nav bar. They should appear as informational/instructions).
* It’s not initially clear what or why I am presented with this list (Replace initial text with something like the following:
  Select a drug from the list to view current drug related information).
* I find the list of drugs too long and in no apparent order (Put the drugs in alphabetical order and in a list group with the badge option for the number of drugs. Apply the materials theme to the basic sample below).
* I don’t know how to get back to the search from either a list or detail page (perhaps add a “back to search” arrow/button).

### Adverse Events Page
* I find the subheads/instructions to be too large (The header should not dominate the page and should be a smaller than the “branding” text in the nav bar. They should appear as informational/instructions).
* It ‘s not initially clear what or why I am presented with this list (Replace initial text with something like the following:
  Select an event from the list to view current event related information).
* I find the list of events to be long and in no apparent order (Put the drugs in alphabetical order and in a list group with the badge option for the number of drugs. Apply the materials theme to the basic sample below).
* I don’t know how to get back to the search from either a list or detail page (perhaps add a “back to search” arrow/button).

### Enforcement Reports Page
* The subheads/instructions to be too large (The header should not dominate the page and should be a smaller than the “branding” text in the nav bar. They should appear as informational/instructions).
* It’s not initially clear what or why I am presented with this list (Replace initial text with something like the following:
  Select a state on the map to view current enforcement reports .
* I find the list of states below the map to be long and in no apparent order (Put the drugs in alphabetical order and in a list group with the badge option for the number of drugs. Apply the materials theme to the basic sample below).
* I don’t know how to get back to the search from either a list or detail page (perhaps add a “back to search” arrow/button).

### About Page
* I would like more information about the purpose, use, and creation of this web app (Add an About page with some text, something like the following:
  Welcome to the FDA Drug Monitor
  We know you take your health seriously. Having the latest Drug related information and tools at your fingertips is a critical part of you overall health and well-being. The information provided by the FDA Drug Monitor is the latest and most relevant in our database. Use it along with your physicians advice to make informed decisions about the drugs you take.
  Please note that the information provided here is for reference only and is not intended as medical advice or diagnosis. Always consult with your physician before making drug related decisions.).
  For more information regarding your health visit www.fda.gov/
  This application was designed and build by Artemis Consulting, Inc. For more information visit www.artemisconsultinginc.com

Section-pool2-Agile
-------------------

Artemis Consulting uses agile scrum techniques for all their internal development efforts and for most of our client projects. For our agile projects, sprints are usually 1-2 week in duration but never exceed 3 weeks. In general, the shorter the sprints, the faster feedback we receive from our users and clients. This timely feedback enables the team quickly make the necessary adjustments, avoiding potential long-term and costly rework. For the FDA prototype, we decided on 2 day sprints but chose to add a 4 day sprint to accommodate the unusual nature of this project and weekend work.

* We used the open source Taiga tool for agile project management and defect tracking. Taiga tends to be more ‘lightweight’ for project with relative quick turnarounds and firm deadlines. Additional information on Taiga can be found [here](https://github.com/artemis-consulting/prototype/tree/master/doc/agile-process/agile-tool-taiga).
* All our agile artifacts related to Play 4, can be found here -> [Sprints](https://github.com/artemis-consulting/prototype/tree/master/doc/agile-process). 

Section-pool2-automated-testing
-------------------------------
Unit testing reduces the amount of bugs that get into the code and potentially into production. Since automated tests can be ran as frequently as needed, and the use of automated test suites makes it easier to change and refactor code later on, unit testing saves precious development time during the life cycle of the product.  For this prototype, the team built a suite of automated tests, which tested the app as well as ensured wide code coverage (>92%). The Pyunit framework was used for unit testing. The team selected Selenium WebDriver for automated web testing. Jenkins was used as our continuous integration and continuous deployment tool.  Upon code commits/checkins into GitHub, Jenkins automatically runs the unit test suites. If the unit tests pass, the code is automatically promoted to the testing/integration environment.  To view the Selenium testing scripts, click [here](https://github.com/artemis-consulting/prototype/blob/master/code/core/tests/test_behavior.py). Additional automated tests are [here](https://github.com/artemis-consulting/prototype/tree/master/code/core/tests). The coverage is currently at >92% as can be viewed [here](https://github.com/artemis-consulting/prototype/blob/master/doc/testing/PythonUnitTestsCoverage.png).  [Pool 3 requirements F, Play 10]

Product Roadmap/Release Strategy
--------------------------------
We followed the following roadmap for this project:
* R1:
	Initial UI;
	Deployment of Drug Browse and Detail pages;
	Deployment of Adverse event Browse and Detail pages;
	Deployment of Enforcement action Browse and Detail pages;
        Defect fixes
* R2:
 	Search;
 	Manufacturer pages;
        Defect fixes;
* R3:
	Final UI updates;
        Defect fixes

Section-pool2-Scrum
-------------------
### Scrum ceremonies

Daily standups at 10:30am, 2-day sprints, sprint planning every other day, review, retro, and release planning to occur and the end of each sprint, entire team to attend all meetings. Backlog grooming and reprioritization happened daily. 
To view all our agile artifacts, click [here](https://github.com/artemis-consulting/prototype/tree/master/doc/agile-process). 


Section-pool2-tools
-------------------
Slack was selected for chatting and online collaboration, Taiga.io for Agile project management, and GitHub for code versioning. The modern technology stack chosen by team is all open source with hosting being the only exception. By selecting the technology stack below, the team strongly feels that it can develop and prototype effectively while delivering a product that is cost-effective and can scale easily. Play [8]

### Tools 
Slack was selected for chatting and online collaboration, Taiga.io for Agile project management, and GitHub for code versioning. The modern technology stack chosen by team is all open source with hosting being the only exception. By selecting the technology stack below, the team strongly feels that it can develop and prototype effectively while delivering a product that is cost-effective and can scale easily. Play [8]

### Initial technology stack: 
#### Front-end development
* Django templates 1.8.2
* JavasScript/jQuery
* Bootstrap/Bootswatch Paper theme
* Highcharts chart and mapping widgets
* (Proprietary) accessibility toolkit

#### Back-end development
* Apache 2.4.7
* Python 2.7.10
* Django 1.8.2
* Memcached 1.4.27 
* Postgres 9.4

#### Configuration Management
* [Docker](http://docker.com): Provides portable containers of pre-configured software
* [Puppet](https://puppetlabs.com/): Manage ‘Ubuntu’ images for developers - automating the developers' workstation configurations

#### Environments 
We used Pivotal Web Services CloudFoundry as the development/test environment and Amazon Web Services as our production environment. Developers coded on their local machines (running Ubuntu/MacOS) to code the prototype.

#### Continuous Integration
- For this prototype, we used [Jenkins](http://jenkins-ci.org/) for CI.

#### Application Monitoring
- For this prototype, we installed and used [Nagios](https://www.nagios.org/) for application monitoring.

#### Continuous Deployment
- As mentioned above, we used [Jenkins](http://jenkins-ci.org/) for CD.
- Our dev/test servers were at [Pivotal CloudFoundry](http://pivotal.io/platform-as-a-service/pivotal-cloud-foundry)

Section-pool2-hosting
---------------------

### Flexible hosting environment 

During Sprint 0, the team performed various user analysis tasks and worked on deploying the hosting environment for both test and production. For the test environment (including continuous integration and continuous deployment), the team picked Pivotal's CloudFoundry service(a.k.a. PWS), and for production, the team chose Amazon Web Services (AWS). Both are flexible infrastructures, where additional resources can be provisioned in real-time to meet user demand. For the prototype’s testing environment, the team decided on using Pivotal Web Services (PWS) CloudFoundry, an open (and agile) platform as a service (PaaS).  The Cloud Foundry platform required minimal setup while still proving rapid deployment and scaling capabilities.  Jenkins on CloudBees was utilized for continuous integration and deployment integrated with Github. A Jenkins job periodically runs unit tests, and if the tests are successful, deploys the latest code from the repository to the CI/CD environment. If the tests are unsuccessful, an email is sent out to the appropriate developer. 

For production, we used Amazon Web Services(AWS) primarily AWS has been around for almost a decade now and offers highly reliable, scalable, and relatively inexpensive cloud hosting services.  The AWS management console is simple and relative straightforward web-based tool. Another driver for using AWS is the government’s interest in migrating parts of their IT infrastructure into the AWS GovCloud. AWS was officially approved for government use in 2013.

### Prototype
* [http://opendatafda-artemis.cfapps.io] or [http://demo.artemisconsultinginc.com](http://opendatafda-artemis.cfapps.io) continuously deployed on [Pivotal CloudFoundry](http://pivotal.io/platform-as-a-service/pivotal-cloud-foundry)
* Note: this development site is not part of the Artemis Consulting RFP submission to GSA/18F, and is not guaranteed to be available during the evaluation period. 

Section-pool2-monitoring
------------------------

### Continuous Monitoring

Continuous monitoring is a risk management approach to cybersecurity that maintains an accurate picture of an agency’s security risk posture, provides visibility into assets, and leverages use of automated data feeds to quantify risk, ensure effectiveness of security controls, and implement prioritized remedies. A well-designed and well-managed continuous monitoring program can effectively transform an otherwise static security control assessment and risk determination process into a dynamic process that provides essential, near real-time security status. For this prototype, we did not have the time to set up a full-blown security posture assessment. However, from past experience - this includes:
* Vulnerability testing
* Penetration testing
* Server OS configuration review
* OS / System Hardening
* Security audits

Using AWS for the production environment provided us additional integration benefits from a Continuous monitoring (CM) perspective. For this prototype, we installed and prototyped CloudWatch and ThreatStack, two monitoring services that are built for AWS. CloudWatch provides basic and detailed monitoring services and can monitor resource utilization, application and database performance, log files, and overall system’s health. If time permits, we will try to monitor custom metrics of the prototype via a simple API. The service provides a dashboard with graphs, statistics, and alarms. Threat Stack is another Continuous Security Monitoring service for AWS. It protects cloud instances from intrusions and data loss by continuously monitoring and providing insights into the system. We installed but were not able to fully explore this service. 

Section-pool2-Nagios
--------------------
Information on we setup Nagios for our needs on Ubuntu is [here] (http://nagios.sourceforge.net/docs/3_0/quickstart-ubuntu.html). Nagios of course can be set up on other Linux variants. 

Section-pool2-automated-testing
-------------------------------

### Automated testing and deployments

* For this prototype, the team built a suite of automated tests, which tested the app as well as ensured wide code coverage (>92%). [Pool 2 requirements F, Play 10]
* The Pyunit framework was used for unit testing.  As mentioned earlier, the Pyunit code coverage is currently at >92%. [Pool 2 requirements F, Play 10]
* The team used Selenium WebDriver for automated web testing.  Links to the Selenium testing scripts have already been provided earlier in this document. 
* Jenkins was used as our continuous integration and continuous deployment tool. Upon code commits into GitHub, Jenkins automatically runs the unit test suites. If the unit tests pass, the code is automatically promoted to the testing/integration environment. 
For the purposes of this app, Artemis used a cloud-based Jenkins installation called [CloudBees](https://www.cloudbees.com/), and a configuration management tool called [Puppet](https://puppetlabs.com/). The setup of Jenkins instance on Cloudbees is shown in the following screenshots: [Jenkins Screenshot 1](https://github.com/artemis-consulting/prototype/blob/master/deployment/CloudBeesScreenshot1.png), [Jenkins Screenshot 2](https://github.com/artemis-consulting/prototype/blob/master/deployment/CloudBeesScreenshot2.png), and [Jenkins Screenshot 3](https://github.com/artemis-consulting/prototype/blob/master/deployment/CloudBeesScreenshot1.png).

