#Pie chart for the devolution formula of the 15th FC
import plotly.graph_objects as go
fig=go.Figure(go.Pie(labels=["Forest and Ecology","Income Distance","Area","Population","Demographic performanc","Tax and Fiscal Efforts"],values=[10,45,15,15,12.5,2.5]))
# Add titles
fig.update_layout(
    title='Devolution Formula for the 15th FC'
)
fig.show()
