from typing import Literal

import pandas as pd
from pydantic import BaseModel

from .base_file_generator import BaseFileGenerator
from src.prompts.excel_file_generation_prompts import excel_planner_prompt


class CreateSheetArgs(BaseModel):
    sheet_name: str


class CreateTableArgs(BaseModel):
    sheet_name: str
    table_name: str
    columns: list[str]
    rows: list[list[str | int | float]]


class CreateSheetStep(BaseModel):
    function: Literal["create_sheet"]
    args: CreateSheetArgs


class CreateTableStep(BaseModel):
    function: Literal["create_table"]
    args: CreateTableArgs


class ExcelOutputStructure(BaseModel):
    steps: list[CreateSheetStep | CreateTableStep]


class ExcelFileGenerator(BaseFileGenerator):
    def __init__(self, model: str = "gpt-4.1"):
        super().__init__(model)
        self.writer: pd.ExcelWriter | None = None
        self.sheets: dict[str, pd.DataFrame] = {}

    def generate_file(self, input: str, output_path: str) -> str:
        plan = self.generate_plan(input)

        with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
            self.writer = writer
            self.execute_plan(plan)

        return output_path


    def generate_plan(self, user_prompt: str) -> ExcelOutputStructure:
        """Convert the user prompt directly into a structured execution plan."""
        return self.call_llm(
            input=excel_planner_prompt.format(user_prompt=user_prompt),
            output_format=ExcelOutputStructure,
        ).parsed


    def execute_plan(self, plan: ExcelOutputStructure):
        for step in plan.steps:
            getattr(self, step.function)(**step.args.model_dump())


    def create_sheet(self, sheet_name: str):
        if sheet_name not in self.sheets:
            df = pd.DataFrame()
            df.to_excel(self.writer, sheet_name=sheet_name, index=False)
            self.sheets[sheet_name] = df

    def create_table(
        self,
        sheet_name: str,
        table_name: str,
        columns: list[str],
        rows: list[list[str | int | float]],
    ):
        df = pd.DataFrame(rows, columns=columns)

        df.to_excel(
            self.writer,
            sheet_name=sheet_name,
            startrow=0,
            startcol=0,
            index=False,
        )

        self.sheets[sheet_name] = df
