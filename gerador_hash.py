import hashlib

def gerar_hash(texto, algoritmo='sha256'):
    # Limitar o texto a 32 caracteres
    texto_limitado = texto[:32]

    # Crie um objeto de hash com o algoritmo especificado
    hash_obj = hashlib.new(algoritmo)

    # Atualize o objeto de hash com o texto convertido para bytes
    hash_obj.update(texto_limitado.encode('utf-8'))

    # Obtenha o valor de hash em hexadecimal
    hash_hex = hash_obj.hexdigest()

    return hash_hex

# Solicitar entrada de texto ao usuário
texto = input("Digite o texto (limite de 32 caracteres): ")

# Chamar a função gerar_hash com o texto inserido
hash_resultado = gerar_hash(texto)

print(f'Texto: {texto}')
print(f'Hash: {hash_resultado}')
