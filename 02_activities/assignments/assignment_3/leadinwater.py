import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as plt_colors
import matplotlib.patches as mpatches

# load the csv dataset file
data_df = pd.read_csv('Non_Regulated_Lead_Samples.csv')

# clean the lead amount column using regex,
# to have measurement-wise insignificant values set to 0
# these values started with a less than sign.
sample_amount_clmn = data_df['Lead Amount (ppm)'].replace(r'<.*', '0', regex=True)

# convert the lead amount values to numeric type float64.
sample_amount_clmn = pd.to_numeric(sample_amount_clmn)


# Only considering dangerous lead amounts per Government of Canada's standard,
# which is more than 0.005 ppm 
# https://www.canada.ca/en/health-canada/services/environmental-workplace-health/environmental-contaminants/lead/lead-information-package-some-commonly-asked-questions-about-lead-human-health.html#a2https://www.canada.ca/en/health-canada/services/environmental-workplace-health/environmental-contaminants/lead/lead-information-package-some-commonly-asked-questions-about-lead-human-health.html#a2
significant_samples = data_df[sample_amount_clmn>0.005]

# counts of dangerous samples grouped by partial postal codes
sig_counts = significant_samples['PartialPostalCode'].value_counts()

# counts of total submitted samples grouped by partial postal codes
tot_counts = data_df['PartialPostalCode'].value_counts()

# normalizing counts of dangerous samples by the total number of samples
# from a given partial postal code
ratio_counts = sig_counts/tot_counts

# only considering ratios bigger than 0.5 percent, 
# in order to have only signifantly dangerous partial postal codes
# shown on the graph, in order to remove very small ratios.
ratio_counts_sig = ratio_counts[ratio_counts>0.005]


# Group partial postal codes with the same initial letter and number by color
# to indicate neighbourhood proximity
## first two letter-numbers e.g. M1
first_two_alpha = ratio_counts_sig.index.str[:2]

##sorted unique first two letter-numbers
unique_first_two = sorted(first_two_alpha.unique())

## producing the color map
cmap = plt.colormaps.get_cmap('viridis')
color_map = {}
for i, first_two in enumerate(unique_first_two):
    #normalize index
    value_ = cmap(i/(len(unique_first_two)-1))
    color_map[first_two] = value_

bar_colors = first_two_alpha.map(color_map)


legend_handles = [mpatches.Patch(color=color_, label=first_2_letts) for first_2_letts, color_ in color_map.items()]

#producing the plot as a histogram
plt.figure(figsize=(15,9))
ratio_counts_sig.sort_index().plot(
    kind= 'bar',
    color=bar_colors
)
plt.title('Toronto Neighbourhoods water samples with dangerous amount of lead',fontdict={'family':'sans-serif', 'fontsize':16})

axis_font_dict ={'family':'sans-serif', 'fontsize':12}
plt.xlabel('Partial Postal Code',fontdict=axis_font_dict)
plt.ylabel('ratio of number of dangerous samples',fontdict=axis_font_dict)

plt.xticks(fontsize =10, family = 'sans-serif')


plt.legend(handles=legend_handles,title ='Postal Code Starting with',bbox_to_anchor = (1,1), loc=  'upper right')


plt.tight_layout()

plt.savefig('python_output_dangerous_lead.png',dpi=600, bbox_inches = 'tight')
plt.show()
