import os

# 根目录
base_dir = os.path.dirname(os.path.dirname(__file__))

testdatas_dir = os.path.join(base_dir, "TestDatas")

testcases_dir = os.path.join(base_dir, "TestCases")

outputs_path = os.path.join(base_dir, 'Outputs')

htmlreport_dir = os.path.join(base_dir, "Outputs/Reports")

logs_dir = os.path.join(base_dir, "Outputs/Logs")


