# Error Handling

from loguru import logger

while True:
    try:
        age = int(input('what is your age ? '))
        10/age
    except ValueError:
        print('please enter number')
        continue
    except ZeroDivisionError:
        print('please enter age higher than 0')
        continue
    else:
        print('thank you!')
        break
    finally:
        logger.info(f'stored to the log')
