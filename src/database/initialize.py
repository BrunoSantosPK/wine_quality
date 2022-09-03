import pandas as pd
from typing import Tuple
from src.models.base import Base
from src.models.wine_result import WineResult
from src.database.connection import get_engine, get_session


class Initialize:
    
    @staticmethod
    def wine_data_from_csv(base_path: str) -> Tuple[bool, str]:
        success, message = True, "Carga do csv realizada com sucesso"

        try:
            dataset = pd.read_csv(f"{base_path}/data/winequality-red.csv")
            session = get_session()
            insert = []

            for i in range(0, len(dataset)):
                insert.append(WineResult(
                    quality=dataset["quality"].values[i],
                    fixed_acidity=dataset["fixed acidity"].values[i],
                    volatile_acidity=dataset["volatile acidity"].values[i],
                    citric_acid=dataset["citric acid"].values[i],
                    residual_sugar=dataset["residual sugar"].values[i],
                    chlorides=dataset["chlorides"].values[i],
                    free_sulfur_dioxide=dataset["free sulfur dioxide"].values[i],
                    total_sulfur_dioxide=dataset["total sulfur dioxide"].values[i],
                    density=dataset["density"].values[i],
                    ph=dataset["pH"].values[i],
                    sulphates=dataset["sulphates"].values[i],
                    alcohol=dataset["alcohol"].values[i]
                ))

            session.add_all(insert)
            session.commit()
            
        except BaseException as e:
            success, message = False, str(e)
            session.rollback()

        finally:
            session.close()
            return success, message

    @staticmethod
    def create_database() -> Tuple[bool, str]:
        try:
            Base.metadata.create_all(get_engine())
            return True, "Tabelas criadas com sucesso."
        except BaseException as e:
            return False, str(e)

    @staticmethod
    def drop_database() -> Tuple[bool, str]:
        try:
            Base.metadata.drop_all(get_engine())
            return True, "Tabelas removidas com sucesso."
        except BaseException as e:
            return False, str(e)
