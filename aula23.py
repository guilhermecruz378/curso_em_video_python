# -------------- ERROS E EXCESSÕES  ----------------
# 'primt' -> erros de sintase 
# Quando o erro não se dá de forma sintatica, nós chamamos isso de excessão
# Todo erro que geralmente não acontece é chamado de excessão
# é para tratar erros e excessões usamos o 
'''
Try : == tente, se der faça: 
    aqui fica a operação

except: == quando falhar faça:
    falhou

else : == se não falhou execute:
    isso
'''
try: # Posso criar um bloco trye para cada coisa
    a = int(input('NUMERADOR: '))
    b = int(input('Denominador: '))
    r = a/b
#except Exception as erro:
#print(f'Problema encontrado foi {erro.__class__}')
#except:
except (ValueError, TypeError ):
    print('Tivemos problemas com o tipo de dados que você digitou!')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário prefiriu não informar os dados!')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}') 
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte Sempre! Muito Obrigado!!')