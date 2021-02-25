

import os
#import time
import logging
import logging.handlers


def log_setup(file, level=logging.DEBUG):
    print(type(file), file) 
    #name = "Logs/"+os.path.basename(file)
    name = os.path.basename(file)
    
    #should_roll_over = name
    log_handler = logging.handlers.RotatingFileHandler(name, mode='a', backupCount=5 )
    #if should_roll_over:  # log already exists, roll over!
    #    log_handler.doRollover()

    formatter = logging.Formatter('%(asctime)s %(levelname)6s %(module)8s:%(lineno)d - %(message)s')  

    log_handler.setFormatter(formatter)
    
    logger = logging.getLogger()
    logger.handlers = [] # This is the key thing for the question!
    logger.addHandler(log_handler)
    logger.setLevel(level)
    
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    return log_handler
    
    
def closeLogFile(prh):
    #print('closelogfile')
    #logging.removeHandler(prh)
    return



#----------------------------------------------------------------------
if __name__ == "__main__":
    lgh = log_setup(__file__[:-3]+'.log') 
    
    logging.info('Hello, World!')
    logging.debug('this is debug')
    logging.error('this is error')
    
    #os.rename('my.log', 'my.log-old')
    logging.info('Hello, New World!')
        
    #closeLogFile(lgh)
    