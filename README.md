自拍坊程序
==========
给人脸添加特效

安装依赖注意事项
==============
* 安装 git (https://git-scm.com/)
* 安装 python (https://www.python.org/)
* 安装 opencv 
```
pip install opencv-python
```
* 安装 dlib （https://www.learnopencv.com/install-dlib-on-windows/）
- 安装 Visual Studio (2013、2015、2017 都可以)
- 安装 CMake
- 下载 Dlib ( http://dlib.net/files/dlib-19.6.zip)
- 编译 Dlib 
```
cd dlib-19.6\
mkdir build
cd build
 
# This is a single command. Backticks are used for line continuation
cmake -G "Visual Studio 14 2015 Win64" `
-DJPEG_INCLUDE_DIR=..\dlib\external\libjpeg `
-DJPEG_LIBRARY=..\dlib\external\libjpeg `
-DPNG_PNG_INCLUDE_DIR=..\dlib\external\libpng `
-DPNG_LIBRARY_RELEASE=..\dlib\external\libpng `
-DZLIB_INCLUDE_DIR=..\dlib\external\zlib `
-DZLIB_LIBRARY_RELEASE=..\dlib\external\zlib `
-DCMAKE_INSTALL_PREFIX=install ..
 
cmake --build . --config Release --target INSTALL
cd ..
```