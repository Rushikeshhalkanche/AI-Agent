def calculator(expression: str) -> float:
    """
    Simple calculator tool.
    """
    try:
        return eval(expression)
    except Exception as e:
        raise ValueError(f"Calculator error: {e}")
