
# regex_pattern = r"^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"	# Do not delete 'r'.

import re
# print(str(bool(re.match(regex_pattern, "MMIMCMXCIX"))))
# print(str(bool(re.match(regex_pattern, input()))))


# 9587456281
# 1252478965
regex_pattern = r"[789][0-9]{9}"	# Do not delete 'r'.
print(str(bool(re.match(regex_pattern, "9587456281"))))