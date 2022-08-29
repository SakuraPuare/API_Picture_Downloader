# API 图片下载器

## 简介

这是一个用于批量API访问下载图片的Python脚本模板，是为了防止书樱多次造轮子而上传。

此脚本以`https://mirlkoi.ifast3.vipnps.vip/Tag/Random/mobile.php`为模板，实现了批量访问并提取图片链接异步下载的功能。

仅供学习参考！

## 使用

### 安装依赖

`pip install -r requirements.txt`

### 开始下载

`python main.py`

### 建立数据库

数据库目前为`json`格式，内有文件名`name`、dhash值`dhash`、高度`height`、宽度`width`和图片链接`url`等信息。

`python json_dict.py`

## 图片

下载的图片请查看其他branch
