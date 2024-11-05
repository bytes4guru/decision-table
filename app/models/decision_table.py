from __future__ import annotations  # Only needed for Python 3.7-3.9 compatibility
import csv
from pathlib import Path
from app.models.abstract import AbstractDecisionTable
from app.models.condition import Condition
from app.models.decision_data_holder import DecisionDataHolder
from typing import Any


class DecisionTable(AbstractDecisionTable):
    def __init__(self, csv_file_path: Path):
        self.rows: list[tuple[list[Condition], dict[str, str]]] = []
        self.load_table(csv_file_path)

    @staticmethod
    def create_from_csv(filepath: Path) -> DecisionTable:
        return DecisionTable(filepath)

    def load_table(self, csv_file_path: Path) -> None:
        with open(csv_file_path, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            headers = next(reader)

            for row in reader:
                input_conditions = []
                output = {}

                for i, cell in enumerate(row):
                    column_name = headers[i]

                    # Parsing based on position in the table (inputs vs outputs)
                    if column_name == "*":
                        continue
                    elif i < headers.index("*"):  # Input columns
                        input_conditions.append(self.parse_condition(column_name, cell))
                    else:  # Output column
                        output[column_name] = cell.strip('"')

                self.rows.append((input_conditions, output))

    def parse_condition(self, column_name: str, cell_value: str) -> Condition:
        if ">=" in cell_value:
            return Condition(column_name, ">=", float(cell_value[2:]))
        elif "<=" in cell_value:
            return Condition(column_name, "<=", float(cell_value[2:]))
        elif ">" in cell_value:
            return Condition(column_name, ">", float(cell_value[1:]))
        elif "<" in cell_value:
            return Condition(column_name, "<", float(cell_value[1:]))
        elif "=" in cell_value:
            value: Any = cell_value[1:]
            if value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
            else:
                value = int(value)
            return Condition(column_name, "=", value)
        else:
            raise ValueError(f"Unsupported condition format: {cell_value}")

    def evaluate(self, data_holder: DecisionDataHolder) -> bool:
        for conditions, output in self.rows:
            if all(condition.evaluate(data_holder) for condition in conditions):
                # Apply output to data_holder and stop
                for key, value in output.items():
                    data_holder[key] = value
                break
        return True
