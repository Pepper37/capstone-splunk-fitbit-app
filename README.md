# Capstone Project for Information Technology BS degree through ASU's Fulton Schools of Engineering

Project worked on with collaboration of team members Peter Luyten and Chi Ko
-
A Splunk app that takes user data from a fitbit account, performs in-depth data analysis, and displays results via custom dashboards


We each had individual Ubuntu virtual machines each running a Splunk Enterprise server. We shared code changes via Discord, in retrospect actually using Git for version control would have been much better, and had all team members been able to get Github working early on this would have been the case.

In our Splunk app, called Capstone, we have a Python script (under `Capstone/bin/python-fitbit-master/GetData.py`) that runs a CherryPy server calling the Fitbit API which gets us our fitness data. We then format that data and place it in a `lookups` directory for Splunk to ingest. This python script is attributed to the Python Fitbit API implementation by ORCAS, found here: https://github.com/orcasgit/python-fitbit

We ingest this data into the Splunk server, and in  our Capstone app we run SPL queries to turn that data into custom dashboards created using Splunk's Dashboard Studio. These dashboards also include Splunk MLTK queries that predict future behavior using machine learning algorithms provided by Splunk in the MLTK. These predictions are included in the dashboards in the Capstone app. 

<img src="/final deliverable poster.png" alt="project presentation" width="50%" height="50%">

<img src="/Dashboard Screenshots/actdash.png" alt="activity dashboard" width="50%" height="50%">

<img src="/Dashboard Screenshots/sleepdashall.png" alt="activity dashboard" width="50%" height="50%">
