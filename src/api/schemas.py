from pydantic import BaseModel, Field
from typing import Literal


class FileGenerationRequest(BaseModel):
    """
    Input schema for file generation API.
    """
    file_type: Literal["docx", "excel"] = Field(
        ...,
        description="Type of file to generate (e.g. 'docx', 'excel')"
    )
    instructions: str = Field(
        ...,
        description="Natural language instructions describing the file content"
    )
