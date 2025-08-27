import nbformat
import glob

def clean_widget_outputs(notebook_path):
    with open(notebook_path, encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    modified = False
    for cell in nb.cells:
        if cell.cell_type == "code" and "outputs" in cell:
            new_outputs = []
            for out in cell.outputs:
                if out.output_type in ["stream", "execute_result", "error"]:
                    new_outputs.append(out)
                elif out.output_type == "display_data":
                    if "application/vnd.jupyter.widget-view+json" in out.data:
                        out.data.pop("application/vnd.jupyter.widget-view+json", None)
                        out.data.pop("application/vnd.jupyter.widget-state+json", None)
                        modified = True
                        if not out.data:
                            continue  # Skip empty output
                    new_outputs.append(out)
            cell.outputs = new_outputs

    if modified:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print(f"✔ Cleaned: {notebook_path}")
    else:
        print(f"✓ Already clean: {notebook_path}")

# Run on all .ipynb files in this folder
for file in glob.glob("*.ipynb"):
    clean_widget_outputs(file)
