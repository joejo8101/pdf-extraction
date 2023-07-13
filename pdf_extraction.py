# # import PyPDF2
# import requests
# import re
# import io
# from PyPDF2 import PdfReader

# # Define the field labels dictionary
# field_labels = {
#     'name_address_employer': 'Name Address Employer',
#     'name_address_employee': 'Name Address Employee',
#     'pan_deductor': 'PAN Deductor',
#     'tan_deductor': 'TAN Deductor',
#     'pan_employee': 'PAN Employee',
#     'assessment_year': 'Assessment Year',
#     'salary_17_1': 'Salary 17(1)',
#     'value_prerequisites_17_2': 'Value Prerequisites 17(2)',
#     'profits_in_lieu_17_3': 'Profits in Lieu 17(3)',
#     'total_salary': 'Total Salary',
#     'salary_from_other': 'Salary from Other',
#     'travel_concession_10_5': 'Travel Concession 10(5)',
#     'gratuity_10_10': 'Gratuity 10(10)',
#     'pension_commuted_10_10a': 'Pension Commuted 10(10a)',
#     'leave_encashment_10_1aa': 'Leave Encashment 10(1aa)',
#     'house_rent_hra_10_13a': 'House Rent (HRA) 10(13a)',
#     'any_other_exemption_10': 'Any Other Exemption(10)',
#     'total_any_other_exemption_10': 'Total Any Other Exemption(10)',
#     'total_exemptions_10': 'Total Exemptions(10)',
#     'total_salary_current_employer': 'Total Salary Current Employer',
#     'standard_deduction_16_ia': 'Standard Deduction 16(ia)',
#     'entertaiment_allowance_16_ii': 'Entertainment Allowance 16(ii)',
#     'tax_on_employment_16_iii': 'Tax on Employment 16(iii)',
#     'total_deduction': 'Total Deduction',
#     'income_house_property': 'Income House Property',
#     'income_other_sources': 'Income Other Sources',
#     'total_other_income': 'Total Other Income',
#     'gross_total_income': 'Gross Total Income',
#     'deduction_80c': 'Deduction 80C',
#     'deduction_80ccc': 'Deduction 80CCC',
#     'deduction_pension_80ccd_1': 'Deduction Pension 80CCD(1)',
#     'deduction_total_80c_ccc_ccd_1': 'Deduction Total 80 (C, CCC, CCD(1))',
#     'deduction_pension_80ccd_1b': 'Deduction Pension 80CCD(1B)',
#     'deduction_employer_pension_80ccd_2': 'Deduction Employer Pension 80CCD(2)',
#     'deduction_health_insurance_80d': 'Deduction Health Insurance 80D',
#     'deduction_education_loan_80e': 'Deduction Education Loan 80E',
#     'deduction_donations_80g': 'Deduction Donations 80G',
#     'deduction_interest_savings_80tta': 'Deduction Interest Savings 80TTA',
#     'deduction_any_other_vi_a': 'Deduction Any Other VI(A)',
#     'deduction_total_any_other_vi_a': 'Deduction Total Any Other VI(A)',
#     'deduction_aggregate_vi_a': 'Deduction Aggregate VI(A)',
#     'total_taxable_income': 'Total Taxable Income',
#     'tax_on_total_income': 'Tax on Total Income',
#     'rebate_87a': 'Rebate under Section 87(A)',
#     'surcharge': 'Surcharge',
#     'health_edu_cess': 'Health and Education Cess',
#     'tax_payable': 'Tax Payable',
#     'relief_89': 'Relief under Section 89',
#     'net_tax_payable': 'Net Tax Payable',
# }

# # Create a dictionary to store the extracted values
# field_values = {}

# # Define the regular expression patterns to extract the values
# patterns = {
#     'name_address_employer': r'Name Address Employer:\s*(.*)',
#     'name_address_employee': r'Name Address Employee:\s*(.*)',
#     'pan_deductor': r'PAN Deductor:\s*(.*)',
#     'tan_deductor': r'TAN Deductor:\s*(.*)',
#     'pan_employee': r'PAN Employee:\s*(.*)',
# }

# # pdf_path = "/home/user/Documents/Test-Data.pdf"

# # # Open the PDF file
# # with open(pdf_path, "rb") as f:
# #     reader = PyPDF2.PdfReader(f)

# #     # Extract text from each page of the PDF
# #     extracted_text = ""
# #     for page in reader.pages:
# #         extracted_text += page.extract_text()

# # for field_key, field_label in field_labels.items():
# #     pattern = patterns.get(field_key)  # Use get() method to handle missing keys
# #     if pattern:
# #         match = re.search(pattern, extracted_text, re.IGNORECASE)
# #         if match:
# #             field_values[field_key] = match.group(1).strip()

# # # Print the extracted values
# # for field_key, field_label in field_labels.items():
# #     print(f"{field_label}: {field_values.get(field_key, 0)}")


# url = 'https://incometaxindia.gov.in/forms/income-tax%20rules/103120000000007849.pdf'

# r = requests.get(url)
# print("r", r)
# f = io.BytesIO(r.content)

