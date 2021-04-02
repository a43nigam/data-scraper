# data-scraper

This takes a college name and finds its common data set from 2018 (not all colleges published the 2019 set for some reason). Not all schools publish or participate in the Common Data Set initiative, so many colleges in the list have an 'n/a' in the CDS column. Only ~25% of accredited universities publish common data sets.

View the google sheet for which this code works here: https://docs.google.com/spreadsheets/d/1vVwnG6BgqjBM9pYOV5jXfOD8SexR-D64gg8ck8KTIhE/edit#gid=0

Make sure client_id.json and credentials.json are in the same virtual environment as scraper.py.

Make sure the pause for google search is more than 2s, any less than that and you risk getting an http 429 too many requests error, or even getting your IP address blocked from google. 
