# trabalhando com log
from loguru import logger

logger.add('meu_log.log', level='CRITICAL')

def soma(x,y):
    try:
        soma = x+y
        logger.info(f"Você digitou valores corretos {soma}")
        return soma
    except:
        logger.critical('Você informou valores errados para a soma')

soma(2,3)
soma(2,7)
soma(2,"3")