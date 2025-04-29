import argparse
import shutil
import os
from jinja2 import Template
from pathlib import Path

config_file_template = Template(Path('config_template.xml').read_text(encoding='utf-8'))
sdf_file_template = Template(Path('model_sdf_template.xml').read_text(encoding='utf-8')) 

def dae2world(dae_path, model_name):
  current_path = Path.cwd()
  mesh_name = Path(dae_path).name
  models_folder = current_path / 'models'
  specific_model_folder = models_folder / model_name
  meshes_folder = specific_model_folder / 'meshes'
  
  if not meshes_folder.exists():
      meshes_folder.mkdir(parents=True)
      print('Folder made!')
  else:
      print('Folder already created')
  print(Path.home())
  destination_folder = Path.home() / '.gazebo' / 'models' / model_name

  if not destination_folder.exists():
    destination_folder.mkdir(parents=True)
  file_custom_directory = meshes_folder / mesh_name

  shutil.copyfile(dae_path, file_custom_directory)

  shutil.copytree(specific_model_folder, destination_folder, dirs_exist_ok=True)

  # SDF File Creation
  sdf_file_path = specific_model_folder / 'model.sdf'
  sdf_file_render = sdf_file_template.render(dae_path_from_home=f'model://{model_name}/meshes/{mesh_name}')
  with open(sdf_file_path, 'w', encoding='utf-8') as f:
     f.write(sdf_file_render)
  # Config File Creation
  config_file_path = specific_model_folder / 'model.config'
  config_render = config_file_template.render(model_name= model_name, sdf_file=Path(sdf_file_path).name)
  with open(config_file_path, 'w', encoding='utf-8') as f:
    f.write(config_render)
  print(current_path)

  shutil.copy(config_file_path, destination_folder)
  shutil.copy(sdf_file_path, destination_folder)
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-df', dest='dae_path', required=True)
  parser.add_argument('-n', dest='model_name', required=True)
  args = parser.parse_args()

  dae2world(args.dae_path, args.model_name)



if __name__ == '__main__':
  main()