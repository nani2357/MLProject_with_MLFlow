# Import necessary modules and libraries
import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

# This function reads a YAML file and returns its content as a ConfigBox object.
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads the content of a YAML file and returns it as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        e: Any other exception that might occur during file reading or parsing.

    Returns:
        ConfigBox: Parsed content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

# This function creates directories from a list of paths.
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories for each path provided in the list.
    
    Args:
        path_to_directories (list): List of paths where directories should be created.
        verbose (bool, optional): If True, logs the creation of each directory. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

# This function saves a dictionary as a JSON file.
@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary as a JSON file.
    
    Args:
        path (Path): Path to the JSON file where data should be saved.
        data (dict): Dictionary to be saved as a JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")

# This function reads a JSON file and returns its content as a ConfigBox object.
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Reads the content of a JSON file and returns it as a ConfigBox object.
    
    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Parsed content of the JSON file as a ConfigBox object.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

# This function saves data as a binary file using joblib.
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data as a binary file using joblib.
    
    Args:
        data (Any): Data to be saved in binary format.
        path (Path): Path to the binary file where data should be saved.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

# This function loads data from a binary file using joblib.
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.
    
    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

# This function returns the size of a file in kilobytes.
@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file in kilobytes.
    
    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in kilobytes.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
