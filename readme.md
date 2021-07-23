# Mission of Radar Station

## Requirements

Implement by [Pytorch](https://pytorch.org/get-started/locally/) framework on Ubuntu=18.04, python>=3.6, and Nvidia RTX 3070

For the installation of Nvidia Driver & Toolkits: [Web Of Official](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=18.04&target_type=runfile_local)

Please use [Anaconda](https://www.anaconda.com/) to deploy the environment (To better maintain the env, please create a new env instead of **base**), and use `pip install` command to download the following packages:

>torch>=1.9.0 & CUDA>=11.1
>
>numpy>=1.18.5
>
>opencv-python>=4.1.2
>
>PyYAML>=5.3.1
>
>scipy>=1.4.1
>
>matplotlib>=3.2.2
>
>tqdm>=4.41.0
>
>pandas
>
>Pillow
>
>easydict
>
>serial
>
>struct

For the installation of Zed Depth Camera, [Zed SDK](https://www.stereolabs.com/docs/installation/linux/). The following contents are the part copy of the SDK web.

**The USB of Zed Camera must plugin USB3.0 (blue)**


### Download and Install the ZED SDK

The [ZED SDK](https://www.stereolabs.com/developers/release/) for Linux contains all the drivers and libraries that powers your camera along with tools that let you test its features and settings.

- Download the [ZED SDK](https://www.stereolabs.com/developers/release/) for Linux.
- Go to the folder where the installer has been downloaded.

```bash
$ cd path/to/download/folder
```

- Add execution permission to the installer using the `chmod +x` command. Make sure to replace the installer name with the version you downloaded.

```bash
$ chmod +x ZED_SDK_Ubuntu18_v3.0.run
```

- Run the ZED SDK installer.

```bash
$ ./ZED_SDK_Ubuntu18_v3.0.run
```

- At the beginning of the installation, the Software License will be displayed, hit `q` after reading it.
- During the installation, you might have to answer some questions on dependencies, tools and samples installation. Type `y` for yes and `n` for no and hit `Enter`. Hit `Enter` to pick the default option.

#### Installing in silent mode

Silent-mode installation allows you to install specific configurations of the ZED SDK. It removes any display or manual configuration options during the installation process.

The installer can be launched in silent mode with the `-- silent` option (with a space between `--` an `silent`).

```bash
$ ./ZED_SDK_Ubuntu18_v3.0.run -- silent`
```

### INSTALLING SDK WITHOUT TOOLS

To install the ZED SDK without any tools or samples, add the `skip_tools` option.

```bash
$ ./ZED_SDK_Ubuntu18_v3.0.run -- silent skip_tools`
```

### INSTALLING RUNTIME VERSION ONLY

To install the ZED SDK without any static library, headers, tools or samples, add the `runtime_only` option.

```bash
$ ./ZED_SDK_Ubuntu18_v3.0.run -- silent runtime_only`
```

### Restart your computer

At the end of the installation, restart your system to make sure your paths are updated.

## Files

> All the codes have comment information. Study carefully!

- **docs**: The useful documents for someone who maintains the Station

- configs: The configs of deep_sort

- communicator: The communicator codes to communicate with **Judge System**

- demo: The demo of Videos

- deep_sort: The framework of DeepSort Algorithm

  ​	|---deep: Feature Extraction (using CNN)

  ​	|---sort: The details of Algorithm

- models: The models of yolov5

- pnp: Measuring distance (Deprecated framework of pnp, cause we use Zed Depth Camera)

- tools: The other tool codes

- yolov5: The network of yolov5

- main.py: `python main.py`

- detect.py: The codes using the pre-trained model(./yolov5/weights/best_DJI.pt) to detect cars

- camera.py: Utilizing Zed Depth Camera to capture real-time images, and integrating the neural network and the A board communication module to complete the overall process of the Radar Station

- paint.py: Painting on the map

- processor.py: Processing the images from the Zed



## Personnel


| **Staff** |             |
| --------- | ----------- |
| 曾聪      | **Manager** |
| 户英豪    |             |
| 魏然      |             |
| 张晨阳    |             |

