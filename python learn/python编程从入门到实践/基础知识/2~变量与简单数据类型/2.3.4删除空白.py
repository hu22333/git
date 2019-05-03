#python能够找出字符串开头和末尾多余的空白，可使用lstrip()和rstrip()
favorite_language =' python '
print(favorite_language)
print(favorite_language.lstrip())#lstrip删除前空格,rstrip删除后空格 
print(favorite_language.strip())#删除前与后空格
print(favorite_language)#删除只是暂时的删除，真正删除需将剔除空格后的结果存回原来的变量中
favorite_language=favorite_language.lstrip()
print(favorite_language)
