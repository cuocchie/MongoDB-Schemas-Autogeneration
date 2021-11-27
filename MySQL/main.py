import logging
import time
import timeit
import utils
from get_random_name import get_name_list, get_name

NUMBER_OF_CLASSES = 1000
NUMBER_OF_STUDENTS = 250000
NUMBER_OF_GRADES = 250000

if __name__ == '__main__':
    logging.basicConfig(filename='logging.log', level=logging.DEBUG)
    cn = utils.connection()

    utils.create_tables()
    utils.set_foreign_key()

    start = timeit.default_timer()

    utils.create_class()
    student_id = 19000000
    for i in range(400):
        try:
            utils.create_grade()
            utils.create_student(student_id=student_id +
                                 NUMBER_OF_STUDENTS * i,
                                 batch=i)
        except Exception as e:
            logging.error('error: ', e)
            cn.close()
            logging.error(f'Batch {i} failed, increase BATCHES to one')
    cn.close()
    stop = timeit.default_timer()  # Stop timer to check time create class dict
    logging.info(
        f'Time insert all values estimated: {time.strftime("%H:%M:%S", time.gmtime(stop - start))}'
    )
    # mycursor.execute("SHOW TABLES")
