import os, importlib.util, argparse
from functools import wraps
from typing import Dict, Any, List
from .docu_files import pdf_doc

_developer_comments: Dict[str, Dict[str, Any]] = {}
_current_file: str = ''

_temp_args: Dict[str, List[str]] = {}
_temp_return: Dict[str, List[str]] = {}

def returns(argument: str):
    def decorator(obj):
        name = obj.__name__
        _temp_return.setdefault(name, []).append(argument)

        @wraps(obj)
        def wrapper(*args, **kwargs):
            return obj(*args, **kwargs)

        return wrapper if callable(obj) else obj
    return decorator

def args(argument: str):
    def decorator(obj):
        name = obj.__name__
        _temp_args.setdefault(name, []).append(argument)

        @wraps(obj)
        def wrapper(*args, **kwargs):
            return obj(*args, **kwargs)

        return wrapper if callable(obj) else obj
    return decorator

def comment(description: str):
    def decorator(obj):
        name = obj.__name__

        @wraps(obj)
        def wrapper(*args, **kwargs):
            return obj(*args, **kwargs)

        _developer_comments[name] = {
            'comment': description.strip(),
            'args': _temp_args.pop(name, [])[::-1],
            'return': _temp_return.pop(name, [])[::-1],
            'type': 'class' if isinstance(obj, type) else 'function',
            'obj': obj,
            'file': _current_file
        }

        return wrapper if callable(obj) else obj
    return decorator

@comment('Collects and returns the copy of all comments')
def get_comments() -> Dict[str, Dict[str, Any]]:
    return _developer_comments.copy()

@comment('Creates documentation by dynamically importing .py files')
def docuflow(base_dir='.'):
    global _developer_comments, _current_file, _temp_args, _temp_return

    parser = argparse.ArgumentParser(description="")

    parser.add_argument('--pdf', nargs='?', const='documentation.pdf', type=str, help='Generates pdf documentation')
    parser.add_argument('--output', nargs='?', const='documentation', type=str, help='Output name')
    parser.add_argument('--html', nargs='?', const='documentation.html', type=str, help='Generates html documentation')

    args = parser.parse_args()

    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        files[:] = [f for f in files if not f.startswith('.') and f != '__init__.py' and f != 'setup.py']

        for file in files:
            if (file.endswith('.py') or file.endswith('.pyw')) and file != os.path.basename(__file__):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir)
                module_name = os.path.splitext(rel_path)[0].replace(os.sep, '.')

                # _developer_comments = {}
                _temp_args = {}
                _temp_return = {}
                _current_file = rel_path

                try:
                    spec = importlib.util.spec_from_file_location(module_name, full_path)
                    if spec and spec.loader:
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                except Exception as e:
                    print(f"Błąd importowania {rel_path}: {e}")
                    continue


    if args.pdf:
        pdf_doc(_developer_comments, args.output)
