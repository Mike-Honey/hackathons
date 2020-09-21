# CSDC - The COVID-19 Symptom Data Challenge

https://www.symptomchallenge.org/

This CSDC dataset is broad - this solution is focussed on the non-US dataset of survey data produced by University of Maryland (UMD). It is described in detail at the link above.

**Team Information:**

Mike Honey leads a data visualization consultancy: [Manga Solutions](https://www.mangasolutions.com). He works with a global portfolio of clients across the healthcare, conservation, social change, finance and education sectors.

**Approach:**

As the dataset is vast and complex, the aim of this solution is to empower those with public health expertise to easily explore and analyse interactively. Power BI is an interactive tool, so an untrained user can use the report pages to explore almost any aspect of the dataset, using just a web browser, with response times in seconds. 

In data science terms, this might be called an "Exploratory Data Analysis" (EDA), but this solution offers a far broader scope than could ever be achieved with a custom-coded EDA. 

**Relevance to COVID-19 disease control policy and practice:**

Experience across many scenarios and domains has shown that when subject-matter experts are freed to explore a complex dataset using this approach, they can quickly find meaningful insights or be inspired to dig deeper.  Domain experts in public health can quickly compare and contrast survey results from any slice of the survey dataset, helping them quickly understand reported trends.

**Approach:**

This solution combines a python script to download the dataset (large CSV files, nested web folders), and a Power BI dataset and report for data transformation and analysis.

The Power BI data transformation approach is to standardise the variations of column names presented into the survey's core list of signals, with attributes to indicate the source. 

For example the column **pct_cli_weighted** from files in the **smoothed** subfolder is presented as:
- Signal: COVID-19-like illness
- Is Weighted: Weighted
- Is Smoothed: Smoothed

This allows a minimal set of visualisation pages to cover all the complexity of the dataset, where the audience can use interactive "Slicers" e.g. to instantly switch between smoothed and raw signal results.  

As the solution code settles, more of the historical data will be added. This solution will also be refreshed as further (more recent) data is released.

[Link to interactive DataViz](https://app.powerbi.com/view?r=eyJrIjoiZGYxZTAyZTktOGE2Yi00Mjc5LWIzMGMtNzRkMDU1ZTY1NTNhIiwidCI6ImRjMWYwNGY1LWMxZTUtNDQyOS1hODEyLTU3OTNiZTQ1YmY5ZCIsImMiOjEwfQ%3D%3D)

Note page navigation controls are at the bottom, e.g. < 1 of 5 >
