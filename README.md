# RadSens-Calibration

Pocket Geiger Calibration

Instructions and Explanation

Repeat Experiment and Calibration

1. Download Calibration code (calibrationsetup.ipynb), calibration data, and GQ GMC Data viewer  to get .csv data from the GMC detector 
	
	a. the data viewer only works on windows machines
	
	b. Collect GMC data for some time interval 
		
		i. Will collect PG data for calibration over the same timer interval
	
	c. Download the .csv from the realtime monitoring of the GMC data or make your own
		
		i. Will have to specify the directory which the data is collected in inside the script
	
	d. Orient PG (see below)
2. Use a source, GMC and PG detector

3. Place them in as similar orientation and distance from the source as possible, do not let anything move during data collection

4. Run the code, it will use the .csv from the GMC and compare the counts from the PG and create a corrected calibration constant and error/percent error

5. The pocket geiger now has a calibration constant which is multuplied by the counts to read out a dose
