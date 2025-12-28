from abc import ABC, abstractmethod
from typing import List, Dict, Any, Type
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


class LLMOutput(BaseModel):
    text: str
    parsed: BaseModel | None = None


class BaseFileGenerator(ABC):
    """Abstract base class for all file generators."""

    def __init__(self, model: str = "gpt-4.1"):
        self.model = model

    @abstractmethod
    def generate_file(self, **kwargs):
        pass

    def call_llm(self, input: str, output_format: Type[BaseModel] | None = None) -> str | BaseModel:
        """Call the OpenAI API with an input and return the content."""

        if output_format:
            parsed = client.responses.parse(model=self.model, input=input, text_format=output_format).output_parsed
            return LLMOutput(text="", parsed=parsed)

        else:
            text = client.responses.create(model=self.model, input=input).output_text
            return LLMOutput(text=text)

    