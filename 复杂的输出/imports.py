def prints_(prints__):  
    class prints:  
        def __init__(self, prints_name):  
            self.prints_name = prints_name  
  
        def print_message(self):  # 更改方法名以避免与类名冲突  
            return self.prints_name  
  
    # 创建类的实例并调用其方法  
    instance = prints(prints__)  
    return instance.print_message()  # 返回调用方法的结果  
  
def running(if_, prints___):  
    if if_ == "running":  
        # 调用prints_函数并返回其结果  
        return prints_(prints___)  
    else:  
        return "imports is ready."
    
