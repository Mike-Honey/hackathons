# The COVID-19 Symptom Data Challenge (CSDC) - EDA solution

[Link to interactive DataViz](https://app.powerbi.com/view?r=eyJrIjoiZGYxZTAyZTktOGE2Yi00Mjc5LWIzMGMtNzRkMDU1ZTY1NTNhIiwidCI6ImRjMWYwNGY1LWMxZTUtNDQyOS1hODEyLTU3OTNiZTQ1YmY5ZCIsImMiOjEwfQ%3D%3D)

Note page navigation controls are at the bottom, e.g. < 1 of 5 >

**Data sources:**

https://www.symptomchallenge.org/

This CSDC dataset is broad - this solution is focussed on the non-US dataset of survey data produced by University of Maryland (UMD). It is described in detail at the link above.  The codebook presented on that site is used to translate the dataset structures into easy-to-read attributes.

**Team Information:**

Mike Honey leads a data visualization consultancy: [Manga Solutions](https://www.mangasolutions.com). He works with a global portfolio of clients across the healthcare, conservation, social change, finance and education sectors.

**Approach:**

As the dataset is vast and complex, the aim of this solution is to empower those with public health expertise to easily explore and analyse interactively. Power BI is an interactive tool, so an untrained user can use the report pages to explore almost any aspect of the dataset, using just a web browser, with response times in seconds. 

In data science terms, this might be called an "Exploratory Data Analysis" (EDA), but this solution offers a far broader scope than could ever be achieved with a custom-coded EDA. 

**Relevance to COVID-19 disease control policy and practice:**

Experience across many scenarios and domains has shown that when subject-matter experts are freed to explore a complex dataset using this approach, they can quickly find meaningful insights or be inspired to dig deeper.  Domain experts in public health can quickly compare and contrast survey results from any slice of the survey dataset, helping them quickly understand reported trends.

Use of a fully interactive data visualisation platform gives the opportunity for the broadest possible audience to engage and understand the survey data.  They do not need any technical understanding of the survey's data structure, or any knowledge of visualisation coding or tools.   

**Methods:**

This solution combines a python script to download the dataset (large CSV files, nested web folders), and a Power BI dataset and report for data transformation and analysis.

[Power BI](powerbi.com) is probably the leading data visualisation tool in use today, with over 2.5m users. It has impressive data integration and query capabilities, and provides intuitive, responsive data visualisation results to an untrained audience via a web browser. It includes a free development tool "Power BI Desktop", and solutions like this can be published and shared from a free online account. 

The Power BI data transformation approach used was to standardise the variations of column names presented into the survey's core list of signals, with attributes added to indicate the specific data source. Technical column names are translated into terms which are less likely to need interpretation by the audience.  The source info for the column names was the "codebook" provided, with some transformation steps to achieve concise, yet easy-to-read attributes.

For example the column **pct_cli_weighted** from files in the **smoothed** subfolder is presented as:
- Signal: **COVID-19-like illness**
- Is Weighted: **weighted**
- Is Smoothed: **smoothed**

This allows a minimal set of visualisation pages to cover all the complexity of the dataset. The audience can use interactive "Slicers" e.g. to instantly switch between smoothed and raw signal results, switch or compare Signals and so on.    

As the solution code settles, more of the historical data will be added. This solution will also be refreshed as further (more recent) data is released.

**Results**

The UMD dataset from June onwards is presented in it's entirety. Results are available for every country and region, for the entire date range or any subset, for every signal, every demographic attribute (age bucket or gender), and every calculation method (smoothed or not, weighted or not).

The data gathered is presented in 6 pages of a Power BI report:
- **EDA - Region, Country Time Series** - choose any Signal, then choose any collection of Countries or Regions to generate a time series (line chart). Additional slicers support filtering by Date range, Age Bucket, Gender, Is Weighted or Is Smoothed.  

**Discussion**

**Relevant figures and graphs**

**Discussion and 10 slide presentation**

**Github link**
[https://github.com/Mike-Honey/hackathons/CSDC/](https://github.com/Mike-Honey/hackathons/CSDC/)

**Website link**
[Link to interactive DataViz](https://app.powerbi.com/view?r=eyJrIjoiZGYxZTAyZTktOGE2Yi00Mjc5LWIzMGMtNzRkMDU1ZTY1NTNhIiwidCI6ImRjMWYwNGY1LWMxZTUtNDQyOS1hODEyLTU3OTNiZTQ1YmY5ZCIsImMiOjEwfQ%3D%3D)

Note page navigation controls are at the bottom, e.g. < 1 of 5 >
