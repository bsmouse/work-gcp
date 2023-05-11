# Billing overview
# https://platform.openai.com/

import os
import openai
openai.organization = "org-kKd2RYxKu2zAcqTGE1to8zxP"
openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = "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"
# print(openai.Model.list())
print(openai.api_key)
