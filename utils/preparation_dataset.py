"""
The class what will check dublicates, blank spaces and empty values. 
And then It will clean dataset with pandas. 

"""
import pandas as pd


class PreparationDataset:
    """
    """
    cleaned_data: pd.DataFrame = None

    def __init__(self,raw_data: pd.DataFrame) -> None:
        self.raw_data: pd.DataFrame = raw_data
        self.cleaned_data = raw_data
        
    
    
    def start_preparation(self):
        pass


    def remove_null_data(self):
        error_message = ""
        try:
            for col in self.raw_data.columns:
                if col == 'bedrooms': 
                    average_room_value = self.raw_data[col].mean().round().astype(int)
                    self.cleaned_data[col] = self.cleaned_data[col].fillna(average_room_value)
                if col == 'surface': 
                    average_surface = self.raw_data[col].round().astype(int)
                    self.cleaned_data[col] =self.cleaned_data[col].fillna(average_surface)
                if col == 'area': 
                    average_area = self.raw_data.mean().round().astype(int)
                    self.cleaned_data[col] = self.cleaned_data[col].fillna(average_area)
                if col == 'equipped_kitchen': self.cleaned_data[col] = self.cleaned_data[col].fillna(self.raw_data[col].describe().top)
                if col == 'state': self.cleaned_data[col] = self.cleaned_data[col].fillna(self.raw_data[col].describe().top)
                if col == 'surface_plot': self.cleaned_data[col].fillna(self.raw_data['surface'])
                if col == 'furnished': self.cleaned_data[col].fillna(0)
                if col == 'open_fire': self.cleaned_data[col].fillna(0)
                if col == 'terrace': self.cleaned_data[col].fillna(0)
                if col == 'garden': self.cleaned_data[col].fillna(0)
                if col == 'facades': self.cleaned_data[col].fillna(2)
                if col == 'swimming_pool': self.cleaned_data[col].fillna(0)
                
        except:
            error_message = "Not Removed null data from specific columns."
        else:
            error_message = "Removed null data from specific columns"


    def check_duplicates(self) -> str:
        error_message = ""
        try:
            self.cleaned_data.drop_duplicates()
        except:
            error_message = "Dataset has not been drop duplicates"
        else:
            error_message = "Dataset has been drop duplicates"
    
    
    def remove_blank_space(self):
        error_message = ""
        try:
            for col in self.raw_data.columns:
                if type(col) == "Object":
                    self.cleaned_data[col] = self.raw_data[col].str.strip()
        except:
             error_message = "Blank space can not removed."
        else:
             error_message = "Blank space has been removed."
