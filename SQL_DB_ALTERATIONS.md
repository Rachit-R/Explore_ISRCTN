-- Data Refinement

1) Reassign NULL values to not specified in Intervention_type
2) Group participant types into more appropriate buckets
3) For sponsor country add category "joint" for multiple countries
4) Add 'mixed' study setting for study_setting column 
5) Group study setting types into more appropriate buckets
6) Change condition category from not specified to Not applicable 
7) Change intervention type of Genetic to Other.
8) Changed studies by age group, 'Other' merged into 'Not specified', 'All' to 'Mixed', 'Senior' to 'Adult'
9) 

1)
UPDATE ISRCTN
SET Intervention_type = 'Not Specified'
WHERE Intervention_type IS NULL;


2)
UPDATE ISRCTN
SET Participant_types = 'Mixed'
WHERE Participant_types LIKE '%;%';

UPDATE ISRCTN
SET Participant_types = 'Mixed'
WHERE Participant_types = 'All';

UPDATE ISRCTN
SET Participant_type = 'Not Specified'
WHERE Participant_type NOT IN ('Patient', 'Healthy volunteer', 'Mixed');

3)
UPDATE ISRCTN
SET Sponsor_Country = 'Joint'
WHERE Sponsor_Country LIKE '%;%';

4)
UPDATE ISRCTN
SET Study_settings = 'Mixed'
WHERE Study_settings LIKE '%;%';

5)

-- Update Community and Residential
UPDATE ISRCTN
SET Study_settings = 'Community and Residential'
WHERE Study_settings IN ('Community', 'Home', 'Care home', 'Hospice', 'Childcare/pre-school');

-- Update Educational Institutions
UPDATE ISRCTN
SET Study_settings = 'Educational Institutions'
WHERE Study_settings IN ('University/medical school/dental school', 'School');

-- Update Remote
UPDATE ISRCTN
SET Study_settings = 'Remote'
WHERE Study_settings IN ('Internet/virtual', 'Telephone');

-- Update Hospital - Healthcare
UPDATE ISRCTN
SET Study_settings = 'Hospital - Healthcare'
WHERE Study_settings IN ('Hospital', 'GP practice', 'Dental clinic');

-- Update Laboratory and Research
UPDATE ISRCTN
SET Study_settings = 'Laboratory and Research'
WHERE Study_settings IN ('Laboratory', 'Pharmaceutical testing facility', 'Training facility/simulation', 'Medical and other records', 'Fitness/sport facility');

-- Update Other
UPDATE ISRCTN
SET Study_settings = 'Other'
WHERE Study_settings IN ( 'Workplace', 'Charity/Voluntary sector', 'Other therapist office', 'Paramedicine', 'Prison/detention');

6)
UPDATE ISRCTN 
SET Condition_category = 'Not Applicable'
WHERE Condition_category = 'Not Specified';

7)
UPDATE ISRCTN
SET Intervention_type = 'Other'
WHERE Intervention_type = 'Genetic';

8)
UPDATE ISRCTN 
SET Age_group = 'Mixed'
WHERE Age_group = 'All';

UPDATE ISRCTN 
SET Age_group = 'Not Specified'
WHERE Age_group = 'Other';

UPDATE ISRCTN 
SET Age_group = 'Adult'
WHERE Age_group = 'Senior';

