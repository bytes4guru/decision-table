from app.models.decision_data_holder import DecisionDataHolder
from typing import Any


class Condition:
    def __init__(self, predictor: str, operator: str, value: Any):
        self.predictor = predictor
        self.operator = operator
        self.value = value

    def evaluate(self, data_holder: DecisionDataHolder) -> bool:
        actual_value = data_holder.get(self.predictor)

        if self.operator == "=":
            return actual_value == self.value
        elif self.operator == ">":
            return actual_value > self.value
        elif self.operator == "<":
            return actual_value < self.value
        elif self.operator == ">=":
            return actual_value >= self.value
        elif self.operator == "<=":
            return actual_value <= self.value
        else:
            raise ValueError(f"Unsupported operator {self.operator}")