# reader = PdfReader(f)
# contents = reader.pages[0].extract_text()
# print("CONTENTS", contents)

import PyPDF2
import requests
import re
import io

# Define the field labels dictionary
field_labels = {
    'name_address_employer': 'Name Address Employer',
    'name_address_employee': 'Name Address Employee',
    'pan_deductor': 'PAN Deductor',
    'tan_deductor': 'TAN Deductor',
    'pan_employee': 'PAN Employee',
    'assessment_year': 'Assessment Year',
    'salary_17_1': 'Salary 17(1)',
    'value_prerequisites_17_2': 'Value Prerequisites 17(2)',
    'profits_in_lieu_17_3': 'Profits in Lieu 17(3)',
    'total_salary': 'Total Salary',
    'salary_from_other': 'Salary from Other',
    'travel_concession_10_5': 'Travel Concession 10(5)',
    'gratuity_10_10': 'Gratuity 10(10)',
    'pension_commuted_10_10a': 'Pension Commuted 10(10a)',
    'leave_encashment_10_1aa': 'Leave Encashment 10(1aa)',
    'house_rent_hra_10_13a': 'House Rent (HRA) 10(13a)',
    'any_other_exemption_10': 'Any Other Exemption(10)',
    'total_any_other_exemption_10': 'Total Any Other Exemption(10)',
    'total_exemptions_10': 'Total Exemptions(10)',
    'total_salary_current_employer': 'Total Salary Current Employer',
    'standard_deduction_16_ia': 'Standard Deduction 16(ia)',
    'entertaiment_allowance_16_ii': 'Entertainment Allowance 16(ii)',
    'tax_on_employment_16_iii': 'Tax on Employment 16(iii)',
    'total_deduction': 'Total Deduction',
    'income_house_property': 'Income House Property',
    'income_other_sources': 'Income Other Sources',
    'total_other_income': 'Total Other Income',
    'gross_total_income': 'Gross Total Income',
    'deduction_80c': 'Deduction 80C',
    'deduction_80ccc': 'Deduction 80CCC',
    'deduction_pension_80ccd_1': 'Deduction Pension 80CCD(1)',
    'deduction_total_80c_ccc_ccd_1': 'Deduction Total 80 (C, CCC, CCD(1))',
    'deduction_pension_80ccd_1b': 'Deduction Pension 80CCD(1B)',
    'deduction_employer_pension_80ccd_2': 'Deduction Employer Pension 80CCD(2)',
    'deduction_health_insurance_80d': 'Deduction Health Insurance 80D',
    'deduction_education_loan_80e': 'Deduction Education Loan 80E',
    'deduction_donations_80g': 'Deduction Donations 80G',
    'deduction_interest_savings_80tta': 'Deduction Interest Savings 80TTA',
    'deduction_any_other_vi_a': 'Deduction Any Other VI(A)',
    'deduction_total_any_other_vi_a': 'Deduction Total Any Other VI(A)',
    'deduction_aggregate_vi_a': 'Deduction Aggregate VI(A)',
    'total_taxable_income': 'Total Taxable Income',
    'tax_on_total_income': 'Tax on Total Income',
    'rebate_87a': 'Rebate under Section 87(A)',
    'surcharge': 'Surcharge',
    'health_edu_cess': 'Health and Education Cess',
    'tax_payable': 'Tax Payable',
    'relief_89': 'Relief under Section 89',
    'net_tax_payable': 'Net Tax Payable',
}

# Create a dictionary to store the extracted values
field_values = {}

# Define the regular expression patterns to extract the values
patterns = {
    'name_address_employer': r'Name Address Employer:\s*(.*)',
    'name_address_employee': r'Name Address Employee:\s*(.*)',
    'pan_deductor': r'PAN Deductor:\s*(.*)',
    'tan_deductor': r'TAN Deductor:\s*(.*)',
    'pan_employee': r'PAN Employee:\s*(.*)',
}

pdf_url = 'https://txgain-user-files.s3.ap-south-1.amazonaws.com/form16/59gxt3mw8k3u/r1no5g8.pdf'

# # Extract the file ID from the URL
# file_id = pdf_url.split('/')[-2]

# # Construct the download URL for the file
# download_url = f'https://drive.google.com/uc?id={file_id}'

# # Download the PDF file
response = requests.get(pdf_url)
pdf_io = io.BytesIO(response.content)
# Open the downloaded PDF file
pdf_file = PyPDF2.PdfReader(pdf_io)

# Extract text from each page of the PDF
extracted_text = ""
for page in pdf_file.pages:
    extracted_text += page.extract_text()
print("EXTRACTEDE TEXT", extracted_text)
for field_key, field_label in field_labels.items():
    pattern = patterns.get(field_key)  # Use get() method to handle missing keys
    if pattern:
        match = re.search(pattern, extracted_text, re.IGNORECASE)
        if match:
            field_values[field_key] = match.group(1).strip()

# Print the extracted values
for field_key, field_label in field_labels.items():
    print(f"{field_label}: {field_values.get(field_key, 0)}")


