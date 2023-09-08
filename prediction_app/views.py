from django.shortcuts import render
from django.http import HttpResponse
import torch
import torch.nn as nn
import numpy as np
import os
from .pytorch_models import LinearReg


script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'linear_regression.pth')
       
linear_reg = LinearReg(input_shape=3, hidden_units=8, output_shape=1)
linear_reg.load_state_dict(torch.load(model_path))   
#    loaded_model = torch.load('prediction_app/linear_regression.pth')

new_data = [[12, 2, 3]]
new_data_array = np.array(new_data)
new_data_array = torch.from_numpy(new_data_array).type(torch.float)

            # Make predictions
linear_reg.eval()
with torch.inference_mode():
    pred = linear_reg(new_data_array)
pred_value = pred.item()
# print(pred_value)


def index(request):
    
    message = {}
    org_scale= 84000.0
    org_center= 73000.0

    country_center = 16
    country_scaled = 16

    education_level_center= 1.0
    education_level_scaled = 2.0

    years_of_experience_center = 9.0
    years_of_experience_scaled = 10.0

    if request.method == 'POST':
        country = (int(request.POST['country']) - country_center)/country_scaled
        education_level = (int(request.POST['education_level'])-education_level_center)/education_level_scaled
        years_of_experience = (int(request.POST['progress'])- years_of_experience_center)/years_of_experience_scaled

        script_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(script_dir, 'linear_regression.pth')
       
        linear_reg = LinearReg(input_shape=3, hidden_units=8, output_shape=1)
        linear_reg.load_state_dict(torch.load(model_path))   
#    loaded_model = torch.load('prediction_app/linear_regression.pth')

        # new_data = [[12, 2, 3]]
        new_data = [[country,education_level, years_of_experience]]
        new_data_array = np.array(new_data)
        new_data_array = torch.from_numpy(new_data_array).type(torch.float)

            # Make predictions
        linear_reg.eval()
        with torch.inference_mode():
            pred = linear_reg(new_data_array)
        pred_value = pred.item()
        org_pred_value = round((pred_value * (org_scale)) + org_center, 4)
        # print(pred_value)

       
        message = {
                # 'prediction': pred_value,
                # 'transform_prediction': org_pred_value,
                # 'country': country,
                # 'education_level':education_level 
                'result': org_pred_value
            }
    
    return render(request, 'index.html', {'message': message})
    # return render(request, 'index.html')
