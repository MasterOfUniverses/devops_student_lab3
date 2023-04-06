import sys
import os


current_path = os.path.dirname(__file__)
parent_path = os.path.dirname(current_path)
src_path = parent_path + "src/"
test_path = parent_path + "test/"
sys.path.append(src_path)
sys.path.append(test_path)
sys.path.append(parent_path)
print(parent_path)
print(test_path)
print(src_path)
