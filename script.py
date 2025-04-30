import argparse
import shutil
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
env = Environment(loader=FileSystemLoader('templates'))

config_file_template = env.get_template('config_template.xml')
sdf_file_template =  env.get_template('model_sdf_template.xml')
world_file_template = env.get_template('world_template.xml')
def dae2world(dae_path, model_name, gazebo_type):
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
  destination_folder = Path.home() / f'.{gazebo_type}' / 'models' / model_name

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

  worlds_folder = current_path / 'worlds'
  if not worlds_folder.exists():
      worlds_folder.mkdir(parents=True)
      print('Folder made!')
  else:
      print('Folder already created')
  
  world_file_path = worlds_folder / f'{model_name}.world'
  world_render = world_file_template.render(model_folder= f'model://{model_name}')
  with open(world_file_path, 'w', encoding='utf-8') as f:
     f.write(world_render)
     
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-df', dest='dae_path', required=True)
  parser.add_argument('-n', dest='model_name', required=True)
  parser.add_argument('-t', dest='gazebo_type', default='gazebo')
  args = parser.parse_args()

  dae2world(args.dae_path, args.model_name, args.gazebo_type)



if __name__ == '__main__':
  main()