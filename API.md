# 版本 0.2.0 更新内容
1. 废弃 5、发起文档对话；6、获取会话ws链接。改为直接与 websocket 交互。
1. 文档的分类从只记录直接所属分类改为从上到下的分类路径，涉及：2、创建文档；4、更新文档。
1. 新增 8、批量操作文档的所属分类；9、websocket发送数据。
1. |private|bool|是否私密| 字段为预留，不做实际处理，可不传。


# 接口
- 版本：0.2.0
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
|category|string|分类路径|
|b_type|string|业务类型|
|private|bool|是否私密|
|uuid|string|文档唯一ID|
|url|string|文档链接|
|md5|string|文档md5值|

注：
- category: 必须从一级分类开始,用 / 分割不同级别的路径。 例如： 高速公路/公路养护/路基病害

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
|category|string|分类路径|
|b_type|string|业务类型|
|private|bool|是否私密|
|uuid|string|文档UUID|
|url|string|文档链接|
|md5|string|文档md5值|

注：
- category: 必须从一级分类开始,用 / 分割不同级别的路径。 例如： 高速公路/公路养护/路基病害
- 返回

|字段名|类型|备注|
|-|-|-|
|job_id|number|任务ID|




## ~~5、发起文档对话【已废弃】~~
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

## ~~6、获取会话ws链接【已废弃】~~
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

## 8、批量操作文档的所属分类 (del)
请求方式：POST
- 参数

|字段名|类型|备注|
|-|-|-|
|domain_id|number|域ID|
|category|string|最新的分类路径|
|uuids|[]string|文档UUID数组|

注：
- category: 必须从一级分类开始,用 / 分割不同级别的路径。 例如： 高速公路/公路养护/路基病害

- 返回

|字段名|类型|备注|
|-|-|-|
|job_id|number|任务ID|

## 9、websocket发送数据
请求方式：ws
- 参数

|字段名|类型|备注|
|-|-|-|
|message|string|发送的消息内容|
|doc_range|object|回答需要查找的范围|
|generalize|bool|是否泛化|
|generalize_b_type|object|泛化业务类型|
|is_summary|bool|是否是总结模式(默认为否，如果message提问方式是总结类，则会自动切换到总结类型的回答)|

doc_range
|字段名|类型|备注|
|-|-|-|
|category|string|分类路径|
|b_type|[]string|所有业务类型|
|ids|[]string|所有文章id|

注：
- category: 必须从一级分类开始,用 / 分割不同级别的路径。 例如： 高速公路/公路养护/路基病害
- b_type: 允许包含多个业务类型
- category 和 b_type 可以同时传入也可单独传入。 当ids也传入的情况下，优先考虑ids 。 优先级： ids> category/b_type

- 返回
```
<msg>包含了回复的信息内容</msg>
<ref>包含了引用的ID，上标显示。通常包含在 <msg></msg> 之中。 </ref>
<source>一个对象结构体，其中包含了引用的文档信息。通常接在信息</msg>之后</source>

</end> 所有数据发送完毕，会发送</end>的标记
```

source

|字段名|类型|备注|
|-|-|-|
|id|number|引用的ID|
|doc_id|string|引用文档的ID|
|doc_name|string|引用的文档名|
|score|number|匹配度分数|
|page|number|引用段落所属页码|


##恢复文档（批量，单个）
del 8

##通过文档得到3个问题 doc_range

##stop 

#模拟连接