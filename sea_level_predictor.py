import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
   
    # Create scatter plot
    plt.scatter(
        x='Year',
        y='CSIRO Adjusted Sea Level',
        data=df
    )
    rs1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Create first line of best fit
    x1 = range(df['Year'].min(), 2051)
    plt.plot(x1, rs1.intercept + rs1.slope*x1,color='blue', label='Line 1')

    # Create second line of best fit
    recent_year = df[df['Year'] >= 2000]
    rs2 = linregress(recent_year['Year'], recent_year['CSIRO Adjusted Sea Level'])
    x2 = range(2000, 2051)
    plt.plot(x2, rs2.intercept + rs2.slope*x2,color='red', label='Line 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()