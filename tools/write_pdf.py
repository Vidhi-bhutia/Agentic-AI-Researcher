from langchain_core.tools import tool
from datetime import datetime
from pathlib import Path
import subprocess

@tool
def render_latex_pdf(latex_content: str) -> str:
    """
    Render LaTeX content into a PDF file using Tectonic.
    Args:
        latex_content (str): The LaTeX document content as a string.
    Returns:
        str: The path to the generated PDF file.
    """
    try:
        output_dir = Path("pdf_outputs").absolute()
        output_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        tex_filename = f"paper_{timestamp}.tex"
        pdf_filename = f"paper_{timestamp}.pdf"

        tex_file = output_dir / tex_filename
        tex_file.write_text(latex_content)

        tectonic_path = str(Path.home() / "tectonic.exe")
        result = subprocess.run(
            [tectonic_path, tex_filename, "--outdir", str(output_dir)],
            cwd=output_dir,
            capture_output=True,
            text=True, 
        )
        final_pdf_path = output_dir / pdf_filename
        if not final_pdf_path.exists():
            raise FileNotFoundError(f"PDF generation failed. Tectonic output:\n{result.stdout}\n{result.stderr}")
        print(f"PDF generated at: {final_pdf_path}")
        return str(final_pdf_path)
    except Exception as e:
        print(f"Error generating PDF: {e}")
        raise