# 接口
- 版本：0.3.0
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

## 1、批量创建文档
请求方式：POST
- 参数

|字段名|类型|备注|
|-|-|-|
|domain_id|number|域ID|
|docs|[]object|文档对象数组|
|- b_type|string|业务类型|
|- private|bool|是否私密|
|- uuid|string|文档唯一ID|
|- url|string|文档链接|
|- md5|string|文档md5值|

- 返回

|字段名|类型|备注|
|-|-|-|
|job_id|number|任务ID|


## 2、批量删除文档
请求方式：POST
- 参数

|字段名|类型|备注|
|-|-|-|
|domain_id|number|域ID|
|uuids|[]string|文档唯一ID数组|

- 返回

|字段名|类型|备注|
|-|-|-|
|job_id|number|任务ID|


## 3、批量恢复文档
请求方式：POST
- 参数

|字段名|类型|备注|
|-|-|-|
|domain_id|number|域ID|
|uuids|[]string|文档唯一ID数组|

- 返回

|字段名|类型|备注|
|-|-|-|
|job_id|number|任务ID|


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
|detail|[]object|当前进度，数组|
|- related_id|string|任务的子项关联的ID，如文档uuid等|
|- status|number|0-未开始；1-正在执行；2-执行成功；3-执行失败；99-任务失败，等待人工处理|


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