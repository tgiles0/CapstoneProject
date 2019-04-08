# CapstoneProject

This repository contains several Python scripts that were used in the data cleansing 
and preparation phase.

Data cleansed by this scripts was retrieved from the splunk/botsv1 repository and as it
was exported directly from Splunk the raw data fields were all bunched together in one 
column of csv files of this data. Our Capstone team wanted to further analyze the important
information contianed in this raw data column and this was accomplished through the
creation of these various python scripts.

Having done this the cleansed data was then able to be further analyzed to create logistic
regression and decision tree models using the BigML platform.

Explainable AI (XAI) was also done on this data through Prediction Explanation tools available
on the BigML platform.
