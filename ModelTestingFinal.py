import plaidml.keras
plaidml.keras.install_backend()
import numpy as np
np.random.seed(1337)
from keras.models import load_model

# AI Powered Sentiment Predictive Tool for Sustainability Awareness and Advocacy

# Models have been built in BoilerMake2020.py
# This file has functions to process input from UI and return predictions using models.

def process_from_form(input_array):
    input_data = np.array()

    #age range
    if input_array[0] is '18-22':
        input_data.append(1)
    elif input_array[0] is '23-27':
        input_data.append(2)
    else:
        input_data.append(3)

    #education level
    if input_array[1] is 'In full-time education':
        input_data.append(0)
    else:
        input_data.append(1)

    # work status
    if input_array[2] is 'Full-time':
        input_data.append(0)
    elif input_array[2] is 'Part-time':
        input_data.append(0)
    else:
        input_data.append(1)

    #transportation
    if input_array[6] is True:
        input_data.append(0)
    elif input_array[3] is True and input_array[4] is False and input_array[5] is False:
        input_data.append(1)
    elif input_array[3] is False and input_array[4] is True and input_array[5] is False:
        input_data.append(2)
    elif input_array[3] is False and input_array[4] is False and input_array[5] is True:
        input_data.append(3)
    elif input_array[3] is True and input_array[4] is True and input_array[5] is False:
        input_data.append(1.5)
    elif input_array[3] is True and input_array[4] is False and input_array[5] is True:
        input_data.append(2)
    elif input_array[3] is False and input_array[4] is True and input_array[5] is True:
        input_data.append(2.5)
    else:
        input_data.append(2)

    #travel time
    if input_array[7] is 'I don\'t travel':
        input_data.append(-1)
    elif input_array[7] is 'Less than 15 minutes':
        input_data.append(2)
    elif input_array[7] is 'Less than 5 minutes':
        input_data.append(0)
    elif input_array[7] is 'Less than an hour':
        input_data.append(1)
    else:
        input_data.append(3)

    #engaged
    if input_array[8] > 3:
        input_data.append(1)
    else:
        input_data.append(0)

    # awareness of what carbon footprint is
    if input_array[9] > 3:
        input_data.append(1)
    else:
        input_data.append(0)

    #awareness of own
    if input_array[10] > 3:
        input_data.append(1)
    else:
        input_data.append(0)

    #how is your carbon footprint?
    if input_array[11] > 3:
        input_data.append(1)
    else:
        input_data.append(0)

    #lifestyle changes
    if input_array[17] is 1:
        input_data.append(0)
    elif input_array[12] is True and input_array[13] is False and input_array[14] is False and input_array[15] is False and input_array[16] is False:
        input_data.append(1)
    elif input_array[12] is False and input_array[13] is True and input_array[14] is False and input_array[15] is False and input_array[16] is False:
        input_data.append(2)
    elif input_array[12] is False and input_array[13] is False and input_array[14] is True and input_array[15] is False and input_array[16] is False:
        input_data.append(3)
    elif input_array[12] is False and input_array[13] is False and input_array[14] is False and input_array[15] is True and input_array[16] is False:
        input_data.append(4)
    elif input_array[12] is False and input_array[13] is False and input_array[14] is False and input_array[15] is False and input_array[16] is True:
        input_data.append(5)
    elif input_array[12] is True and input_array[13] is True and input_array[14] is False and input_array[15] is False and input_array[16] is False:
        input_data.append(3.5)
    elif input_array[12] is False and input_array[13] is True and input_array[14] is False and input_array[15] is True and input_array[16] is False:
        input_data.append(6.5)
    elif input_array[12] is False and input_array[13] is True and input_array[14] is True and input_array[15] is False and input_array[16] is False:
        input_data.append(5.5)
    elif input_array[12] is False and input_array[13] is True and input_array[14] is False and input_array[15] is False and input_array[16] is True:
        input_data.append(7.5)
    elif input_array[12] is True and input_array[13] is True and input_array[14] is True and input_array[15] is False and input_array[16] is False:
        input_data.append(6.5)
    elif input_array[12] is False and input_array[13] is True and input_array[14] is False and input_array[15] is True and input_array[16] is True:
        input_data.append(11)
    else:
        input_data.append(4.5)

    #encourage
    if input_array[18] is 'Yes':
        input_data.append(0)
    else:
        input_data.append(1)

    p1 = predict_model_output(input_data, 'Info_Utility.h5')
    p2 = predict_model_output(input_data, 'Habit_Change.h5')
    p3 = predict_model_output(input_data, 'Care_Sentiment.h5')

    return p1, p2, p3


def predict_model_output(input_data, modname):
    model = load_model(modname)
    predictions = model.predict_classes(input_data)
    return predictions
