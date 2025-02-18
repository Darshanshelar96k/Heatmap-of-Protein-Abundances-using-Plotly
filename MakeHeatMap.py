
import pandas as pd
import plotly.express as px
import sys

file_path = sys.argv[1]

# Load data
df = pd.read_excel(file_path)
df.set_index(df.columns[0], inplace=True)

# Convert the data to numeric (handle commas if present)
df = df.applymap(lambda x: float(str(x).replace(',', '')) if isinstance(x, str) else x)

# Create heatmap using Plotly
fig = px.imshow(
    df,
    labels=dict(x="Conditions", y="Proteins", color="Abundance"),
    x=df.columns,
    y=df.index,
    color_continuous_scale='Viridis',
    aspect='auto'  # Ensures the heatmap is not stretched
)

fig.update_layout(
    title='Heatmap of Protein Abundances',
    xaxis_title='Conditions',
    yaxis_title='Proteins',
    height=800  # Adjust height for better visualization
)

fig.show()

