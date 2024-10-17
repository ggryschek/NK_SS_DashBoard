About Tab

# Neurologisk Klinik - DashBoard

**Synapse Solutions**
```
Team Members:  
- Agnes Rehn 
- Alhaan Kasi
- Guilherme Gryschek
- Nchedochukwu Uzoigwe
- Ning Gai
- Sreeja Mohanan Nair

```

### Business Problem

To enhance care for Alzeimers patient’s, data from NK will be used to gain insight in the disease. The business need will focus on early detection of the disease and risk prevention, to enhance personalized care, and optimize the resources used. The following areas will enhance early detection, optimize resources and provide a more person-centered care. 

#### Early detection of the disease and risk prevention

The predictive models will be able to foresee an Alzheimer's diagnosis, making it easier for health care workers to identify risk patients,  which can lead to earlier treatment plans and better patient outcomes. 

#### Enhance personalized care

By combining different features with each other based on patient data, more tailored correlations can arise, which can lead to a more person-centered and more effective treatment plan. This can also lead to a higher chance of patient satisfaction.

#### Optimizing resources

By becoming more familiar with the patient group and its correlations, resources will be able to be distributed more efficiently and the patient flow will be able to increase without affecting the quality of care. This through a better optimization of personnel resources and reduction of unnecessary costs.

### Dataset Description

Neurologisk Klinik has compiled a synthetic and anonymized dataset [1] with detailed health information for synthetic 2,149 patients, each identified by a unique ID (4751 and 6900). The dataset contains various types of data. Patient Information includes a unique PatientID (integer). Demographic Details cover Age (integer), Gender (binary), Ethnicity, and EducationLevel (categorical). Lifestyle Factors include BMI (float), Smoking, AlcoholConsumption, PhysicalActivity, DietQuality, and SleepQuality (integers or binary). Medical History variables are binary (e.g., FamilyHistoryAlzheimers, Hypertension). Clinical Measurements include blood pressure and cholesterol levels (integers). Cognitive and Functional Assessments cover MMSE, FunctionalAssessment, ADL (integers), and several binary indicators. Symptoms are binary (e.g., Confusion, Forgetfulness). Diagnosis Information is binary for Alzheimer’s status. DoctorInCharge: This column contains confidential information about the doctor in charge, with "XXXConfid" as the value for all patients.

The original dataset can be retrieved from: https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset [1]

### Justification for Alzheimer's Patients clinical data

DEMENTIA RISK FACTORS

Emerging evidence indicates that dementia shares several modifiable risk factors with other non-communicable diseases (NCDs). These include physical inactivity, obesity, tobacco use, excessive alcohol consumption, diabetes mellitus, and hypertension during mid-life. Additionally, certain risk factors more closely linked to dementia are social isolation, low educational attainment, cognitive inactivity, and mid-life depression.

Mitigating exposure to these modifiable risk factors at both the individual and population levels—starting from childhood and continuing throughout life—can enhance individuals’ and communities’ abilities to make healthier choices and adopt lifestyle patterns that promote overall well-being. [4]

#### Disclaimer
The limited availability of real-world data poses significant challenges to development and innovation in the medical field. Given the sensitivity of medical data, using real patient information introduces privacy risks and regulatory concerns. By leveraging synthetic data, we can effectively mitigate these concerns, ensuring compliance with patient confidentiality and data protection regulations.
Once the initial testing and development are complete, the dashboard will be validated using real patient data provided by NK. This approach allows us to develop a reliable system in an ethical manner while being prepared to refine the system with real-world data later.

##  Dataset Dictionary for Data Visualization

### Table of Contents
#### Patient Information
    - Patient ID
    - Demographic Details
    - Lifestyle Factors
    - Medical History
    - Clinical Measurements
    - Cognitive and Functional Assessments
    - Symptoms
    - Diagnosis Information
    - Doctor In Charge Information

##### Details - Patient Information
1. Patient ID

        1.1 PatientID: A unique identifier assigned to each patient (4751 to 6900).

2. Demographic Details

        2.1 Age: The age of the patients ranges from 60 to 90 years.
        2.2 AgeRange: range of grouped ages as categories, splited in 10 years range.
        2.3 Gender: Gender of the patients, where 0 represents Male and 1 represents Female.
        2.4 Ethnicity: The ethnicity of the patients, coded as follows:
            0: Caucasian
            1: African American
            2: Asian
            3: Other
        2.5 EducationLevel: The education level of the patients, coded as follows:
            0: No Formal Education
            1: High School
            2: Bachelor's
            3: Higher
            
3. Lifestyle Factors

        3.1 BMI: Body Mass Index of the patients, ranging from 15 to 40.
        3.2 Smoking: Smoking status, where 0 indicates No and 1 indicates Yes.
        3.4 AlcoholConsumption: Weekly alcohol consumption in units, ranging from 0 to 20.
        3.5 PhysicalActivity: Weekly physical activity in hours, ranging from 0 to 10.
        3.6 DietQuality: Diet quality score, ranging from 0 to 10.
        3.7 SleepQuality: Sleep quality score, ranging from 4 to 10.
        3.8 WeightStatus: variable to categorize the weight based on BMI measures, in 7 different classes (7): 'Severely underweight','Underweight', 'Normal weight', 'Overweight', 'Obesity class I', 'Obesity class II','Obesity class III'.

