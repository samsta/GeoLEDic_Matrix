from importlib import reload
import GeoLEDic_Matrix.GeoLEDicMatrix


def create_instance(c_instance):
    reload(GeoLEDicMatrix)
    return GeoLEDicMatrix.GeoLEDicMatrix(c_instance)
