class validadorEmail:
    def es_valido(self, email: str) -> bool:
        return "@" in email and "."in email
class validadorEmailEmpresarial(validadorEmail):
    def es_valido(self, email: str) -> bool:
        return super().es_valido(email) and email.endswith("@empresa.com")