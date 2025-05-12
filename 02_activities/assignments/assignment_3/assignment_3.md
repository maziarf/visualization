# Data Visualization

## Assignment 3: Final Project

### Requirements:
- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data. 
- Choose a dataset of interest from the [City of Toronto’s Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario’s Open Data Catalogue](https://data.ontario.ca/). 
- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.  
- For each visualization, describe and justify: 

Dataset: http://open.toronto.ca/dataset/non-regulated-lead-sample/
Toronto non-regulated Lead sample from Jan 1 2014- Mar 13 2025.

**Visualization 1: using Python**
> What software did you use to create your data visualization?
Python's pandas and matplotlib were used in producing this visualization.

> Who is your intended audience? 
Residents of the city of Toronto.

> What information or message are you trying to convey with your visualization? 
The goal is to indicate which neighbourhoods have higher levels of lead detected in their water, informing the residents of the neighbourhood. 

This can be potentially correlated with the distribution of old houses among different neighbourhoods as old houses tend to have a higher usage of lead pipes.     

We plot the number of samples that were submitted for a given partial postal code which contained dangerous amounts of lead (more than 0.005 ppm per Government of Canada), normalized by the total number of samples that were submitted from that partial postal code, filtered by partial postal code ratio of samples (i.e. normalized number of samples) that were bigger than 0.5 percent considered as a significance threshold. We plotted the histogram of this distribution grouped by partial postal codes ordered lexicographically. 
We normalize by the total number of submitted samples for each partial postal code since the raw number of samples is skewed if a particular partial postal code neighbourhood submits samples to be evaluated more than others, possibly due to having higher awareness, neighbourhood initiatives, or more free time. 

Partial postal codes that do not show up should not necessarily be considered safe since it can be the case that that particular neighbourhood did not submit a sample at all. In other words, since the samples are submitted voluntarily by the residents, this dataset might suffer from selection bias.  

> What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
I mainly used color to group near neighbourhoods, and bar to show the amount (so length of the bar indicating the ratio of the number of detected samples).     


> How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
I made sure to clean the data automatically in the code instead of changing the data file manually to ensure reproducibility. Of course, having produced the plot programmatically is also very important.

> How did you ensure that your data visualization is accessible?  
I made sure to use viridis for the colormap. I used sans-serif for the font. Both of these choices are color-blind friendly. I also tried to use large enough font and the proper image size for clear visibility.

> Who are the individuals and communities who might be impacted by your visualization?  
Residents of Toronto might be impacted by this visualization. The presentation aspect of this data could advocate for those neighbourhoods with dangerous amounts of lead in their water. 

> How did you choose which features of your chosen dataset to include or exclude from your visualization? 
My main goal for this visualization was to extract only the information that could be useful to citizens of Toronto. 
I decided to only include the features (i.e. the dangerous level of lead in samples). Therefore, the insignificant detected amounts were excluded.

> What ‘underwater labour’ contributed to your final data visualization product?
The production, distribution, and analysis of lead sample kits relies on essential labour of many workers including those working for the city of Toronto and the postal services, without whom this data visualization would not have been possible. 




**Visualization 2: using Excel**

> What software did you use to create your data visualization?
I used Google Sheets (Excel).

> Who is your intended audience? 
Residents of the city of Toronto's M4J postal code area.

> What information or message are you trying to convey with your visualization? 
The message is that disregarding outlier samples, the total amount of lead detected in M4J's water has been decreasing over time. This is the neighbourhood with the highest number of samples submitted for analysis over all neighbourhoods in Toronto which participated in this program. This can potentially indicate the benefit of this program, indicating a correlation between the feedback that the city provides about lead levels. 

Particularly, we have first found the neighbourhood postal code with the highest number of sample entries, which is M4J. Then, we filtered for amounts lead sample amounts bigger than 0.00006 ppm (inclusively above which is measurement-wise significant) and smaller than 0.5 ppm (for the few values larger than this amount we have deemed them as outliers). Finally, we binned the total amount of detected lead (ppm) over half year periods, and plotted this.




> What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
In this graph, the bar size is used to show the amount of detected lead (so length of the bar indicates the amount of lead in detected samples).      


> How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
I tried to use Excel conditional statements whenever possible to filter, but the results are not really reproducible. This can cause problem for others who might want to see if the result I have come up with actually withstands scrutiny. 

> How did you ensure that your data visualization is accessible?  
I made sure to use color schemes that are colorblind-friendly, and used sans-serif font. I also made sure that my font-size are not too small, and to use black font. 

> Who are the individuals and communities who might be impacted by your visualization?  
Residents of Toronto's M4J neighbourhood might be impacted by this visualization. It can also benefit other communities in the city, learning that there is a correlation between lead amount detected in their water and potentially taking steps to decrease the lead amount in the water.

> How did you choose which features of your chosen dataset to include or exclude from your visualization? 
I used heuristics to exclude outliers in the lead amount, whereby using statistical inference methods would have been more robust. Otherwise, I chose the neighbourhood with the highest number of samples submitted to have a more representative sample of the water quality of a neighbourhood. 

> What ‘underwater labour’ contributed to your final data visualization product?
This is the same as the previous answer. The production, distribution, and analysis of lead sample kits relies on essential labour of many workers including those working for the city of Toronto and the postal services, without whom this data visualization would not have been possible. 





- This assignment is intentionally open-ended - you are free to create static or dynamic data visualizations, maps, or whatever form of data visualization you think best communicates your information to your audience of choice! 
- Total word count should not exceed **(as a maximum) 1000 words** 
 
### Why am I doing this assignment?:  
- This ongoing assignment ensures active participation in the course, and assesses the learning outcomes: 
* Create and customize data visualizations from start to finish in Python
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story  
- This would be a great project to include in your GitHub Portfolio – put in the effort to make it something worthy of showing prospective employers!

### Rubric:

| Component         | Scoring  | Requirement                                                                 |
|-------------------|----------|-----------------------------------------------------------------------------|
| Data Visualizations | Complete/Incomplete | - Data visualizations are distinct from each other<br>- Data visualizations are clearly identified<br>- Different sources/rationales (text with two images of data, if visualizations are labeled)<br>- High-quality visuals (high resolution and clear data)<br>- Data visualizations follow best practices of accessibility |
| Written Explanations | Complete/Incomplete | - All questions from assignment description are answered for each visualization<br>- Explanations are supported by course content or scholarly sources, where needed |
| Code              | Complete/Incomplete | - All code is included as an appendix with your final submissions<br>- Code is clearly commented and reproducible |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 09/05/2025`
* The branch name for your repo should be: `assignment-3`
* What to submit for this assignment:
    * A folder/directory containing:
        * This file (assignment_3.md)
        * Two data visualizations 
        * Two markdown files for each both visualizations with their written descriptions.
        * Link to your dataset of choice.
        * Complete and commented code as an appendix (for your visualization made with Python, and for the other, if relevant) 
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-3`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
