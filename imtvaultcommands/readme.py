"""

"""
import subprocess


def run(args):
    from cldfbench_imtvault import Dataset

    ds = Dataset()
    readme = ds.dir / 'README.md'
    subprocess.check_call([
        'cldfbench',
        'cldfviz.text',
        str(ds.cldf_specs_dict[None].metadata_path.resolve()),
        '--output', str(readme),
        '--text-file', str(ds.etc_dir / 'README_tmpl.md')
    ])
    readme.write_text(readme.read_text(encoding='utf8').replace(
        "__cldf_markdown_example__",
        """\
[](ExampleTable?with_internal_ref_link#cldf:langsci220-e5ca0880e8) 
[](ExampleTable?with_internal_ref_link#cldf:glossa5188-47)

[References](Source?cited_only#cldf:__all__)"""), encoding='utf8')
