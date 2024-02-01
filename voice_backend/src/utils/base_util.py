import re
import datetime
from osgeo import gdal, osr
import zipfile


class BaseUtils:
    @classmethod
    def model_to_dict(cls, model):
        try:
            my_model_dict = model.__dict__
            if '_sa_instance_state' in my_model_dict:
                del my_model_dict['_sa_instance_state']
            return my_model_dict
        except:
            my_model_dict_list = []
            for item in model:
                my_model_dict = item.__dict__
                if '_sa_instance_state' in my_model_dict:
                    del my_model_dict['_sa_instance_state']
                my_model_dict_list.append(my_model_dict)
            return my_model_dict_list

    @classmethod
    def datetime_to_string(cls, date_value):
        # 使用 strftime 函数将 DATE 转换为字符串
        date_str = date_value.strftime('%Y年%m月%d日')
        return date_str

    @classmethod
    def csv_string_to_list(cls, csv_string):
        # 使用 split() 函数将字符串分割成列表
        csv_list = re.split(',', csv_string)
        return csv_list

    @classmethod
    def unzip_file(cls, zip_path, extract_path):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                for file_info in zip_ref.infolist():
                    file_info.filename = file_info.filename.encode('cp437').decode('gbk')
                    zip_ref.extract(file_info, extract_path)
            return True
        except Exception as e:
            print(f"Error extracting ZIP file: {str(e)}")
            return False

    @classmethod
    def geographic_to_projected(cls, geographic_coords, source_srs, target_srs):
        try:
            # 创建坐标转换对象
            transform = osr.CoordinateTransformation(source_srs, target_srs)

            # 转换坐标
            projected_coords = transform.TransformPoint(geographic_coords[0], geographic_coords[1])
            return projected_coords[:2]  # 返回投影坐标 (x, y)

        except Exception as e:
            print("Error:", str(e))
            return None
