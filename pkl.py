import cPickle as pickle

fr = open('config.pkl')
inf = pickle.load(fr)
fr.close()