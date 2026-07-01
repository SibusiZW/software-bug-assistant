from pathlib import Path

BASE_DIR = Path('workspace').resolve()

def read_text(path: str) -> str:
    try:
        resolved_path = (BASE_DIR / path).resolve()

        if not str(resolved_path).startswith(str(BASE_DIR)):
            return "Access denied"

        if not resolved_path.exists():
            return "File not found"
        
        read_text = resolved_path.read_text(encoding='utf-8')
        return read_text
    except Exception as e:
        return str(e)
    
def write_text(path: str, content: str) -> dict:
    try:
        resolved_path = (BASE_DIR / path).resolve()

        if not str(resolved_path).startswith(str(BASE_DIR)):
            return {'error': "Access denied"}

        resolved_path.parent.mkdir(parents=True)
        
        resolved_path.write_text(encoding='utf-8', data=content)
        return {
            "msg": 'Success',
            'file': path,
            'content': content
        }
    except Exception as e:
        return { "error": str(e) }
    

def list_directory(directory: str = '.') -> list:
    try:
        resolved_path = (BASE_DIR / directory).resolve()

        if not str(resolved_path).startswith(str(BASE_DIR)):
            return ["Access denied"]

        if not resolved_path.exists():
            return ["File not found"]

        return [str(file.name) for file in resolved_path.iterdir()]

        
    except Exception as e:
        return [str(e)]
    
