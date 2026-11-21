import numpy as np
from src.model_training import train_model


def test_model_training():
    model, mae, rmse, r2 = train_model()

    assert model is not None
    assert mae >= 0
    assert rmse >= 0
    assert np.isfinite(r2)


def test_model_prediction():
    model, mae, rmse, r2 = train_model()

    prediction = model.predict([[1500, 3]])

    assert len(prediction) == 1
    assert prediction[0] > 0
