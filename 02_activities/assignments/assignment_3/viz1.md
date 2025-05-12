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


