import os
import subprocess


# subprocess.run("ls code/input_files", shell=True)

for filename in os.listdir('input_files'):

    source_file = f"/input_files/{filename}"   # original document

    output_filename = os.path.splitext(filename)[0]+".pdf"
    output_file = f"output_files/{output_filename}"
    output_folder = "output_files"   # pdf files will be here

    # METHOD 1 - LibreOffice straightly
    # assign the command of converting files through LibreOffice
    convert_to_pdf = rf"libreoffice --headless --convert-to pdf {source_file} --outdir {output_folder}"
    subprocess.run(r'ls output_files/', shell=True)

    ## METHOD 2 - Using unoconv - also working
    # convert_to_pdf = f"unoconv -f pdf {source_file}"
    # subprocess.run(convert_to_pdf, shell=True)
    # print(f'file {filename} converted')