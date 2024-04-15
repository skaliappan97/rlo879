
## Exporting Your Data

1. iPhone/Apple Watch: 
    1. Go to the “Health” app on your iPhone.
    2. Click on the profile icon on the top right corner.
    3. Select “Export All Health Data” on the bottom. This process might take some time.
    4. Transfer it to your PC/laptop by email, AirDrop, or any other method you prefer.
    5. Open and Review your data by unzipping the downloaded file. This will include:
        a. Folders:
            1. Electrocardiograms
            2. workout-routines → workout location data
        b. Files:
            1. Export_cda.xml
            2. export.xml -> data stored in various tags: record, StepCount,  WorkoutActivity, WorkoutEvent, WorkoutStatistics, WorkoutRoute, ActivitySummary, ClinicalRecord, Audiogram, and much more.
    6. Add the following scripts to the Apple health export folder.
        1. Convert__xm__csv.py
        2. Get_sleep.py
        3. Get_stepy.py
        4. Run the files in the same order
2. Android: We recommend using Google Fit as a step counter/sleep tracker.
    1. Go to [Google Takeout](https://takeout.google.com/)
    2. Under “Select data to include”, first deselect all
    3. Select “Fit”
    4. Select “Next step”
    5. Select “Create Export”
    6. You will receive an email with your information. Download the folder and unzip it.
    7. You are now ready for preprocessing!

3. Fitbit : Step-by-Step Guide to Extract Data from Fitbit

    1. Visit the Fitbit Website: Open your web browser and go to Fitbit's official website (Fitbit).
        - Access Your Account: Click on the login link and enter your credentials to access your account.
    2. Access the Dashboard
        - Navigate to Settings: Once logged in, locate and click on the Data Export panel on the left side of the page.

    3. Google Takeout
        - This will take you to Google Takeout.
        - Choose Data Types: Select the types of data you want to include, in this case select Fitbit
    4. Export Your Data
        - Choose export destination and frequency, for this project select Export once.
        - Create Export: Choose this option, you’ll get an email with the download link.
    5. Download the data and review the contents.

## Processing Your Data: 
1. We have provided scripts depending on which platform you are using. 
    1. Apple: Run `export_scripts/`
    2. Android (Google Fit): Run `export_scripts/google_fit_sleep.py` and `export_scripts/google_fit_step.py`
    3. Fitbit: TODO
2. Do some data cleaning: TODO

## Analyzing Your Data
TODO cleanup

## Writing A Reflection 
TODO prompt
