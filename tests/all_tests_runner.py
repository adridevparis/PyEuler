from tests.pb1_test import Pb1Test
from tests.pb2_test import Pb2Test
from tests.pb3_test import Pb3Test
from tests.pb4_test import Pb4Test
from tests.pb5_test import Pb5Test

if __name__ == '__main__':
    Pb1Test().run_all()
    Pb2Test().run_all()
    Pb3Test().run_all()
    Pb4Test().run_all()
    Pb5Test().run_all()