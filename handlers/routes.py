import joblib
import zipfile
import os
from flask import Flask, render_template, request
import numpy as np


def index():
    if request.method == "POST":
        attributes = [
            'movement_reactions', 'mentality_composure', 'passing',
            'release_clause_eur', 'dribbling', 'wage_eur', 'power_shot_power',
            'value_eur', 'mentality_vision', 'attacking_short_passing',
            'physic', 'skill_long_passing', 'age'
        ]

        input_data = {}
        for attr in attributes:
            value = float(request.form.get(attr, 0))
            input_data[attr] = value

        prediction = ensemble.predict([list(input_data.values())])
        prediction = round(prediction[0])

        return render_template("result.html", prediction=prediction)

    return render_template("form.html")
