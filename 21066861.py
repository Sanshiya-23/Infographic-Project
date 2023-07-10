import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec

# Load data
fastfood = pd.read_csv(r"C:\Users\SANSHIYA\Downloads\fastfood.csv")

# Set figure size and layout
fig = plt.figure(figsize=(20, 15))
gs = GridSpec(nrows=2, ncols=2, figure=fig)

# Create line graph
ax1 = fig.add_subplot(gs[0, 0])
sns.lineplot(y=fastfood['restaurant'], x=fastfood['calories'], ax=ax1)
ax1.set_title('Fast Food Calorie Count')
ax1.set_xlabel('Calories', fontsize=12)
ax1.set_ylabel('Restaurant', fontsize=12)
ax1.tick_params(labelsize=10)
# Add description
ax1.text(0.05, 0.95, 'SANSHIYA RAMESHKUMAR, 21066861',
         transform=ax1.transAxes, fontsize=20, va='baseline')
# Create histogram
df_Mcd  = fastfood[fastfood['restaurant']=='Mcdonalds']
ax2 = fig.add_subplot(gs[0, 1])
sns.histplot(data=df_Mcd, ax=ax2)
ax2.annotate('Most common calorie count: 500', xy=(500, 10), ha='left', va='center')
ax2.set_title('Overall Analysis in Mcdonalds')
ax2.set_xlabel('Calories', fontsize=12)
ax2.set_ylabel('Count', fontsize=12)
ax2.tick_params(labelsize=10)

# Create bar graph
chick_info = fastfood[fastfood['restaurant'] == 'Chick Fil-A']
ax3 = fig.add_subplot(gs[1, 0])
sns.barplot(y=chick_info['item'], x=fastfood['calories'], ax=ax3)
for index, value in enumerate(fastfood['calories']):
    ax3.annotate(str(value), xy=(value, index), ha='left', va='center')
ax3.set_title('Chick Fil-A Calorie Per Item')
ax3.set_xlabel('Calories', fontsize=12)
ax3.set_ylabel('Item', fontsize=12)
ax3.tick_params(labelsize=10)

# Create box plot
Arbys_info = fastfood[fastfood['restaurant'] == 'Arbys']
ax4 = fig.add_subplot(gs[1, 1])
sns.boxplot(x=Arbys_info['calories'], ax=ax4)
ax4.set_title('Analysis of calorie trends in Arbys', fontsize=16)
ax4.set_xlabel('Calories', fontsize=12)
ax4.set_ylabel('Restaurant', fontsize=12)
ax4.tick_params(labelsize=10)

# Create scatter plot
sonic_info = fastfood[fastfood['restaurant'] == 'Sonic']
fig, ax5 = plt.subplots(figsize=(8, 12))
ax5.scatter(x=sonic_info['calories'], y=sonic_info['item'])

# Add annotations to the scatter plot
for i, txt in enumerate(sonic_info['calories']):
    ax5.annotate(txt, (sonic_info['calories'].iloc[i], sonic_info['item'].iloc[i]))

# Set title and labels
ax5.set_title('Analysis of highest calories in Sonic')
ax5.set_xlabel('Calories', fontsize=12)
ax5.set_ylabel('Item', fontsize=12)
ax5.tick_params(labelsize=10)
# Add legend
ax5.legend(['Calories'])

# Show plot
plt.show()

fig.suptitle('Food Analysis in top restaurant', fontsize=60, fontweight='bold')
fig.tight_layout()
plt.savefig('mental_health_infographic.png', dpi=600)
plt.show()




