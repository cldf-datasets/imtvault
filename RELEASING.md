# Releasing IMTVault

You must have installed the dataset via
```shell
pip install -e .
```
preferably in a separate virtual environment.

- Update the source repos:
  ```shell
  cldfbench download cldfbench_imtvault.py
  ```
- Recreate the CLDF running (~10mins)
  ```shell
  cldfbench makecldf --with-cldfreadme --with-zenodo cldfbench_imtvault.py --glottolog-version v5.1
  cldf validate cldf
  ```
- Recreate the README running
  ```shell
  cldfbench imtvault.readme
  ```
- Commit and push changes to GitHub
- Create a release on GitHub, thereby pushing the version to Zenodo.
