mkdir build -p &&
cd build &&
cmake .. &&
cmake --build . &&
cd .. &&
ctypesgen -l build/libRoboMasterUILib.so RM_Client_UI.h -o RM_Client_UI.py
# python3 hackctypesgen.py
