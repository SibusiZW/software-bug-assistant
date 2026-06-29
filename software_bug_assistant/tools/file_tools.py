from pathlib import Path

def read_text(path: str):
    try:
        resolved_path = Path(path).resolve()

        if not resolved_path.exists():
            return "File not found"
        
        read_text = resolved_path.read_text(encoding='utf-8')
        return read_text
    except Exception as e:
        return str(e)