import argparse
import shutil
import os
from pathlib import Path

def dae2world(dae_path, model_name):
  current_path = Path.cwd()
  models_folder = current_path / 'models'
  specific_model_folder = models_folder / model_name
  meshes_folder = specific_model_folder / 'meshes'
  
  if not meshes_folder.exists():
      meshes_folder.mkdir(parents=True)
      print('Folder made!')
  else:
     print('Folder already created')
  print(current_path)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-df', dest='dae_path', required=True)
  parser.add_argument('-n', dest='model_name', required=True)
  args = parser.parse_args()

  dae2world(args.dae_path, args.model_name)



if __name__ == '__main__':
  main()