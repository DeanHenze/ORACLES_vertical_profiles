# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 17:05:19 2022

@author: Dean
"""

from flask import Flask, render_template
import xarray as xr
import numpy as np


app = Flask(__name__)


@app.route('/')
def index():
    
    data = xr.load_dataset(
        "./data/wisper_oracles_verticalprofiles_2016.nc", 
        decode_times=False
        )
    
    temperature_prf = data.sel(profile=1)['T'].values
    temperature_prf = temperature_prf[~np.isnan(temperature_prf)]
    
    return render_template('index.html', dataarray=temperature_prf)


if __name__=="__main__":
    app.run(debug=True)
