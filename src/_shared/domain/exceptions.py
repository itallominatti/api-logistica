class CurrencyNotFoundException(Exception):
    """
        Moeda não encontrada
    """
    def __init__(self, currency: str):
        message = f"Moeda {currency} não encontrada ou não implementada"