4. Medical History

        4.1 FamilyHistoryAlzheimers: Family history of Alzheimer's Disease, where 0 indicates No and 1 indicates Yes.
        4.2 CardiovascularDisease: Presence of cardiovascular disease, where 0 indicates No and 1 indicates Yes.
        4.3 Diabetes: Presence of diabetes, where 0 indicates No and 1 indicates Yes.
        4.4 Depression: Presence of depression, where 0 indicates No and 1 indicates Yes.
        4.5 HeadInjury: History of head injury, where 0 indicates No and 1 indicates Yes.
        4.6 Hypertension: Presence of hypertension, where 0 indicates No and 1 indicates Yes.

5. Clinical Measurements

        5.1 SystolicBP: Systolic blood pressure, ranging from 90 to 180 mmHg.
        5.2 DiastolicBP: Diastolic blood pressure, ranging from 60 to 120 mmHg.
        5.3 CholesterolTotal: Total cholesterol levels, ranging from 150 to 300 mg/dL.
        5.4 CholesterolLDL: Low-density lipoprotein cholesterol levels, ranging from 50 to 200 mg/dL.
        5.5 CholesterolHDL: High-density lipoprotein cholesterol levels, ranging from 20 to 100 mg/dL.
        5.6 CholesterolTriglycerides: Triglycerides levels, ranging from 50 to 400 mg/dL.

6. Cognitive and Functional Assessments

        6.1 MMSE: Mini-Mental State Examination score, ranging from 0 to 30. Lower scores indicate cognitive impairment.
        6.2 FunctionalAssessment: Functional assessment score, ranging from 0 to 10. Lower scores indicate greater impairment.
        6.3 MemoryComplaints: Presence of memory complaints, where 0 indicates No and 1 indicates Yes.
        6.4 BehavioralProblems: Presence of behavioral problems, where 0 indicates No and 1 indicates Yes.
        6.5 ADL: Activities of Daily Living score, ranging from 0 to 10.00. Lower scores indicate greater impairment.
        6.6 ImpairmentLevel: based on MMSE score, to categorize in 4 different classes, related to scientific literature (3): 'Severe', 'Moderate', 'Mild', 'No Imparment'.
        6.7 DependencyLevel: based on ADL scores, to categorize patients in 5 different classes, related to scientific literature (4): 'Totally dependent', 'Very dependent', 'Partially dependent', 'Minimally dependent', 'Independent'.

7. Symptoms

        7.1 Confusion: Presence of confusion, where 0 indicates No and 1 indicates Yes.
        7.2 Disorientation: Presence of disorientation, where 0 indicates No and 1 indicates Yes.
        7.3 PersonalityChanges: Presence of personality changes, where 0 indicates No and 1 indicates Yes.
        7.4 DifficultyCompletingTasks: Presence of difficulty completing tasks, where 0 indicates No and 1 indicates Yes.
        7.5 Forgetfulness: Presence of forgetfulness, where 0 indicates No and 1 indicates Yes.

8. Diagnosis Information

        8.1 Diagnosis: Diagnosis status for Alzheimer's Disease, where 0 indicates No and 1 indicates Yes.

9. Doctor In Charge Information

        9.1 DoctorInCharge: This column contains confidential information about the doctor in charge on the original dataset; for the visualization tasks, "Med A", "Med B" and "Med C" were the values randomly assigned for all patients, to simulate filters based on health professionals.

## References
1. El Kharoua R. Alzheimer’s Disease Dataset [Internet]. Kaggle; 2024 [cited 2024 Sep 6]. Available from: https://doi.org/10.34740/KAGGLE/DSV/8668279
2. Weintraub S, Carrillo MC, Farias ST, Goldberg TE, Hendrix JA, Jaeger J, Knopman DS, Langbaum JB, Park DC, Ropacki MT, Sikkes SAM, Welsh-Bohmer KA, Bain LJ, Brashear R, Budur K, Graf A, Martenyi F, Storck MS, Randolph C. Measuring cognition and function in the preclinical stage of Alzheimer's disease. Alzheimers Dement (N Y). 2018 Feb 13;4:64-75. doi: 10.1016/j.trci.2018.01.003. PMID: 29955653; PMCID: PMC6021264.
3. Zeltzer L, Korner-Bitensky N, Sitcoff E. Mini-Mental State Examination (MMSE) [Internet]. StrokEngine. 2010 Jul 11 [cited 2024 Sep 13]. Available from: https://strokengine.ca/en/assessments/mini-mental-state-examination-mmse/
4. Mahoney FI, Barthel D. Functional evaluation: The Barthel Index. Maryland State Medical Journal 1965;14:56-61. Available from: MDCalc. Barthel Index of Activities of Daily Living (ADL) [Internet]. Available from: https://www.mdcalc.com/calc/3912/barthel-index-activities-daily-living-adl#evidence
5. World Health Organization (2018). The global dementia observatory reference guide. World Health Organization. https://iris.who.int/handle/10665/272669
6. Hypertension in adults: diagnosis and management. London: National Institute for Health and Care Excellence (NICE); 2023 Nov 21. (NICE Guideline, No. 136.) Available from: https://www.ncbi.nlm.nih.gov/books/NBK547161/
7. Weir CB, Jan A. BMI Classification Percentile And Cut Off Points. [Updated 2023 Jun 26]. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2024 Jan-. Available from: https://www.ncbi.nlm.nih.gov/books/NBK541070/
8. Tahami Monfared AA, Phan NTN, Pearson I, Mauskopf J, Cho M, Zhang Q, Hampel H. A Systematic Review of Clinical Practice Guidelines for Alzheimer's Disease and Strategies for Future Advancements. Neurol Ther. 2023 Aug;12(4):1257-1284. doi: 10.1007/s40120-023-00504-6. Epub 2023 Jun 1. PMID: 37261607; PMCID: PMC10310649.
