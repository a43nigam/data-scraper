# data-scraper
Used to collect data for https://www.todocollege.com/, a website to help high schoolers organize their college applications. 

This takes a college name and finds its common data set from 2018 (not all colleges published the 2019 set for some reason). Not all schools publish or participate in the Common Data Set initiative, so many colleges in the list have an 'n/a' in the CDS column. Only ~25% of accredited universities publish common data sets, but applicants are disproportionately interested in those who do.

View the google sheet for this code here: https://docs.google.com/spreadsheets/d/1vVwnG6BgqjBM9pYOV5jXfOD8SexR-D64gg8ck8KTIhE/edit#gid=0

Create a credentials.json and client_id.json from GCP and make sure they are in the same virtual environment as scraper.py.

Make sure the pause for google search is more than 2s, any less than that and you risk getting an http 429 too many requests error or getting your IP address blocked from google. 
