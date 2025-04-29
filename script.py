import argparse
import shutil
import os
from jinja2 import Template
from pathlib import Path

config_file_template = Template(Path('config_template.xml').read_text(encoding='utf-8'))

def dae2world(dae_path, model_name):
  current_path = Path.cwd()
  file_name = Path(dae_path).name
  models_folder = current_path / 'models'
  specific_model_folder = models_folder / model_name
  meshes_folder = specific_model_folder / 'meshes'
  
  if not meshes_folder.exists():
      meshes_folder.mkdir(parents=True)
      print('Folder made!')
  else:
     print('Folder already created')
  file_custom_directory = meshes_folder / file_name
  shutil.copyfile(dae_path, file_custom_directory)

  sdf_file = "example.sdf"
  config_file_path = specific_model_folder / 'model.config'
  config_render = config_file_template.render(model_name= model_name, sdf_file=sdf_file)
  with open(config_file_path, 'w', encoding='utf-8') as f:
    f.write(config_render)
  print(current_path)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-df', dest='dae_path', required=True)
  parser.add_argument('-n', dest='model_name', required=True)
  args = parser.parse_args()

  dae2world(args.dae_path, args.model_name)



if __name__ == '__main__':
  main()