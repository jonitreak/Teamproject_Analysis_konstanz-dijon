import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.api import VAR
from scipy.stats import pearsonr
import python_scripts.data_handling.data_handler as dd


# https://github.com/ritvikmath/Time-Series-Analysis/blob/master/VAR%20Model.ipynb
# load data
user_aata = dd.loaData()
