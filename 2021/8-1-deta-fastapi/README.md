
- 视频 ？？

- 文档
    - 部署到Deta[Deploy FastAPI on Deta](https://fastapi.tiangolo.com/zh/deployment/deta/)
    - 开始启动[Getting Started](https://docs.deta.sh/docs/micros/getting_started/)

- 安装
```bash
(.py39) pro:~ play$ curl -fsSL https://get.deta.dev/cli.sh | sh
########################################################################################## 100.0%
Archive:  /Users/play/.deta/bin/deta.zip
  inflating: deta
  inflating: ._deta
Deta was installed successfully to /Users/play/.deta/bin/deta
Run 'deta --help' in a new shell to get started
```
- 登录
```bash
(.py39) pro:~ play$ /Users/play/.deta/bin/deta login
Please, log in from the web page. Waiting..
https://web.deta.sh/cli/52934
Logged in successfully.
```
- 新建
```bash
(.py39) pro:app play$ /Users/play/.deta/bin/deta new
Successfully created a new micro
{
	"name": "app",
	"runtime": "python3.7",
	"endpoint": "https://zba3nl.deta.dev",
	"visor": "enabled",
	"http_auth": "disabled"
}
Adding dependencies...
Collecting fastapi
  Downloading https://files.pythonhosted.org/packages/52/be/2a26007dc86c51e87d70021f6c1b3442726c5918fe57d27927badf687122/fastapi-0.67.0-py3-none-any.whl (51kB)
Collecting starlette==0.14.2
  Downloading https://files.pythonhosted.org/packages/15/34/db1890f442a1cd3a2c761f4109a0eb4e63503218d70a8c8e97faa09a5500/starlette-0.14.2-py3-none-any.whl (60kB)
Collecting pydantic!=1.7,!=1.7.1,!=1.7.2,!=1.7.3,!=1.8,!=1.8.1,<2.0.0,>=1.6.2
  Downloading https://files.pythonhosted.org/packages/9f/f2/2d5425efe57f6c4e06cbe5e587c1fd16929dcf0eb90bd4d3d1e1c97d1151/pydantic-1.8.2-cp37-cp37m-manylinux2014_x86_64.whl (10.1MB)
Collecting typing-extensions>=3.7.4.3
  Downloading https://files.pythonhosted.org/packages/2e/35/6c4fff5ab443b57116cb1aad46421fb719bed2825664e8fe77d66d99bcbc/typing_extensions-3.10.0.0-py3-none-any.whl
Installing collected packages: starlette, typing-extensions, pydantic, fastapi
Successfully installed fastapi-0.67.0 pydantic-1.8.2 starlette-0.14.2 typing-extensions-3.10.0.0
```
- 更新
```

```

## 数据库

## 文件存储