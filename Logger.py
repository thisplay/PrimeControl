import logging


logFile= ("System.log")   
                
             
# Criando o logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
logger.setLevel(logging.INFO)        

  
# Criando um handler para o arquivo
logger_handler = logging.FileHandler(logFile, mode='a')
logger_handler.setLevel(logging.INFO)
c_handler = logging.StreamHandler()
 
# formatação da mensagem
logger_formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
logger_handler.setFormatter(logger_formatter)
  
logger.addHandler(logger_handler)
 
 

logger.error('Logger OK/error')