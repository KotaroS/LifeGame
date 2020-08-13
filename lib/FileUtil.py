import datetime
import glob
import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import pathlib
import pickle

#lst = [1, 2, 3]
class FileUtil:
	@classmethod
	def __getFileName(cls):
		now = datetime.datetime.now()
		fileName = '{0:%Y%m%d_%H%M%S}.pkl'.format(now)
		return fileName
	
	@classmethod
	def getAbsPath(cls, fileName):
		dataset_dir = os.path.dirname(os.path.abspath(__file__))
		return  '{0}/../data/{1}'.format(dataset_dir, fileName)
	
	@classmethod
	def getFileList(cls):
		dataset_dir = os.path.dirname(os.path.abspath(__file__))
		filePath = '{0}/../data/'.format(dataset_dir)
		fileList = pathlib.Path(filePath).glob('*.pkl')
		result = {}
		index = 1
		for file in fileList:
			if index > 20:
				break
			result[index] = file.name
			index += 1
		return result
	
	@classmethod
	def saveInit(cls, data):
		fileName = cls.__getFileName()
		filePath = cls.getAbsPath(fileName)
		with open(filePath, 'wb') as f:
				pickle.dump(data, f, -1)
	
	@classmethod
	def loadInit(cls, fileName):
		filePath = cls.getAbsPath(fileName)
		with open(filePath, 'rb') as f:
			initList = pickle.load(f)
		print(initList)
		return initList

#saveInit(getFileName(), lst)
#FileUtil.loadInit('20200727_181828.pkl')
#print(FileUtil.getFileList())
