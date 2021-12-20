from tablib import Dataset
from django.shortcuts import render
from information.models import StudentInformation


def upload(request):
    # if request.method == 'POST':
    #     dataset = Dataset()
    #     new_res = request.FILES['myfile']
    #
    #     imported_data = dataset.load(new_res.read(), format='xlsx')
    #     print(imported_data)
    #     for data in imported_data:
    #         value = StudentInformation(Registration_ID=data[1],
    #                                    certificate_name=data[2],
    #                                    nickname=data[3],
    #                                    email=data[4],
    #                                    phone_Number=data[5],
    #                                    present_Address=data[6],
    #                                    permanent_Address=data[7],
    #                                    gender=data[8],
    #                                    batch=data[9]
    #                                    )
    #         value.save()
    return render(request, template_name='information/upload.html')
