import os
import tempfile
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from src.api.schemas import FileGenerationRequest
from src.generators.docx_file_generator import DocxFileGenerator
from src.generators.excel_file_generator import ExcelFileGenerator

router = APIRouter()


@router.post("/generate-file")
def generate_file(request: FileGenerationRequest):
    """
    Generate a file (DOCX or Excel) from natural language instructions
    and return it as a downloadable response.
    """

    if request.file_type == "docx":
        generator = DocxFileGenerator()
        suffix = ".docx"
    elif request.file_type == "excel":
        generator = ExcelFileGenerator()
        suffix = ".xlsx"
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        output_path = tmp.name

    generator.generate_file(
        input=request.instructions,
        output_path=output_path,
    )

    return FileResponse(
        path=output_path,
        filename=f"generated_file{suffix}",
        media_type="application/octet-stream",
    )
