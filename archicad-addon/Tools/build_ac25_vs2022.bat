pushd %~dp0
cmake -B ../Build/AC25 -G "Visual Studio 17 2022" -A "x64" -T "v142" -DAC_API_DEVKIT_DIR="C:\Program Files\GRAPHISOFT\API Development Kit 25.3002" .. || goto :error
cmake --build ../Build/AC25 --config Debug || goto :error
cmake --build ../Build/AC25 --config RelWithDebInfo || goto :error
popd
exit /b 0

:error
echo Build Failed with Error %errorlevel%.
popd
exit /b 1
