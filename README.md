## 使用FastAPI 构建的项目API

> 学习FastAPI 构建项目目录

<details>
<summary>项目文件结构</summary>

```
.
|_app                           // 主项目文件
| 
|___api
| |_____init__.py               // (重要) 生成app对象
| |____v1
| | |_____init__.py
| | |____database.py              // 数据库对象
| | |____schemas.py               // 验证参数       （可放到对应模块内)
| | |____models.py                // models模型类型 （可放到对应模块内)
| | |____home
| | | |____home.py
| | | |______init__.py
| | | |____home_backup.py
|____test                     // 测试用例
| |______init__.py
| |____test_sqlite.py
|____utils                    // 工具类
| |______init__.py
| |___response_code.py        // 自定义返回的状态码
|____setting                  // 配置文件夹
| |______init__.py            // 根据虚拟环境 导出不同配置
| |____development_config.py  // 开发环境配置
| |____production_config.py   // 生产环境配置
|____extensions               // 扩展文件(log)
| |______init__.py            //
| |____logger.py              // 
|____Pipfile
|____Pipfile.lock
|____requirements.text        // 依赖文件
|____main.py                  // 项目启动文件
|__mall_data.sql            // mysql insert 数据
|__mall_table.sql           // msyql表格 
|__README.md
|__.gitignore


```

</details>


## 导入数据

- mall_data.sql            // mysql insert 数据
- mall_table.sql           // msyql表格 

> 上面两个文件是mysql数据， 需自行导入

## 常规启动

#### 安装依赖
```
# 先进入到项目文件下
cd /项目目录/FastApiDemo-master

# 安装依赖
pip install -r requirements.text -i https://mirrors.aliyun.com/pypi/simple/

```
#### 启动
直接执行
```
python main.py
```