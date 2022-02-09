"""
The class what will check dublicates, blank spaces and empty values. 
And then It will clean dataset with pandas. 

"""
from unittest import result
import pandas as pd


class PreparationDataset:
    """
    """
    cleaned_data: pd.DataFrame = None

    def __init__(self,raw_data: pd.DataFrame) -> None:
        self.raw_data: pd.DataFrame = raw_data
        self.cleaned_data = raw_data
        
    
    
    def start_preparation(self) -> str:
        result_progress = ""
        try:
            result_progress = self.remove_blank_space()
            result_progress += self.check_duplicates()
            result_progress += self.remove_blank_space()
            
        except:
            result_progress += "Progress has not been finished."
        else:
             result_progress = "Progress has been finished successfuly"
             self.cleaned_data.to_csv("./data/cleaned_data.csv")
        
        return result_progress



    def remove_null_data(self) -> str:
        error_message = ""
        try:
                
            average_room_value = self.raw_data['bedrooms'].mean().round().astype(int)
            self.cleaned_data['bedrooms'] = self.cleaned_data['bedrooms'].fillna(average_room_value)
            average_surface = self.raw_data['surface'].round().astype(int)
            self.cleaned_data['surface'] = self.cleaned_data['surface'].fillna(average_surface)
            average_area = self.raw_data['area'].mean().round().astype(int)
            self.cleaned_data['area'] = self.cleaned_data['area'].fillna(average_area)
            self.cleaned_data['equipped_kitchen'] = self.cleaned_data['equipped_kitchen'].fillna(self.raw_data['equipped_kitchen'].describe().top)
            self.cleaned_data['state'] = self.cleaned_data['state'].fillna(self.raw_data['state'].describe().top)
            self.cleaned_data['surface_plot'].fillna(self.raw_data['surface'])
            self.cleaned_data['furnished'] = self.cleaned_data['furnished'].fillna(0)
            self.cleaned_data['open_fire'] = self.cleaned_data['open_fire'].fillna(0)
            self.cleaned_data['terrace'] = self.cleaned_data['terrace'].fillna(0)
            self.cleaned_data['garden'] = self.cleaned_data['garden'].fillna(0)
            self.cleaned_data['facades'] = self.cleaned_data['facades'].fillna(2)
            self.cleaned_data['swimming_pool'] = self.cleaned_data['swimming_pool'].fillna(0)
                
        except:
            error_message = "Not Removed null data from specific columns."
        else:
            error_message = "Removed null data from specific columns"
        
        return error_message


    def check_duplicates(self) -> str:
        error_message = ""
        try:
            self.cleaned_data.drop_duplicates()
        except:
            error_message = "Dataset has not been drop duplicates"
        else:
            error_message = "Dataset has been drop duplicates"
        
        return error_message
    
    
    def remove_blank_space(self) -> str:
        error_message = ""
        try:
            for col in self.raw_data.columns:
                if type(col) == "Object":
                    self.cleaned_data[col] = self.raw_data[col].str.strip()
        except:
             error_message = "Blank space can not removed."
        else:
             error_message = "Blank space has been removed."
        
        return error_message
    

