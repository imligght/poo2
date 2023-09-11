from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)

    def __eq__(self, other_object) -> bool:
        if isinstance(other_object, Cliente):
            return (
                id(self) == id(other_object)
            )
        return False
