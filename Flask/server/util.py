import pickle
import json
import numpy as np

__model = None
__company_name=None
__job_title=None
__seniority=None
__data_columns=None

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __company_name
    global __job_title
    global __seniority

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __company_name = __data_columns[7:]  # first 9 columns are sqft, bath, bhk
        __job_title = __data_columns[1:7]

    global __model
    if __model is None:
        with open('./artifacts/model_file.p', 'rb') as f:
            __model = pickle.load(f)
            #print(type(__model)) 
    print("loading saved artifacts...done")



def get_estimated_salary(company_name,job_title,experience):
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        with open('./artifacts/model_file.p', 'rb') as f:
            __model = pickle.load(f)
            #print(type(__model))
        #print(len(__data_columns))
        try:
            company_index = __data_columns.index(company_name.lower())
        except:
            company_index = -1
        try:
            job_index = __data_columns.index(job_title.lower())
        except:
            job_index = -1

        
        x = np.zeros(len(__data_columns))
        #print(x)
        x[0] = experience
        if company_index>=0:
            x[company_index] = 1
        if job_index>=0:
            x[job_index] =1

        return round(__model.predict([x])[0],2)




def get_company_names():
    return __company_name

def get_data_columns():
    return __data_columns

def get_job_titles():
    return __job_title


if __name__ == '__main__':
    load_saved_artifacts()
    #print(get_company_names())
    #print(get_job_titles())
    print(get_estimated_salary("Amazon","Data Scientist",9))