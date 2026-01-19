def parse_log_file(file_path: str) -> str:
    """
    Read log file and trim to avoid very large prompts (max 4000 chars).
    """
    with open(file_path, "r", errors="ignore") as file:
        data = file.read()
    return data[:4000]
