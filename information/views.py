from tablib import Dataset
from django.shortcuts import render
from information.models import StudentInformation, ExtendedInformation
import pandas as pd


def upload(request):
    if request.method == 'POST':
        dataset = Dataset()
        new_res = request.FILES['myfile']
        imported_data = pd.read_csv(new_res)
        imported_data['Registration ID'] = imported_data['Registration ID'].map(str)
        for x in imported_data.index:
            if pd.isna(imported_data['Nickname'][x]):
                var = str(imported_data['Full Name'][x]).split()
                ss = var[-1]
            else:
                ss = imported_data['Nickname'][x]
            value = StudentInformation(registration_ID=imported_data['Registration ID'][x],
                                       certificate_name=imported_data['Full Name'][x],
                                       nickname=ss,
                                       email=imported_data['Email'][x],
                                       permanent_Address=imported_data['Permanent Address'][x],
                                       present_Address=imported_data['Present Address'][x],
                                       phone_Number=imported_data['Phone'][x],
                                       blood_Group=imported_data['Blood'][x],
                                       gender=imported_data['Gender'][x],
                                       batch=imported_data['Batch'][x]
                                       )
            value.save()
            extend_value = ExtendedInformation(
                registration_ID=value
            )
            extend_value.save()
    return render(request, template_name='information/upload.html')
