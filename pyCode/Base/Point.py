class PointD(object):
    def __init__(self):
        self._x = 0
        self._y = 0
    @property
    def X(self):
        return self._x
    @X.setter
    def X(self,value):
        self._x = value
    @property
    def Y(self):
        return self._y
    @Y.setter
    def Y(self,value):
        self._y = value