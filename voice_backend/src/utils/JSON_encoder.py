from json import JSONEncoder
import datetime


# 创建一个自定义的 JSONEncoder 类来处理 datetime 对象的序列化
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()  # 将 datetime 对象转换为 ISO 8601 格式字符串
        if isinstance(obj, datetime.time):
            return obj.isoformat()  # 将 datetime 对象转换为 ISO 8601 格式字符串
        return super().default(obj)
