import json
import joblib
from flask import request


class ControllerPredict:

    @staticmethod
    def predict(base_path: str) -> str:
        result = {"success": True, "message": ""}

        try:
            # Carrega modelos e dados para input da previsão
            classifier = joblib.load(f"{base_path}/data/model.joblib")
            scaler = joblib.load(f"{base_path}/data/scaler.joblib")
            body = json.loads(request.data)
            data_input = [[
                body["volatile_acidity"],
                body["citric_acid"],
                body["free_sulfur_dioxide"],
                body["alcohol"]
            ]]

            # Realiza previsão e envia a resposta para o cliente
            data_input = scaler.transform(data_input)
            data_predict = classifier.predict(data_input)
            result["quality"] = data_predict[0]

        except BaseException as e:
            result["success"] = False
            result["message"] = str(e)

        finally:
            return json.dumps(result)
