import pickle
import warnings
import shap

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from flask import Flask, request, jsonify
warnings.filterwarnings("ignore")

app = Flask(__name__)

with open('banking_model20.md', 'rb') as f:
    banking_model = pickle.load(f)

with open('Explainer.md', 'rb') as f:
    explainer = pickle.load(f)


def plot_shap_bar(sv, name='../image/test.png',
                  adjust_left=0.35):
    fig = plt.figure()
    shap.plots.bar(sv[0], show=False)
    plt.gcf().set_size_inches(15,6)
    fig.subplots_adjust(left=adjust_left)
    plt.savefig(name)


@app.route('/solvabilite',methods=['POST','GET'])
def solvabilite():
    data=request.json
    data=pd.DataFrame(data, index=[0])

    result = dict()
    result['predict_proba'] = banking_model.predict_proba(data).tolist()[0]
    result['predict'] = banking_model.predict(data).tolist()
    
    shap_value = explainer(data, check_additivity=False)
    plot_shap_bar(shap_value)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
