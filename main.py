def compare_files(correctFile, submitFile):
      correct = zipfile.ZipFile(correctFile)
      submit = zipfile.ZipFile(submitFile)
      if len(correct.namelist()) != len(submit.namelist()):
          return "Wrong file structure"
      for name in submit.namelist():
          if name not in correct.namelist():
              return "Wrong file structure"
          if submit.read(name) != correct.read(name):
              return "Wrong answer"
      return "OK"


