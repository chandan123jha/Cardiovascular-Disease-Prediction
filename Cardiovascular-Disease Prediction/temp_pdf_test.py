import sys
from pathlib import Path
project = Path(__file__).resolve().parent
sys.path.insert(0, str(project))
import Check_Heart
path = Check_Heart.generate_pdf_report(
    'Test report text', 'TestUser', '21', '1', '1', '130', '200', '0', '0', '140', '0', '2.3', '1', '0', '2',
    text_color='green'
)
print(path)
print('exists', Path(path).exists())
