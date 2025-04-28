import argparse
import shutil
import os
import jinja2
from pathlib import Path

config_file_template = '''
<?xml version="1.0" ?>
<model>
  <name>{{ model_name }}</name>
  <version>1.0</version>
  <sdf version="1.6">f{{ sdf_file }}</sdf>
  <author>
    <name>User</name>
    <email>you@example.com</email>
  </author>
  <description>
    Model Mesh
  </description>
</model>

'''
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

  print(current_path)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-df', dest='dae_path', required=True)
  parser.add_argument('-n', dest='model_name', required=True)
  args = parser.parse_args()

  dae2world(args.dae_path, args.model_name)



if __name__ == '__main__':
  main()