import os
import subprocess

from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/convert")
def convert_to_pdf():
    input_folder = "input_files"
    output_folder = "output_files"

    # Установка UID и GID пользователя appuser:appgroup
    # os.setgid(20023)
    # os.setuid(20023)

    for filename in os.listdir(input_folder):
        source_file = os.path.join(input_folder, filename)  # Полный путь к исходному документу
        output_filename = os.path.splitext(filename)[0] + ".pdf"  # Имя выходного файла PDF
        output_file = os.path.join(output_folder, output_filename)  # Полный путь к выходному файлу PDF

        # Команда для конвертации файла в PDF с использованием LibreOffice
        convert_to_pdf_cmd = f"libreoffice --headless --convert-to pdf '{source_file}' --outdir '{output_folder}'"
        subprocess.run(convert_to_pdf_cmd, shell=True)

        # Если нужно использовать unoconv, закомментируйте предыдущую строку и раскомментируйте следующую:
        # convert_to_pdf_cmd = f"unoconv -f pdf '{source_file}' -o '{output_file}'"
        # subprocess.run(convert_to_pdf_cmd, shell=True)

    return {"message": "Conversion completed"}