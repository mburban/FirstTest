# 6.	В одномерном списке поменять местами минимальный и максимальный элементы. Остальные оставить на своих местах.
# *IN PLACE*

import random

m_list = list(set([random.randint(1, 10) for _ in range(10)]))
print(m_list)
min_value, max_value = min(m_list), max(m_list)
min_index, max_index = m_list.index(min_value), m_list.index(max_value)
m_list[min_index], m_list[max_index] = m_list[max_index], m_list[min_index]
print(m_list)