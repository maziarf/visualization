Dataset: http://open.toronto.ca/dataset/non-regulated-lead-sample/
Toronto non-regulated Lead sample from Jan 1 2014- Mar 13 2025.

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


