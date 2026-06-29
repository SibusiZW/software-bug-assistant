from pathlib import Path

def read_text(path: str) -> str:
    try:
        resolved_path = Path(path).resolve()

        if not resolved_path.exists():
            return "File not found"
        
        read_text = resolved_path.read_text(encoding='utf-8')
        return read_text
    except Exception as e:
        return str(e)
    

def list_directory(directory: str) -> list:
    try:
        resolved_path = Path(directory).resolve()

        return [str(file.name) for file in resolved_path.iterdir()]

        if not resolved_path.exists():
            return ["File not found"]
    except Exception as e:
        return [str(e)]