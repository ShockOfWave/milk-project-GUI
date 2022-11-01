import numpy as np
import pandas as pd
from catboost import CatBoostClassifier, CatBoostRegressor
from MilkApp.paths.paths import *

class Catboost_evaluations:
    def __init__(self, device, path_to_model, current):
        self.device = device
        self.current = current
        self.binary_prediction = None
        self.multi_prediction = None
        self.full_prediction = None
        self.regression_prediction = None
        self.regression_prediction_full = None
        self.path_to_model = path_to_model
        self.binary, self.multi = self.list_of_models()
        self.model_classifier_binary = CatBoostClassifier()
        self.model_classifier_multi = CatBoostClassifier()
        self.load_models()

    def list_of_models(self):
        self.binary = os.path.join(self.path_to_model, 'catboost_binary')
        self.multi = os.path.join(self.path_to_model, 'catboost_multi')
        return self.binary, self.multi


    def load_models(self):
        self.model_classifier_binary.load_model(self.binary)
        self.model_classifier_multi.load_model(self.multi)

    def predict_class(self):
        self.binary_prediction = self.model_classifier_binary.predict(self.current)
        self.multi_prediction = self.model_classifier_multi.predict(self.current)[0]