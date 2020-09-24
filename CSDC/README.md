# CSDC Global Explorer

[Link to interactive DataViz](https://app.powerbi.com/view?r=eyJrIjoiZGYxZTAyZTktOGE2Yi00Mjc5LWIzMGMtNzRkMDU1ZTY1NTNhIiwidCI6ImRjMWYwNGY1LWMxZTUtNDQyOS1hODEyLTU3OTNiZTQ1YmY5ZCIsImMiOjEwfQ%3D%3D)

Note page navigation controls are at the bottom, e.g. < 1 of 6 >


**Data sources:**

The COVID-19 Symptom Data Challenge (CSDC):

https://www.symptomchallenge.org/

This CSDC dataset is broad - this solution is focussed on the Global (non-US) dataset of survey data produced by University of Maryland (UMD). It is described in detail at the link above.  The codebook presented on that site is used to translate the dataset structures into easy-to-read attributes.


**Team Information:**

[Mike Honey](https://www.linkedin.com/in/mikehoney/) leads a data visualization consultancy: [Manga Solutions](https://www.mangasolutions.com). He works with a global portfolio of clients across the healthcare, conservation, social change, finance and education sectors. He draws on 20+ years of experience implementing data integration and data visualization solutions. He was recently awarded a prize by Kaggle for his contribution on the [COVID-19 Open Research Dataset Challenge (CORD-19)](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge), and is an active member of the [CoronaWhy](www.coronawhy.org) data science community.


**Approach:**

As the dataset is vast and complex, the aim of the **CSDC Global Explorer** solution is to empower those with public health expertise to easily explore and analyse interactively. Power BI is an interactive tool, so an untrained user can use the report pages to explore almost any aspect of the dataset, using just a web browser, with response times in seconds. 

In data science terms, this might be called an "Exploratory Data Analysis" (EDA), but this solution offers a far broader scope than could ever be achieved with a custom-coded EDA. 


**Relevance to COVID-19 disease control policy and practice:**

Experience across many scenarios and domains has shown that when subject-matter experts are freed to explore a complex dataset using this approach, they can quickly find meaningful insights or be inspired to dig deeper.  Domain experts in public health can quickly compare and contrast survey results from any slice of the survey dataset, helping them quickly understand reported trends.

Use of a fully interactive data visualization platform gives the opportunity for the broadest possible audience to engage and understand the survey data.  They do not need any technical understanding of the survey's data structure, or any knowledge of visualization coding or tools.   


**Methods:**

This solution combines a python script to download the dataset (large CSV files, nested web folders), and a Power BI dataset and report for data transformation and analysis.

[Power BI](powerbi.com) is probably the leading data visualization tool in use today, with over 2.5m users. It has impressive data integration and query capabilities, and provides intuitive, responsive data visualization results to an untrained audience via a web browser. It includes a free development tool "Power BI Desktop", and solutions like this can be published and shared from a free online account. 

The Power BI data transformation approach used was to standardise the variations of column names presented into the survey's core list of signals, with attributes added to indicate the specific data source. Technical column names are translated into terms which are less likely to need interpretation by the audience.  The source info for the column names was the "codebook" provided, with some transformation steps to achieve concise, yet easy-to-read attributes.

For example the column **smoothed_pct_cli_weighted** is presented as attributes:
- Signal: **COVID-19-like illness**
- Is Weighted: **weighted**
- Is Smoothed: **smoothed**

This allows a minimal set of visualization pages to cover all the complexity of the dataset. The audience can use interactive "Slicers" e.g. to instantly switch between smoothed and raw signal results, switch or compare Signals and so on.  The "sync slicers" feature is used extensively to pass each user's slicer selections across the pages, where appropriate. For example if a particular date range is specified using the slicer on one page, all the other pages will automatically synchronize to that same date range.  This provides a smooth and consistent user experience. Refreshing the web browser or closing and re-entering the link will restore all the default selections.

Some sets of the survey signals are understood to be ["Likert scale"](https://en.wikipedia.org/wiki/Likert_scale), and can be considered together. For example there are 4 questions that categorise whether the respondent is worried they are ill with COVID-19. Likert scale questions are tagged by their set during the data integration, and a specific page was designed to appropriately present them.

As the solution code settles, more of the historical data will be added. This solution will also be refreshed as further (more recent) data is released.


**Results**

The UMD Global dataset from June onwards is presented in it's entirety in the **CSDC Global Explorer**. Results are available for every country and region, for the entire date range or any subset, for every signal, every demographic attribute (age bucket or gender), and every calculation method (smoothed or not, weighted or not).

The data gathered is presented in 6 pages of a Power BI report:
1. **Region, Country Time Series** - choose any Signal, then choose any collection of Countries or Regions to generate a time series (line chart). Each series/line represents a Country or Region. Additional slicers support filtering by Date range, Age Bucket, Gender, Is Weighted or Is Smoothed.  
2. **Region, Country Scatter** - choose any 2 Signals: Y-axis and X-Axis, then choose any collection of Countries or Regions to generate a scatter/bubble chart. Each bubble represents a country or region, sized for the number of respondents (for Y-axis Signal). The chart initially shows the last data avaialable. A **play** control at the bottom can be used to animate by day, or can be dragged to a specific date. Selecting a bubble (or it's entry in the legend) highlights the track of that series over time. Additional slicers support filtering by Date range, Age Bucket, Gender, Is Weighted or Is Smoothed.  
3. **Signal Time Series** - choose any collection of Signals, then choose a Country or Region to generate a time series (line chart). Each series/line represents a Signal. Additional slicers support filtering by Date range, Age Bucket, Gender, Is Weighted or Is Smoothed.  
4. **Likert Signals** - choose any collection of Likert scale Signals (e.g. "mask use"), then choose a Country or Region to generate a time series (column chart). Each series represents a specific Signal, sorted in order of their Likert scale sequence. Additional slicers support filtering by Date range, Age Bucket, Gender, Is Weighted or Is Smoothed.  The raw signal results typically add to 100% for a single date, but smoothed and weighted results may not, as a result of the calculations applied by the survey publishers.
5. **Age Time Series** - choose any Signal, then choose a Country or Region to generate a time series (line chart). Each series/line represents an Age Bucket, including the "overall" bucket. Additional slicers support filtering by Date range, Age Bucket, Gender, Is Weighted or Is Smoothed.  
6. **Gender Time Series** - choose any Signal, then choose a Country or Region to generate a time series (line chart). Each series/line represents a Gender, including the "overall" category. Additional slicers support filtering by Date range, Age Bucket, Gender, Is Weighted or Is Smoothed.  


**Discussion**

The CSDC datasets represent an exciting opportunity for a rich variety of analysis and understanding on topics relating to public health and the urgent COVID-19 challenge faced around the world. However a typical file for a single month and single aggregation method will present hundreds of columns and 250,000+ rows (100+MB CSV). Data at that scale and complexity is very challenging to analyze using traditional data science tools like python. Authors using those tools will tend to take narrow scopes of particular slices of data, missing adjacent features and relying on assumptions.  The set of authors who can produce useful results will unfortunately be narrow, as results require significant skills, compute resources and time.  Their results will be similarly difficult for others to understand and reproduce.

By contrast, the **CSDC Global Explorer** solution offers interactive visualization built on a solid data integration platform capable of delivering instant results at scale. Multiple audiences can explore the visualizations offered with great flexibility to tune and refine what slice of the dataset they want to explore.  The need only a web browser for instant access - the interface is simple and intuitive.  The deployment infrastructure used is a massive global cloud service, provided for free by Microsoft. 

Therefore this solution can engage and inform a far broader set of subject matter experts, skilled in public health and with local knowledge, but perhaps lacking the skills, resources and time to interrogate the dataset using traditional data science tools.


**Relevant figures and graphs**

For sample output, refer to either the slide presentation or Website link (below).

The Power BI report file includes daily data spanning over 3 months, for the intersection of:
- 53 Signals
- 1,793 Region & Country combinations
- 4 Age Buckets
- 4 Gender classifications
- With or without Smoothing
- With or without Weighting

In total there were over 127m individual observations collected. This is stored in a Power BI Report file (PBIX format) of just over 250MB.  That was published to the Power BI Web service (www.powerbi.com) and shared using the "Publish to Web" feature (free shared infrastructure).


**Discussion and 10 slide presentation**


**Github link**
[https://github.com/Mike-Honey/hackathons/CSDC/](https://github.com/Mike-Honey/hackathons/CSDC/)

**Website link**
[Link to interactive DataViz](https://app.powerbi.com/view?r=eyJrIjoiZGYxZTAyZTktOGE2Yi00Mjc5LWIzMGMtNzRkMDU1ZTY1NTNhIiwidCI6ImRjMWYwNGY1LWMxZTUtNDQyOS1hODEyLTU3OTNiZTQ1YmY5ZCIsImMiOjEwfQ%3D%3D)

Note page navigation controls are at the bottom, e.g. < 1 of 6 >
