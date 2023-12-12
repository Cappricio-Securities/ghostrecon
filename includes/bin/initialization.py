import os
import sys

target_name = sys.argv[1]
savepath = sys.argv[2]

# Creating folder for data
os.makedirs(savepath, exist_ok=True)

# Creating folder with company name
company_folder = os.path.join(savepath, target_name)
os.makedirs(company_folder, exist_ok=True)
