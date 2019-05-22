自拍坊程序
==========
给人脸添加特效

本地运行、开发步骤
==============
* 安装 git (https://git-scm.com/)

```
git clone https://github.com/JeffTrain/selfie2.git
```

### OS X:
* 安装 CMake
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
brew install cmake
```

### Windows:
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


* 安装依赖
```
pip3 install -r requirements.txt
```
* 运行
```
python3 app.py
```

注意，如果没有摄像头设备，程序会报错退出：

```
OpenCV: AVFoundation didn't find any attached Video Input Devices!
OpenCV: camera failed to properly initialize!
Traceback (most recent call last):
  File "app.py", line 69, in <module>
    scale = 200 / min(image.shape[0], image.shape[1])
AttributeError: 'NoneType' object has no attribute 'shape'
```
