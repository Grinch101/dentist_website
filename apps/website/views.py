from django.shortcuts import render
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Bar(x=[1,3,4],y=[2,3,1]))
fig = fig.to_html(full_html=False)
# Create your views here.
def index(req):
    return render(req,'index.html', {'myFig':fig})
