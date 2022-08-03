from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verificarsenha(senha: str, hash_senha: str) -> bool: 
    """
    funcao pra verificar se a senha ta correta, comparando texto puro do usuario e o hash da senha existente no banco
    """

    return CRIPTO.verify(senha,hash_senha)

def gerar_hash_senha(senha: str) -> str : 
    """"
    funcao que gera e retorna o hash da senha
    """
    return CRIPTO.hash(senha)