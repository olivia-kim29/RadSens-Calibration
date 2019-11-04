# RadSens-Calibration

Pocket Geiger Calibration
	Instructions and Explanation

2 Methods: Repeat Experimental Contraints or Repeat Experiment

	Go to RadSens Calibration Git Hub Directory, download all files in download folder.
		IF: Repeating Constraints, use given csv. precalibrated data
1. Download Calibration Code and .csv data from calibrated Geiger Muller Counter 
2. Specify directory of data from calibrated detector in the code
3. Test if Pocket Geiger is working on the rPi0 // Connect Pocket Geiger
4. Run calibration code//Recreate Experimental data
	-The code now gets counts from the pocket geiger that will be as experimentally accurate to the GMC detector.
	- Place the Pocket geiger parallel to the center of the thorium rock source and 10 cm away
	- Run calibration code
	-The code will compare the PG's counts to the GMC's count from the same angle, distance, and source and create a calibration constant for your PG.
5. The pocket geiger now has a calibration constant that will be pushed to the rPi0 code. When it collects counts, it will use this constant to convert it to a dose.

	IF Repeating Experiment
1. Download Calibration code and GQ GMC Data viewer to get .csv data from the GMC detector
	a. the data viewer only works on windows machines
	b. Collect GMC data for at least 5 minutes
	c. Download the .csv from the realtime monitoring of the GMC data
	d. Orient PG (see below)
	e. run calibration over same time interval as in b.
2. Use a source, GMC and PG detector
3. Place them in as similar orientation and distance from the source as possible
4. Run the code, it will use the .csv from the GMC and compare the counts from the PG and create a calibration constant.
5. The pocket geiger now has a calibration constant that will be pushed to the rPi0 code. When it collects counts, it will use this constant to convert it to a dose.
