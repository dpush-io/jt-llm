
# 接口
- 请求地址：--
- 内容格式：Content-Type: applicaton/json
- 响应：
```json
  {
    "status": 1000,   // 1000 为正常
    "data": {},       // 业务数据，为对象或者数组
    "msg": ""         // 错误描述，无错误时为空
  }
```
- 关于 job_id：凡是涉及到异步操作的，如果成功接收到请求并且参数通过了验证，返回 job_id ，后台执行失败会自动重试，如果前台不关心这个处理进度，可以直接认为是成功了。如果在要异步操作后执行别的操作，例如发起文档对话，用 job_id 去轮询任务状态。
```json
  {
    "status": 1000,
    "data": {
      "job_id": 12345,
    },
    "msg": ""
  }
```

## 0、新增域
请求方式：POST

- 参数：无

- 响应

|字段名|类型|备注|
|-|-|-|
|domain_id|number|域ID|


## 1、分类变更
请求方式：POST
- 参数

|字段名|类型|备注|
|-|-|-|
|domain_id|number|域ID|
|cat_id|number|分类ID|
|parent_id|number|分类的父ID（更新的时候传新的父ID）|
|private|bool|是否私密|
|action|string|增删改：add、delete、update|

- 响应

|字段名|类型|备注|
|-|-|-|
|job_id|number|任务ID|


## 2、创建文档
请求方式：POST
- 参数

|字段名|类型|备注|
|-|-|-|
|domain_id|number|域ID|
|cat_id|number|分类ID|
|private|bool|是否私密|
|uuid|string|文档唯一ID|
|url|string|文档链接|
|md5|string|文档md5值|

- 返回

|字段名|类型|备注|
|-|-|-|
|job_id|number|任务ID|


## 3、删除文档
请求方式：POST
- 参数

|字段名|类型|备注|
|-|-|-|
|domain_id|number|域ID|
|uuid|string|文档唯一ID|

- 返回

|字段名|类型|备注|
|-|-|-|
|job_id|number|任务ID|

## 4、更新文档
请求方式：POST
- 参数

|字段名|类型|备注|
|-|-|-|
|domain_id|number|域ID|
|cat_id|number|分类ID|
|private|bool|是否私密|
|uuid|string|文档UUID|
|url|string|文档链接|
|md5|string|文档md5值|

- 返回

|字段名|类型|备注|
|-|-|-|
|job_id|number|任务ID|


## 5、发起文档对话
请求方式：POST
- 参数

|字段名|类型|备注|
|-|-|-|
|domain_id|number|域ID|
|uuids|[]string|文档UUID数组|
|cat_ids|[]number|分类ID数组|
|question|string|问题|
|generalize|bool|是否泛化|
|mode|string|对话模式：chat、summary|

- 返回

|字段名|类型|备注|
|-|-|-|
|job_id|number|任务ID|

## 6、获取会话ws链接
请求方式：POST
- 参数

|字段名|类型|备注|
|-|-|-|
|domain_id|number|域ID|
|job_id|number|任务ID|

- 返回

|字段名|类型|备注|
|-|-|-|
|ws_url|string|会话ws链接|


## 7、查询任务状态
请求方式：POST
- 参数

|字段名|类型|备注|
|-|-|-|
|domain_id|number|域ID|
|job_id|number|任务ID|

- 返回

|字段名|类型|备注|
|-|-|-|
|status|number|0-未开始；1-正在执行；2-执行成功；3-执行失败；99-任务失败，等待人工处理|
|step|number|当前进度|
