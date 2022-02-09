# Renaming and sorting Files with Python
from datetime import datetime
from pathlib import Path

our_files = Path("/Users/ilaprihodko/Desktop/code")
for file in our_files.iterdir():
    if file.name != ".DS_Store":
        directory = file.parent
        extension = file.suffix

        old_name = file.stem
        region, report_type, old_date = old_name.split("-")

        old_date = datetime.strptime(old_date, "%Y%b%d")
        date = datetime.strftime(old_date, "%Y-%m-%d")
        print(date)

        new_name = f'{date} - {region} - {report_type}{extension}'

        month = datetime.strftime(old_date, "%B")
        new_path = our_files.joinpath(month)
        
        if not new_path.exists():
            new_path.mkdir()

        new_file_path = new_path.joinpath(new_name)

        file.rename(new_file_path)
        print(new_name)
