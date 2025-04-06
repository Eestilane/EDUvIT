from typing import Any, List, Union

def function_name(search: str, status: bool, *args: Any, **kwargs: Any) -> Union[List[int], str]:
    result: List[int] = []
    result_2: str = ""

    """
    Обрабатывает аргументы в зависимости от режима поиска и статуса.

    1. Если search == "args":
       status = True, оставляет только цифры из args
       status = False, склеивает все args в одну строку
    
    2. Если search == "kwargs":
       делает строку из всех переданных ключей и значений
    
    3. Если search другой, выдаёт ошибку
    """
    
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")
    
    