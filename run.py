import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
print(sys.path)

if __name__ == '__main__':
    pytest.main(["-v", "case/test_demo.py"])