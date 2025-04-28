import argparse
from pathlib import Path



def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-df', dest='dae_path', required=True)
  args = parser.parse_args()

  dae_path = Path(args.dae_path)
  print(dae_path)



if __name__ == '__main__':
  main()