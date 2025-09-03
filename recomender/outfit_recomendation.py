
import pandas as pd
class OutfitRecomender:
  def __init__(self, csv_path):
    self.data = pd.read_csv(csv_path)

  def recomend(self, color = None, ocassion = None):
    result = self.data
    if color:
      result = result[result['color'].str.lower()==
color.lower()]
    if ocassion:
      result = result[result['ocassion'].str.lower()==
ocassion.lower()]
    return result['outfit'].tolist()
