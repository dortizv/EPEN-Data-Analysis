import os
import zipfile

def download_dataset(city_code, trimester_code):
    csv_files=[]
    os.chdir("\\".join(os.environ["JPY_SESSION_NAME"].split("\\")[:-1])+"\\")
    try:
        dataset_path = "\\".join(os.environ["JPY_SESSION_NAME"].split("\\")[:-1])+"\\"+"dataset\\"
        os.mkdir(dataset_path)
        print("Dataset directory created")
        os.chdir("dataset")
    except:
        os.chdir("dataset")
        dataset_zips=os.listdir()
        print("Dataset directory already exists")
        
    for i in trimester_code.values():
      for j in city_code.values():
        file_name = str(next((key for key, val in city_code.items() if val == j), None)) + "_" + str(next((key for key, val in trimester_code.items() if val == i), None))
        url = "https://proyectos.inei.gob.pe/iinei/srienaho/descarga/CSV/" + str(i) + "-Modulo" + str(j) + ".zip"
        try:
            dataset_files=os.listdir()
            name_zip=file_name+".zip"
            name_csv=file_name+".csv"
            
            if name_csv in dataset_files:
                print(name_csv + " already extracted.")
            
            elif name_zip in dataset_files:
                print(name_zip + " already exists in the dataset directory.")
                
                with zipfile.ZipFile(name_zip, "r") as f:
                    for name in f.namelist():
                        if name.endswith(".csv"):
                            f.extract(name)
                            os.rename(name, name_csv)
                            csv_files.append(name_csv)
                print(file_name + ".csv succesfully extracted.")
            
            else:
                os.system("curl --output "+ str(name_zip) + " " + str(url))
                print(file_name + " succesfully downloaded.")

                with zipfile.ZipFile(name_zip, "r") as f:
                    for name in f.namelist():
                        if name.endswith(".csv"):
                            f.extract(name)
                            os.rename(name, name_csv)
                            csv_files.append(name_csv)
                print(file_name + ".csv succesfully extracted.")
        except:
            print(file_name + " couldn't be downloaded or extracted.")
    os.chdir("\\".join(os.environ["JPY_SESSION_NAME"].split("\\")[:-1])+"\\")

