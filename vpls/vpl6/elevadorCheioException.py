class ElevadorCheioException(Exception):
    def __init__(self) -> None:
        super().__init__('O elevador está cheio!')
