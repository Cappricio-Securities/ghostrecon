import os
import sys

target_name = sys.argv[1]
savepath = sys.argv[2]

# Creating folder for data
data_folder = os.path.join(savepath, 'data')
os.makedirs(data_folder, exist_ok=True)

# Creating folder with company name
company_folder = os.path.join(data_folder, target_name)
os.makedirs(company_folder, exist_ok=True)
