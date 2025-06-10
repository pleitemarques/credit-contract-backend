from validate_docbr import CPF


def is_valid_cpf(value: str) -> bool:
    """
    Returns True if the CPF is valid (format-agnostic), otherwise False.
    """
    cpf = CPF()

    return cpf.validate(value)