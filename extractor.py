import os
import io
import re
import csv
import shutil
import atexit
import tarfile

class FunkyLogs:

    LOG_DIR_NAME = 'funky_logs'
    LOG_DIR_PATH = os.path.join(
        os.getcwd(),
        LOG_DIR_NAME,
    )

    def __init__(self, archivename:str='logs.tgz') -> None:
    
        atexit.register(self._cleanup)
        
        self.file = tarfile.open(
            os.path.join(os.getcwd(),archivename,),
            'r'
        )
        self._dumpfiles()

    def _cleanup(self):
      try:
          self.file.close()
      except AttributeError:
          pass
      print('Exiting...')

    def _dumpfiles(self):
        print('Dumping Files...')
        self._mkdir()
        self._extract()
        self._create_django()
        self._create_django_dev()

        
        
    def _mkdir(self):
        print('Making Dir...')
        if os.path.isdir(self.LOG_DIR_PATH):
            shutil.rmtree(self.LOG_DIR_PATH)
        return os.mkdir(self.LOG_DIR_PATH)

    def _extract(self):
        print('Extracting Files...')
        self.file.extractall(path=self.LOG_DIR_PATH)

    def _create_django(self):
        print('Loading #django...')
        self._join('#django_', 'django_csv.csv')

    def _create_django_dev(self):
        print('Loading #django-dev...')
        self._join('#django-dev_', 'djangodev_csv.csv')

    def _join(self, pattern, csv_title):
        print('Joining Logs...')

        # we have two sets of logs, #django and #django-dev
        # lets create two files with the combined logs
        files = [
            name 
                for name 
                    in os.listdir(self.LOG_DIR_PATH) 
                        if 
                            pattern in name
        ]
        lines = 0
        matched_lines = 0
        with open(os.path.join(self.LOG_DIR_PATH, csv_title), 'w') as ofile:
            writer = csv.writer(ofile)
            logline_pattern = re.compile(r'\[(\d{2}:\d{2}:\d{2})\] \<(.+)\> (.*)')
            filename_pattern = re.compile(r'\d{8}')
            for file in files:
                year = filename_pattern.search(file)
                with open(os.path.join(self.LOG_DIR_PATH,file,), 'r', encoding="ISO-8859-1") as file:
                    for line in file:
                        lines += 1
                        result = logline_pattern.match(line)
                        if result is not None:
                            matched_lines += 1
                            writer.writerow([year.group(), *result.groups()])
        print('-' * 40)
        print('File Created: %s' % csv_title)
        print('-' * 40)
        print('%d files joined' % files.__len__())
        print('%d lines read' % lines)
        print('%d lines matched' % matched_lines)

if __name__ == '__main__':
    FunkyLogs()