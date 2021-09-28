from django.shortcuts import render
import plotly.graph_objects as go
from django.http import Http404

fig = go.Figure()
fig.add_trace(go.Bar(x=[1, 3, 4], y=[2, 3, 1]))


fig = fig.to_html(full_html=False)


def index(req):
    return render(req, 'index.html')


def tables(req):
    return render(req, 'tables.html')


def register(req):
    return render(req, 'register.html')


def password(req):
    return render(req, 'password.html')


def login(req):
    return render(req, 'login.html')


def layout_static(req):
    return render(req, 'layout-static.html')


def layout_sidenav_light(req):
    return render(req, 'layout-sidenav-light.html')


def charts(req):
    return render(req, 'charts.html')


def error404handler(req, exception):
    return render(req, '404.html')