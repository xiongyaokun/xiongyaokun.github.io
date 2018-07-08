## Python 创建虚拟环境：Anaconda之conda——Virtualenv——Python3 venv

### 1.conda创建虚拟环境

#### 1.1.常用命令注意：
1. __--help__ 和 __-h__
2. __--name__ 和 __-n__

#### 1.2.查看包
- conda list 查看安装了哪些包
- conda env list 查看有哪些虚拟环境
- conda -V 或者 conda --version 查看conda的版本

#### 1.3.创建虚拟环境，命名为 **myflaskapp**, **n** 就是指 **name**, 并安装flask包。
conda创建虚拟环境时，必须指定一个或者几个需要使用的 **package**

    conda create -n py2 python=2* anaconda
    这样就会安装anaconda2版本

##### 例子1：
这条命令创建了一个名为myflaskapp的虚拟环境，安装flask包：
    conda create -n myflaskapp flask

##### 例子2：
这个是克隆了一个和原系统一样的python环境,命名为nb：

    conda create -n nb --clone root

##### 例子3：
下面这个就不需要指定具体的包了：

    conda create --name your_env_name

创建指定版本的python环境

    1. conda create --name your_env_name python=2.7
    2. conda create --name your_env_name python=3
    3. conda create --name your_env_name python=3.5

创建包含某些包的环境

    1. conda create --name your_env_name numpy scipy

创建指定版本下包含某些包的环境

    1. conda create --name your_env_name python=3.5 numpy scipy

列举当前所有环境：

    1. conda info --envs
    2. conda env list

进入某个环境：

    1. activate your_env_name


推出当前环境：

    1. deactivate

复制某个环境：

    1. conda create --name new_env_name --clone old_env_name

删除环境：

    1. conda remove --name your_env_name --all

#### 1.4.分享环境

如果你想把当前的环境配置与别人分享，这条TA可以快速建立一个与你一模一样的环境（同一个版本的python及各种包）来共同开发/进行新的实验。
一个分享环境的快速方法就是给ta一个你的环境的 **.yml** 文件。

首先通过 activate target_env 命令，激活目标环境，然后使用下面的命令会在当前的工作目录下生成一个 environment.yml的文件，

    conda env export > environment.yml

当然，你也可以手写一个 **.yml** 文件用来描述你的python环境配置。

#### 1.5.包管理

列举当前活跃环境下的所有包：

    1.conda list

列举一个非当前活跃环境下的所有包：

    1.conda list -n your_env_name

为指定环境安装某个包：

    1.conda install -n env_name package_name

如果不能通过**conda install**来安装，文档中提到可以从**Anaconda.org**来安装，但我觉得更习惯使用**pip**直接安装，
**pip**在**Anaconda**中已经安装好，不需要为每个环节单独安装**pip**。如果想使用**pip**管理包，**activate**环境后，直接使用即可。

### 2.Virtualenv创建虚拟环境

#### 2.1 安装virtualenv

    pip install virtualenv

#### 2.2 创建虚拟环境

    $ mkdir myproject
    $ cd myproject
    $ virtualenv venv

创建一个名为myproject的文件夹，然后再里面创建虚拟环境venv。

### 3.Python3 venv

#### 3.1创建虚拟环境

Python3官方版本自带创建虚拟环境的功能：

    python -m venv myvenv

#### 3.2激活

    Windows下：myvenv\Scripts\activate.bat

