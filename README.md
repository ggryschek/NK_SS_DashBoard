# NK Dashboard

![NK Dashboard](./assets/Neurologisk_Klinik_Logo.jpg)

## Introduction

To enhance care for Alzeimers patient’s, data from NK will be used to gain insight in the disease. The business need will focus on early detection of the disease and risk prevention, to enhance personalized care, and optimize the resources used. The following areas will enhance early detection, optimize resources and provide a more person-centered care. 

#### Early detection of the disease and risk prevention

The predictive models will be able to foresee an Alzheimer's diagnosis, making it easier for health care workers to identify risk patients,  which can lead to earlier treatment plans and better patient outcomes. 

#### Enhance personalized care

By combining different features with each other based on patient data, more tailored correlations can arise, which can lead to a more person-centered and more effective treatment plan. This can also lead to a higher chance of patient satisfaction.

#### Optimizing resources

By becoming more familiar with the patient group and its correlations, resources will be able to be distributed more efficiently and the patient flow will be able to increase without affecting the quality of care. This through a better optimization of personnel resources and reduction of unnecessary costs.

## System description

### Dependencies

Tested on Python 3.10 with the following packages:
  - Jupyter v1.1.1
  - Streamlit v1.38.0
  - Seaborn v0.13.2
  - Plotly v5.24.0
  - Scikit-Learn v1.5.1
  - shap v0.46.0
  - pandas v2.2.2
  - numpy v1.24.4
  - skimpy v0.0.15
  - joblib v1.3.2

### Installation

Run the commands below in a terminal to configure the project and install the package dependencies for the first time.

If you are using Mac, you may need to follow install Xcode. Check the official Streamlit documentation [here](https://docs.streamlit.io/get-started/installation/command-line#prerequisites). 

1. Create the environment with `python -m venv env`
2. Activate the virtual environment for Python
   - `source env/bin/activate` [in Linux/Mac]
   - `.\env\Scripts\activate.bat` [in Windows command prompt]
   - `.\env\Scripts\Activate.ps1` [in Windows PowerShell]
3. Make sure that your terminal is in the environment (`env`) not in the global Python installation
4. Install required packages `pip install -r analysis/requirements.txt`
5. Check that everything is ok running `streamlit hello`

### Execution

To run the dashboard execute the following command:

```
> streamlit run .\streamlit_dashboard\Welcome.py
# If the command above fails, use:
> python -m streamlit run .\streamlit_dashboard\Welcome.py
```

## Contributors

```
Team Members:  
- Agnes Rehn 
- Alhaan Kasi
- Guilherme Gryschek
- Nchedochukwu Uzoigwe
- Ning Gai
- Sreeja Mohanan Nair

```

The team collaborated through a [GitHub repository](https://github.com/ggryschek/NK_SS_DashBoard).

The [dashboard](https://ggryschek-nk-ss-dashboard-streamlit-dashboardwelcome-eitwpq.streamlit.app/) has been deployed online.

The [portfolio showcasing video](https://www.youtube.com/watch?v=pre50ZaYHNc) has been uploaded to YouTube.
