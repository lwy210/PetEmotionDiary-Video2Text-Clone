import os
import pickle

import torch
from autogluon.tabular import TabularDataset, TabularPredictor
from django.apps import AppConfig
from django.conf import settings


class AiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ai"

    # 모델 불러오기
    dog_emotion_predictor = TabularPredictor.load("models/dog_emotion_dir")

    dog_action_predictor = TabularPredictor.load("models/dog_action_dir")

    cat_emotion_predictor = TabularPredictor.load("models/cat_emotion_dir")

    cat_action_predictor = TabularPredictor.load("models/cat_action_dir")

    path = os.path.join(settings.MODELS, "cat_skeleton_model_ep18_1.20.pkl")
    with open(path, "rb") as f:
        cat_skeleton_model = pickle.load(f)

    path = os.path.join(settings.MODELS, "dog_skeleton_model_ep22_1.23.pkl")
    with open(path, "rb") as f:
        dog_skeleton_model = pickle.load(f)

    path = os.path.join(settings.MODELS, "input_df_col_name.pkl")
    with open(path, "rb") as f:
        input_df_col_name = pickle.load(f)

    path = os.path.join(settings.MODELS, "yolov5")
    yolo5s = torch.hub.load(
        path,
        "custom",
        path="yolov5s.pt",
        source="local",
    )
