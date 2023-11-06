 
 
## 异步文档嵌入
请求方式：POST

地址: [请提供具体的请求地址]

- 参数

| 字段名 | 类型 | 必填 | 默认值 | 备注 |
| --- | --- | --- | --- | --- |
| doc_location | string | 是 |  | 文档内容的文件路径 |
| doc_id | string | 是 |  | 文档的唯一标识 |
| doc_name | string | 是 |  | 文档的名称 |
| category | string | 否 |  | 文档分类路径 |
| b_type | string | 是 |  | 文档的商业类型 |
| domain_id | string | 是 |  | 文档的所属域ID |
| chunk_size | int | 否 | 512 | 分块大小 |
| chunk_overlap | int | 否 | 100 | 分块重叠大小 |
| project_name | string | 否 | "default" | 项目名称 |
| pinecone_index_name | string | 否 | 默认值 | Pinecone索引名称 |
| pinecone_index_batch_size | int | 否 | 默认值 | Pinecone索引批处理大小 |
| mongodb_db | string | 否 | 默认值 | MongoDB数据库名 |
| mongodb_collection | string | 否 | 默认值 | MongoDB集合名 |
| extra_metadata | object | 否 | {} | 额外元数据 |

- 返回

| 字段名 | 类型 | 备注 |
| --- | --- | --- |
| job_id | string | 异步任务的唯一标识符 |

 

## 更新或插入文档元数据
请求方式：POST

地址: [请提供具体的请求地址]

- 参数

| 字段名 | 类型 | 必填 | 默认值 | 备注 |
| --- | --- | --- | --- | --- |
| doc_range | object | 否 | {} | 文档的筛选范围 |
| new_metadata | object | 是 |  | 要更新或插入的新元数据 |

文档筛选范围`doc_range`可以包含以下字段：

| 字段名 | 类型 | 备注 |
| --- | --- | --- |
| category | string | 分类过滤器 |
| b_type | array | 业务类型过滤器 |
| ids | array | 文档ID过滤器 |
| domain_id | string | 是 |  | 文档的所属域ID |

- 返回

| 字段名 | 类型 | 备注 |
| --- | --- | --- |
| job_id | string | 异步任务的唯一标识符 |
| status | string | 任务状态 |

 
 
md_del_document_template = """
## 标记文档为删除状态
请求方式：POST

地址: /delete

- 参数

| 字段名 | 类型 | 必填 | 备注 |
| --- | --- | --- | --- |
| ids | array | 是 | 要标记为删除的文档ID数组 |

- 返回

| 字段名 | 类型 | 备注 |
| --- | --- | --- |
| job_id | string | 异步任务的唯一标识符 |
| status | string | 任务状态 |
 


 

md_recover_document_template = """
## 恢复标记为删除的文档
请求方式：POST

地址: /recover

- 参数

| 字段名 | 类型 | 必填 | 备注 |
| --- | --- | --- | --- |
| ids | array | 是 | 要恢复的文档ID数组 |

- 返回

| 字段名 | 类型 | 备注 |
| --- | --- | --- |
| job_id | string | 异步任务的唯一标识符 |
| status | string | 任务状态 |
 


 handle_force_del_document

md_force_del_document_template = """
## 强制删除文档
请求方式：POST

地址: /force_delete

- 参数

| 字段名 | 类型 | 必填 | 备注 |
| --- | --- | --- | --- |
| ids | array | 是 | 要永久删除的文档ID数组 |

- 返回

| 字段名 | 类型 | 备注 |
| --- | --- | --- |
| job_id | string | 异步任务的唯一标识符 |
| status | string | 任务状态 |

 