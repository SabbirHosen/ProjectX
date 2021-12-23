from tablib import Dataset
from django.shortcuts import render
from information.models import StudentInformation
import pandas as pd


def upload(request):
    if request.method == 'POST':
        dataset = Dataset()
        new_res = request.FILES['myfile']
        imported_data = pd.read_csv(new_res)
        imported_data['Registration ID'] = imported_data['Registration ID'].map(str)

        # imported_data = dataset.load(new_res.read(), format='xlsx')
        print(imported_data)
        for x in imported_data.index:
            if imported_data['Nickname'][x] is None:
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
    return render(request, template_name='information/upload.html')
