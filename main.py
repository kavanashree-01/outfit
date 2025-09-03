from recomender.outfit_recomendation import OutfitRecomender
def main():
  recomender = OutfitRecomender("data/outfit.csv")
  print("Outfit for color='red', ocassion='party' is:")
  print(recomender.recomend(color='red',ocassion='party'))

if __name__ == "__main__":
  main()
