# Billing overview
# https://platform.openai.com/

import os
import openai
openai.organization = "org-kKd2RYxKu2zAcqTGE1to8zxP"
openai.api_key = os.getenv("OPENAI_API_KEY")

# bsmouse test........github
# 11:41 추가
# 13:56
# 13:58
# 14:57

print(openai.Model.list())
# print(openai.api_key)
